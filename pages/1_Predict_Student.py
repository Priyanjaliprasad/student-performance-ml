import streamlit as st
import numpy as np
import pickle
from utils.pdf_generator import generate_pdf

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.header("📌 Student Performance Prediction")

# Initialize session state
if "predicted" not in st.session_state:
    st.session_state.predicted = False

# Inputs
attendance = st.slider("Attendance (%)", 0, 100, 75)
study_hours = st.slider("Study Hours per Day", 0, 10, 2)
internal_marks = st.slider("Internal Marks", 0, 100, 60)
previous_gpa = st.slider("Previous GPA", 0.0, 10.0, 6.5)
assignments_completed = st.selectbox("Assignments Completed", [0, 1])

# Predict button
if st.button("Predict Performance"):
    input_data = np.array([[attendance, study_hours, internal_marks, previous_gpa, assignments_completed]])
    prediction = model.predict(input_data)[0]

    # Store EVERYTHING
    st.session_state.predicted = True
    st.session_state.status = "Safe" if prediction == 1 else "At Risk"
    st.session_state.inputs = {
        "attendance": attendance,
        "study_hours": study_hours,
        "internal_marks": internal_marks,
        "previous_gpa": previous_gpa,
        "assignments_completed": assignments_completed
    }

# Show result ONLY if predicted
if st.session_state.predicted:

    if st.session_state.status == "Safe":
        st.success("✅ Student is Performing Well")

        st.subheader("📈 Strengths")
        if attendance >= 75:
            st.write("✔ Good attendance")
        if study_hours >= 2:
            st.write("✔ Consistent study habits")
        if internal_marks >= 60:
            st.write("✔ Satisfactory internal performance")
        if previous_gpa >= 6.0:
            st.write("✔ Stable academic foundation")

    else:
        st.error("⚠️ Student is At Risk of Dropout")

        st.subheader("🛠 Areas of Improvement")
        if attendance < 75:
            st.write("❌ Attendance is low – improve class participation")
        if study_hours < 2:
            st.write("❌ Study hours are insufficient")
        if internal_marks < 60:
            st.write("❌ Internal marks need improvement")
        if previous_gpa < 6.0:
            st.write("❌ Weak academic foundation – seek mentoring")

        st.subheader("📌 Recommended Actions")
        st.write("- Attend remedial classes")
        st.write("- Follow structured study timetable")
        st.write("- Regular mentor interaction")

    # PDF section
    st.divider()

    if st.button("📄 Generate PDF Report"):
        file_path = generate_pdf(
            st.session_state.inputs["attendance"],
            st.session_state.inputs["study_hours"],
            st.session_state.inputs["internal_marks"],
            st.session_state.inputs["previous_gpa"],
            st.session_state.inputs["assignments_completed"],
            st.session_state.status
        )

        with open(file_path, "rb") as pdf:
            st.download_button(
                "⬇️ Download Student Report",
                data=pdf,
                file_name="Student_Report.pdf",
                mime="application/pdf"
            )
