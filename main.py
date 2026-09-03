import streamlit as st
from utils import get_ai_response

# Page configuration
st.set_page_config(
    page_title="AI Career Mentor", page_icon="🧭", layout="wide"
)

st.title("🧭 AI Career Mentor")
st.markdown(
    "Your personalized guide for skill roadmaps, resume reviews, and mock"
    " interviews powered by AI."
)

# Sidebar navigation
menu = st.sidebar.selectbox(
    "Choose a Feature",
    [
        "Home",
        "Learning Roadmap Generator",
        "Resume Reviewer",
        "Mock Interviewer",
    ],
)

if menu == "Home":
    st.subheader("Welcome to your AI-powered career growth companion!")
    st.write(
        "Select a tool from the sidebar to start shaping your professional"
        " journey."
    )
    st.info(
        "Tip: Ensure you have added your `GEMINI_API_KEY` to the `.env` file."
    )

elif menu == "Learning Roadmap Generator":
    st.subheader("Custom Skill Roadmap")
    current_skill = st.text_input(
        "What is your current background/skill level?",
        placeholder="e.g., Beginner in Python",
    )
    target_goal = st.text_input(
        "What is your career goal?", placeholder="e.g., Junior Machine Learning Engineer"
    )

    if st.button("Generate Roadmap"):
        if current_skill and target_goal:
            with st.spinner("Crafting your custom roadmap with AI..."):
                prompt = (
                    f"Create a detailed, step-by-step learning roadmap for someone"
                    f" whose current background is '{current_skill}' and whose"
                    f" goal is to become a '{target_goal}'. Break it down by"
                    f" months and include recommended topics/projects."
                )
                roadmap_result = get_ai_response(prompt)
                st.success("Roadmap generated successfully!")
                st.markdown(roadmap_result)
        else:
            st.warning("Please fill in both fields.")

elif menu == "Resume Reviewer":
    st.subheader("Instant Resume Feedback")
    resume_text = st.text_area(
        "Paste your resume summary, project description, or bullet points here:"
    )

    if st.button("Review Resume"):
        if resume_text:
            with st.spinner("Analyzing resume content..."):
                prompt = (
                    f"Act as an expert technical recruiter. Review the"
                    f" following resume text and provide constructive"
                    f" feedback, highlighting strengths and specific areas for"
                    f" improvement:\n\n{resume_text}"
                )
                feedback = get_ai_response(prompt)
                st.markdown(feedback)
        else:
            st.warning("Please paste your resume text first.")

elif menu == "Mock Interviewer":
    st.subheader("AI Mock Technical Interview")
    job_role = st.selectbox(
        "Select Target Role",
        ["Python Developer", "AI/ML Engineer", "Data Analyst"],
    )

    user_answer = st.text_area(
        f"Answer this mock interview question for a {job_role}:\n'Can you"
        " explain a challenging technical problem you solved or a core"
        " concept in your field?'"
    )

    if st.button("Evaluate Answer"):
        if user_answer:
            with st.spinner("Evaluating your response..."):
                prompt = (
                    f"Act as a strict technical interviewer for a {job_role}"
                    f" position. Evaluate the candidate's answer below, give a"
                    f" score out of 10, and provide constructive suggestions"
                    f" for improvement:\n\nCandidate Answer: {user_answer}"
                )
                evaluation = get_ai_response(prompt)
                st.markdown(evaluation)
        else:
            st.warning("Please write an answer before submitting.")