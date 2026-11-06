# DataPilot — CSV Analytics & Automation Platform

DataPilot is a Python-based web application that analyzes CSV datasets, generates interactive visualizations, stores analysis history in SQLite, and provides a REST API for CSV analysis.

## Features

- Upload and analyze CSV files
- View dataset rows, columns, missing values, and duplicate rows
- Explore interactive charts using Plotly
- Download analyzed data as CSV
- Save analysis history in SQLite
- Analyze CSV files through a FastAPI REST API
- Test API endpoints using automated tests

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- FastAPI
- SQLite
- Pytest

## Installation

1. Clone this repository.
2. Open the project folder in your terminal.
3. Create and activate a virtual environment.
4. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Dashboard

```bash
streamlit run app.py
```

## Run the API

Open a separate terminal and run:

```bash
python -m uvicorn api:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore the API.

## Run Tests

```bash
python -m pytest -v
```

## Project Structure

```text
Task_4_Datapilot/
├── app.py
├── api.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
├── tests/
└── output/
```

## Purpose

This project demonstrates CSV data analysis, interactive dashboard development, REST API creation, database integration, and automated testing.
