import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, job_role):

    prompt = f"""
    You are a professional AI Resume Analyzer.

    Analyze this resume for the role:
    {job_role}

    Resume Content:
    {resume_text}

    Give response in EXACT format below:

    ============================
    PROFESSIONAL SUMMARY
    ============================

    Write a short professional summary.

    ============================
    SKILLS FOUND
    ============================

    Mention all technical and soft skills.

    ============================
    SKILL GAP ANALYSIS
    ============================

    Mention important missing skills required for this role.

    ============================
    ATS IMPROVEMENT SUGGESTIONS
    ============================

    Give ATS optimization tips.

    ============================
    STRENGTHS
    ============================

    Mention strengths of candidate.

    ============================
    WEAKNESSES
    ============================

    Mention weaknesses.

    ============================
    INTERVIEW QUESTIONS
    ============================

    Generate 5 technical interview questions.

    ============================
    FINAL RESUME SCORE
    ============================

    Give resume score out of 100.
    """

    response = model.generate_content(prompt)

    return response.text