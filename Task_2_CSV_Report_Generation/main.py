from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "StudentsPerformance.csv"
OUTPUT_DIR = BASE_DIR / "output"


def main():
    try:
        # Read dataset
        df = pd.read_csv(DATA_FILE)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        print("===== CSV DATA ANALYZER =====")
        print("File:", DATA_FILE.name)
        print("Total Rows:", len(df))
        print("Total Columns:", len(df.columns))

        # 1. Average score chart
        score_columns = [
            "math score",
            "reading score",
            "writing score"
        ]

        averages = df[score_columns].mean()

        plt.figure(figsize=(8, 5))
        averages.plot(kind="bar")
        plt.title("Average Student Scores")
        plt.xlabel("Subject")
        plt.ylabel("Average Score")
        plt.ylim(0, 100)
        plt.tight_layout()

        score_chart = OUTPUT_DIR / "average_scores.png"
        plt.savefig(score_chart)
        plt.close()

        # 2. Gender distribution chart
        gender_counts = df["gender"].value_counts()

        plt.figure(figsize=(6, 6))
        gender_counts.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90
        )
        plt.title("Student Distribution by Gender")
        plt.ylabel("")

        gender_chart = OUTPUT_DIR / "gender_distribution.png"
        plt.tight_layout()
        plt.savefig(gender_chart)
        plt.close()

        # 3. Math score distribution chart
        plt.figure(figsize=(8, 5))
        df["math score"].plot(
            kind="hist",
            bins=10,
            edgecolor="black"
        )
        plt.title("Math Score Distribution")
        plt.xlabel("Math Score")
        plt.ylabel("Number of Students")
        plt.tight_layout()

        histogram_chart = OUTPUT_DIR / "math_score_distribution.png"
        plt.savefig(histogram_chart)
        plt.close()

        # Create HTML report
        report_file = OUTPUT_DIR / "report.html"

        
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, initial-scale=1.0">
            <title>Student Performance Analytics</title>

            <style>
                * {{
                    box-sizing: border-box;
                }}

                body {{
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: #f1f5f9;
                    color: #1e293b;
                }}

                header {{
                    background: #172554;
                    color: white;
                    padding: 30px 6%;
                }}

                header h1 {{
                    margin: 0 0 10px;
                    font-size: 30px;
                }}

                header p {{
                    margin: 0;
                    color: #dbeafe;
                }}

                main {{
                    max-width: 1100px;
                    margin: 25px auto;
                    padding: 0 20px;
                }}

                .cards {{
                    display: grid;
                    grid-template-columns:
                        repeat(auto-fit, minmax(200px, 1fr));
                    gap: 18px;
                }}

                .card {{
                    background: white;
                    padding: 22px;
                    margin-bottom: 20px;
                    border-radius: 12px;
                    box-shadow: 0 3px 12px #0000000d;
                }}

                .stat h2 {{
                    font-size: 32px;
                    color: #2563eb;
                    margin: 10px 0;
                }}

                .muted {{
                    color: #64748b;
                    font-size: 14px;
                }}

                .chart {{
                    width: 100%;
                    max-width: 750px;
                    display: block;
                    margin: 15px auto;
                }}

                li {{
                    margin: 9px 0;
                }}

                footer {{
                    text-align: center;
                    padding: 25px;
                    color: #64748b;
                }}
            </style>
        </head>

        <body>
            <header>
                <h1>Student Performance Analytics</h1>
                <p>Automated CSV Analysis & Visualization Report</p>
            </header>

            <main>
                <section class="cards">
                    <div class="card stat">
                        <p class="muted">Total Rows / Students</p>
                        <h2>{len(df):,}</h2>
                    </div>

                    <div class="card stat">
                        <p class="muted">Total Columns</p>
                        <h2>{len(df.columns)}</h2>
                    </div>

                    <div class="card stat">
                        <p class="muted">Average Math Score</p>
                        <h2>{averages["math score"]:.1f}</h2>
                    </div>
                </section>

                <section class="card">
                    <h2>Dataset Overview</h2>
                    <p><b>Source file:</b> {DATA_FILE.name}</p>
                    <p><b>Subjects analyzed:</b>
                       Math, Reading and Writing</p>
                </section>

                <section class="card">
                    <h2>Average Scores by Subject</h2>
                    <p class="muted">
                        Compare the average scores across all three subjects.
                    </p>
                    <img class="chart" src="average_scores.png"
                         alt="Average scores bar chart">
                </section>

                <section class="card">
                    <h2>Student Distribution by Gender</h2>
                    <img class="chart" src="gender_distribution.png"
                         alt="Gender distribution pie chart">
                </section>

                <section class="card">
                    <h2>Math Score Distribution</h2>
                    <p class="muted">
                        This histogram shows how math scores are distributed.
                    </p>
                    <img class="chart" src="math_score_distribution.png"
                         alt="Math score histogram">
                </section>

                <section class="card">
                    <h2>Average Score Details</h2>
                    <ul>
                        {"".join(
                            f"<li>{subject.title()}: {score:.2f}</li>"
                            for subject, score in averages.items()
                        )}
                    </ul>
                </section>

                <section class="card">
                    <h2>Dataset Columns</h2>
                    <ul>
                        {"".join(
                            f"<li>{column}</li>"
                            for column in df.columns
                        )}
                    </ul>
                </section>
            </main>

            <footer>
                CSV Data Analyzer | Python & Pandas
            </footer>
        </body>
        </html>
        """


        report_file.write_text(html, encoding="utf-8")

        # Also save a simple text summary
        summary_file = OUTPUT_DIR / "summary_report.txt"
        with open(summary_file, "w", encoding="utf-8") as file:
            file.write("CSV DATA ANALYZER REPORT\n\n")
            file.write(f"File: {DATA_FILE.name}\n")
            file.write(f"Rows: {len(df)}\n")
            file.write(f"Columns: {len(df.columns)}\n\n")
            file.write("Average Scores:\n")
            file.write(averages.round(2).to_string())

        print("\nReports generated successfully!")
        print("HTML report:", report_file)
        print("Charts saved in:", OUTPUT_DIR)

    except FileNotFoundError:
        print("Error: Check that the CSV exists inside the data folder.")

    except KeyError as error:
        print(f"Error: A required dataset column is missing: {error}")

    except Exception as error:
        print("Something went wrong:", error)


if __name__ == "__main__":
    main()
