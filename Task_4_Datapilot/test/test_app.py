
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_analyze_valid_csv():
    csv_content = (
        "Name,Marks\n"
        "Ali,85\n"
        "Ahmed,90\n"
        "Sara,75\n"
    )

    response = client.post(
        "/analyze",
        files={
            "file": (
                "students.csv",
                csv_content,
                "text/csv"
            )
        }
    )

    assert response.status_code == 200

    result = response.json()["analysis"]

    assert result["total_rows"] == 3
    assert result["total_columns"] == 2
    assert result["missing_values"] == 0
    assert result["duplicate_rows"] == 0


def test_analyze_invalid_file():
    response = client.post(
        "/analyze",
        files={
            "file": (
                "notes.txt",
                "This is not a CSV file",
                "text/plain"
            )
        }
    )

    assert response.status_code == 400
