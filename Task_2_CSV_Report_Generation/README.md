# CSV Data Analyzer & Report Automation Tool

## Project Overview

CSV Data Analyzer is a beginner-friendly Python automation project that reads CSV data, calculates basic statistics, generates visualizations, and creates an HTML report automatically.

This project was developed as part of the GIST Python Developer Internship — Task 2.

## Features

- Reads CSV datasets using Pandas.
- Displays the total number of rows and columns.
- Lists dataset column names.
- Calculates average student scores.
- Generates a bar chart for average subject scores.
- Creates a pie chart for gender distribution.
- Creates a histogram for math score distribution.
- Generates a professional HTML report.
- Saves a simple text summary.
- Handles common file and dataset errors.

## Technologies Used

- Python
- Pandas
- Matplotlib
- pathlib
- HTML and CSS

## Dataset

**Dataset:** Students Performance in Exams

**Source:** [Kaggle — Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

The dataset includes student demographic information and math, reading, and writing scores.

## Project Structure

```text
csv_report_generation/
├── data/
│   └── StudentsPerformance.csv
├── output/
│   ├── report.html
│   ├── summary_report.txt
│   ├── average_scores.png
│   ├── gender_distribution.png
│   └── math_score_distribution.png
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Install Python.
2. Clone or download this repository.
3. Open a terminal inside the project folder.
4. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Place `StudentsPerformance.csv` inside the `data` folder.

## Run the Project

```bash
python main.py
```

The program processes the CSV file and generates the report and charts in the `output` folder.

Open `output/report.html` in a web browser to view the visual report.

## Learning Outcomes

- CSV processing with Pandas.
- Basic data analysis and statistics.
- Data visualization with Matplotlib.
- Automated report generation.
- File and folder management with pathlib.
- Project documentation and dependency management.

## Author

Developed as a Python Developer Internship project.
