import streamlit as st

st.set_page_config(page_title="GPA Calculator", page_icon="🎓")

st.title("📘 GPA Calculator (Marks-Based)")

# Grade thresholds from your table
def get_grade_info(marks):
    if 85 <= marks <= 100:
        return "A", 4.00
    elif 80 <= marks <= 84:
        return "A-", 3.70
    elif 75 <= marks <= 79:
        return "B", 3.30
    elif 70 <= marks <= 74:
        return "B+", 3.00
    elif 65 <= marks <= 69:
        return "B-", 2.70
    elif 61 <= marks <= 64:
        return "C", 2.30
    elif 58 <= marks <= 60:
        return "C+", 2.00
    elif 55 <= marks <= 57:
        return "C-", 1.70
    elif 50 <= marks <= 54:
        return "D", 1.00
    else:
        return "F", 0.00

# Subjects and their credit hours
subjects = {
    "Multivariate Calculus": 3,
    "Introduction to Data Science (IDS)": 2,
    "Artificial Intelligence (AI)": 2,
    "Data Visualization (DV)": 2,
    "Database (DB)": 3,
    "DB Lab": 1,
    "Analysis of Algorithms (AOA - optional)": 3,
    "Quantitative Techniques (QT)": 0.5
}

st.header("Enter your obtained marks (0–100):")

grades = {}
total_points = 0
total_credits = 0

for subject, credit in subjects.items():
    marks = st.number_input(f"{subject} ({credit} CR)", min_value=0, max_value=100, step=1, key=subject)
    letter_grade, grade_point = get_grade_info(marks)
    grades[subject] = (marks, letter_grade, grade_point)
    total_points += grade_point * credit
    total_credits += credit

if st.button("Calculate GPA"):
    gpa = total_points / total_credits
    st.subheader("📊 Result Summary")
    for subject, (marks, grade, point) in grades.items():
        st.write(f"**{subject}**: {marks} → Grade: `{grade}` | Grade Point: `{point}`")

    st.success(f"🎓 Your GPA is: **{gpa:.2f}**")
