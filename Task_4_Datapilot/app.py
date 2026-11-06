
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import database

database.initialize_database()

# Page configuration
st.set_page_config(
    page_title="DataPilot | CSV Analytics",
    page_icon="📊",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
    .main-title {
        font-size: 36px;
        font-weight: 700;
        color: #2563eb;
    }
    .subtitle {
        color: #64748b;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="main-title">DataPilot Analytics</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">CSV Data Analysis & Automation Platform</div>',
    unsafe_allow_html=True
)

st.divider()

# Sidebar
st.sidebar.title("⚙️ DataPilot")
st.sidebar.write("Upload your CSV dataset to begin.")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# Load uploaded file or sample dataset
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        source_name = uploaded_file.name
    except Exception as error:
        st.error(f"Unable to read CSV file: {error}")
        st.stop()
else:
    # Load the existing sample dataset if available
    data_file = (
        Path(__file__).resolve().parent
        / "data"
        / "StudentsPerformance.csv"
    )

    if data_file.exists():
        try:
            df = pd.read_csv(data_file)
            source_name = data_file.name
        except Exception as error:
            st.error(f"Unable to read sample CSV: {error}")
            st.stop()
    else:
        st.info("Upload a CSV file from the sidebar to get started.")
        st.stop()

if df.empty:
    st.warning("The selected CSV file has no data.")
    st.stop()

# Dataset overview
st.subheader("📌 Dataset Overview")
st.caption(f"Current file: {source_name}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Rows", f"{df.shape[0]:,}")

with col2:
    st.metric("Total Columns", f"{df.shape[1]:,}")

with col3:
    st.metric(
        "Missing Values",
        f"{int(df.isnull().sum().sum()):,}"
    )

with col4:
    st.metric(
        "Duplicate Rows",
        f"{int(df.duplicated().sum()):,}"
    )


st.divider()
st.subheader("💾 Save Analysis")

if st.button("Save Current Analysis", type="primary"):
    try:
        database.save_analysis(
            file_name=source_name,
            total_rows=int(df.shape[0]),
            total_columns=int(df.shape[1]),
            missing_values=int(df.isnull().sum().sum()),
            duplicate_rows=int(df.duplicated().sum())
        )
        st.success("Analysis saved to database successfully!")
    except Exception as error:
        st.error(f"Unable to save analysis: {error}")

# Data preview
st.divider()
st.subheader("🔍 Dataset Preview")

preview_rows = st.slider(
    "Number of rows to display",
    min_value=5,
    max_value=50,
    value=10
)

st.dataframe(
    df.head(preview_rows),
    use_container_width=True
)

# Column information
with st.expander("View Column Information"):
    column_info = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Missing Values": df.isnull().sum().values,
        "Unique Values": df.nunique().values
    })

    st.dataframe(column_info, use_container_width=True)

# Charts
st.divider()
st.subheader("📈 Interactive Visualizations")

numeric_columns = df.select_dtypes(
    include="number"
).columns.tolist()

if numeric_columns:
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        selected_column = st.selectbox(
            "Select a numeric column",
            numeric_columns
        )

        histogram = px.histogram(
            df,
            x=selected_column,
            title=f"Distribution of {selected_column}",
            color_discrete_sequence=["#3b82f6"]
        )

        st.plotly_chart(
            histogram,
            use_container_width=True
        )

    with chart_col2:
        average_values = df[numeric_columns].mean().reset_index()
        average_values.columns = ["Column", "Average"]

        bar_chart = px.bar(
            average_values,
            x="Column",
            y="Average",
            title="Average Values by Numeric Column",
            color="Column"
        )

        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

else:
    st.info("No numeric columns are available for numeric charts.")

# Categorical chart
categorical_columns = df.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

if categorical_columns:
    st.subheader("📊 Category Distribution")

    selected_category = st.selectbox(
        "Select a categorical column",
        categorical_columns
    )

    category_counts = (
        df[selected_category]
        .fillna("Missing")
        .astype(str)
        .value_counts()
        .head(15)
        .reset_index()
    )

    category_counts.columns = ["Category", "Count"]

    pie_chart = px.pie(
        category_counts,
        names="Category",
        values="Count",
        title=f"Distribution of {selected_category}",
        hole=0.35
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

# Download cleaned export (original data is not modified)
st.divider()
st.subheader("📥 Export Dataset")

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="datapilot_export.csv",
    mime="text/csv"
)

st.success("DataPilot is ready. Upload another CSV to analyze it!")


# Analysis History
st.divider()
st.subheader("🗂️ Analysis History")

try:
    history = database.get_history()

    if history:
        history_columns = [
            "ID",
            "File Name",
            "Rows",
            "Columns",
            "Missing Values",
            "Duplicate Rows",
            "Analyzed At"
        ]

        history_df = pd.DataFrame(
            history,
            columns=history_columns
        )

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            f"Total saved analyses: {len(history_df)}"
        )

    else:
        st.info(
            "No saved analyses yet. "
            "Click 'Save Current Analysis' to create your first record."
        )

except Exception as error:
    st.error(f"Unable to load analysis history: {error}")
