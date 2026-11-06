
import sqlite3
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "datapilot.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS analysis_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL,
                total_rows INTEGER NOT NULL,
                total_columns INTEGER NOT NULL,
                missing_values INTEGER NOT NULL,
                duplicate_rows INTEGER NOT NULL,
                analyzed_at TEXT NOT NULL
            )
        """)


def save_analysis(
    file_name,
    total_rows,
    total_columns,
    missing_values,
    duplicate_rows
):
    analyzed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as connection:
        connection.execute("""
            INSERT INTO analysis_history (
                file_name,
                total_rows,
                total_columns,
                missing_values,
                duplicate_rows,
                analyzed_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            file_name,
            total_rows,
            total_columns,
            missing_values,
            duplicate_rows,
            analyzed_at
        ))


def get_history():
    with get_connection() as connection:
        cursor = connection.execute("""
            SELECT
                id,
                file_name,
                total_rows,
                total_columns,
                missing_values,
                duplicate_rows,
                analyzed_at
            FROM analysis_history
            ORDER BY id DESC
        """)

        return cursor.fetchall()
