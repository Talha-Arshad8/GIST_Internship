
from io import BytesIO

import pandas as pd
from fastapi import FastAPI, File, HTTPException, UploadFile

import database

app = FastAPI(
    title="DataPilot API",
    description="CSV analysis and history API",
    version="1.0.0"
)

database.initialize_database()


@app.get("/")
def home():
    return {
        "message": "Welcome to DataPilot API",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/history")
def analysis_history():
    try:
        history = database.get_history()

        columns = [
            "id",
            "file_name",
            "total_rows",
            "total_columns",
            "missing_values",
            "duplicate_rows",
            "analyzed_at"
        ]

        records = [
            dict(zip(columns, row))
            for row in history
        ]

        return {
            "total_records": len(records),
            "history": records
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve analysis history"
        ) from error


@app.post("/analyze")
async def analyze_csv(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a CSV file."
        )

    try:
        content = await file.read()

        if not content:
            raise HTTPException(
                status_code=400,
                detail="The uploaded CSV file is empty."
            )

        df = pd.read_csv(BytesIO(content))

        if df.empty or len(df.columns) == 0:
            raise HTTPException(
                status_code=400,
                detail="The CSV contains no usable data."
            )

        result = {
            "file_name": file.filename,
            "total_rows": int(df.shape[0]),
            "total_columns": int(df.shape[1]),
            "missing_values": int(df.isnull().sum().sum()),
            "duplicate_rows": int(df.duplicated().sum()),
            "columns": df.columns.tolist()
        }

        database.save_analysis(
            file_name=result["file_name"],
            total_rows=result["total_rows"],
            total_columns=result["total_columns"],
            missing_values=result["missing_values"],
            duplicate_rows=result["duplicate_rows"]
        )

        return {
            "message": "CSV analyzed and saved successfully.",
            "analysis": result
        }

    except HTTPException:
        raise

    except pd.errors.EmptyDataError as error:
        raise HTTPException(
            status_code=400,
            detail="The CSV file has no readable data."
        ) from error

    except pd.errors.ParserError as error:
        raise HTTPException(
            status_code=400,
            detail="The CSV file format is invalid."
        ) from error

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred during analysis."
        ) from error

    finally:
        await file.close()
