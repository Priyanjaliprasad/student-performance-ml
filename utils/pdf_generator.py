from fpdf import FPDF

def generate_pdf(attendance, study_hours, internal_marks,
                 previous_gpa, assignments, status):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Student Performance Prediction Report", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 8, f"Attendance: {attendance}%", ln=True)
    pdf.cell(0, 8, f"Study Hours per Day: {study_hours}", ln=True)
    pdf.cell(0, 8, f"Internal Marks: {internal_marks}", ln=True)
    pdf.cell(0, 8, f"Previous GPA: {previous_gpa}", ln=True)
    pdf.cell(0, 8, f"Assignments Completed: {assignments}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, f"Final Prediction: {status}", ln=True)

    file_path = "Student_Report.pdf"
    pdf.output(file_path)

    return file_path
