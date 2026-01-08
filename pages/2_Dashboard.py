import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("📊 Student Performance Analytics Dashboard")

data = pd.read_csv("student_data.csv")

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(data))
col2.metric("Safe Students", int(data["final_result"].sum()))
col3.metric("At Risk Students", int(len(data) - data["final_result"].sum()))

st.divider()

# Attendance Distribution
st.subheader("Attendance Distribution")
fig, ax = plt.subplots()
ax.hist(data["attendance"], bins=10)
ax.set_xlabel("Attendance %")
ax.set_ylabel("Number of Students")
st.pyplot(fig)

# Performance Comparison
st.subheader("Internal Marks vs Final Result")
fig, ax = plt.subplots()
ax.boxplot(
    [data[data["final_result"] == 1]["internal_marks"],
     data[data["final_result"] == 0]["internal_marks"]],
    labels=["Safe", "At Risk"]
)
ax.set_ylabel("Internal Marks")
st.pyplot(fig)
