import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="📑",
    layout="wide"

)
st.title("📑 Personal Expense Tracker")
st.write(
    "Upload your expenses CSV file, filter transactions by date and category, "
    "and analyze your spending patterns."
)

uploaded_file = st.file_uploader(
    "Upload expenses.csv",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Please upload expenses.csv to get started.")
    st.stop()

df = pd.read_csv(r"C:\Users\Scalefusion admin\project_4.1\data\expences.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

st.header("Filters")

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Handle single date selection
if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = min_date
    end_date = max_date

all_categories = sorted(df["Category"].unique())

selected_categories = st.multiselect(
    "Select Categories",
    options=all_categories,
    default=all_categories
)

# Guard if user deselects everything
if not selected_categories:
    selected_categories = all_categories

filtered_df = df[
    (df["Date"].dt.date >= start_date) &
    (df["Date"].dt.date <= end_date)
]

filtered_df = filtered_df[
    filtered_df["Category"].isin(selected_categories)
]

total_spend = filtered_df["Amount"].sum()
transaction_count = len(filtered_df)
average_transaction = filtered_df["Amount"].mean()
largest_expense = filtered_df["Amount"].max()

st.subheader("📊 Expense Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Spend",
    f"₹{total_spend:,.2f}"
)

col2.metric(
    "Transactions",
    f"{transaction_count}"
)

col3.metric(
    "Average Transaction",
    f"₹{average_transaction:,.2f}"
)

col4.metric(
    "Largest Expense",
    f"₹{largest_expense:,.2f}"
)

st.subheader("📋 Filtered Transactions")

st.dataframe(
    filtered_df,
    hide_index=True,
    use_container_width=True
)

csv = filtered_df.to_csv(index=False).encode("utf-8")

filename = (
    f"expenses_"
    f"{start_date.strftime('%Y-%m-%d')}_"
    f"{end_date.strftime('%Y-%m-%d')}.csv"
)

st.download_button(
    label="⬇ Download Filtered CSV",
    data=csv,
    file_name=filename,
    mime="text/csv"
)

st.subheader("Spend by Category")

bar_color = st.color_picker(
    "Choose Bar Colour",
    "#3B82F6"
)

st.write(f"Selected Colour: {bar_color}")

category_spend = (
    filtered_df
    .groupby("Category")["Amount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_spend)

st.subheader("Monthly Summary")

monthly_summary = (
    filtered_df
    .assign(Month=filtered_df["Date"].dt.month_name())
    .groupby("Month")
    .agg(
        Total_Spend=("Amount", "sum"),
        Transactions=("Amount", "count")
    )
    .reset_index()
)

st.table(monthly_summary)

st.markdown("---")

today = datetime.today().strftime("%d-%m-%Y")

st.caption(
    f"Created by Muhammed Faiz | Personal Expense Tracker | {today}"
)


