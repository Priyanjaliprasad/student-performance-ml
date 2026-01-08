import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

features = [
    "Attendance",
    "Study Hours",
    "Internal Marks",
    "Previous GPA",
    "Assignments Completed"
]

importance = model.feature_importances_
df = pd.DataFrame({"Feature": features, "Importance": importance})

st.header("📌 Feature Importance Analysis")

fig, ax = plt.subplots()
ax.barh(df["Feature"], df["Importance"])
ax.set_xlabel("Importance Score")
st.pyplot(fig)

st.info("This shows which academic factors influence student performance the most.")

st.markdown("""
### 📘 Interpretation
- Higher importance means stronger influence on prediction
- Attendance and GPA usually dominate performance outcomes
- Helps faculty focus on critical parameters
""")
