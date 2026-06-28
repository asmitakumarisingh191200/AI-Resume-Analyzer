from django.shortcuts import render
from PyPDF2 import PdfReader

from .gemini_utils import analyze_resume


def home(request):

    result = ""

    if request.method == "POST":

        try:

            pdf_file = request.FILES['resume']

            job_role = request.POST['job_role']

            reader = PdfReader(pdf_file)

            resume_text = ""

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    resume_text += text

            result = analyze_resume(
                resume_text,
                job_role
            )

        except Exception as e:

            result = f"Error: {str(e)}"

    return render(
        request,
        'index.html',
        {'result': result}
    )