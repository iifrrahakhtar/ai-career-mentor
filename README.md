Project Title & Overview: AI Career Mentor — An intelligent web application built with Python, Streamlit, and the Google Gemini API designed to guide students and professionals through resume reviews, custom skill roadmaps, and mock technical interviews.

Key Features:

Instant Resume Feedback: Analyzes project summaries and skill bullet points to provide actionable improvement tips.

Custom Skill Roadmap: Generates tailored learning steps based on your current background and career goals.

AI Mock Technical Interview: Simulates a technical interview session with targeted questions and feedback.

Tech Stack:

Python

Streamlit (for the interactive web UI)

Google GenAI SDK (google-genai with Gemini models)

Setup & Installation Instructions:

Clone or download this repository.

Install the required dependencies by running:

Bash
pip install -r requirements.txt
Create a .env file in the root directory and add your Google Gemini API key:

Plaintext
GEMINI_API_KEY=your_actual_api_key_here
Run the application locally using Streamlit:

Bash
streamlit run main.py
Security & Environment Variables: This repository uses a .env.example template file. Real API credentials are kept strictly in a local .env file and excluded via .gitignore to protect sensitive data.
