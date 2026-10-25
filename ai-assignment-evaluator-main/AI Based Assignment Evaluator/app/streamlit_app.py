import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from evaluation.similarity_checker import compute_similarity
from evaluation.grading_engine import calculate_marks
from generation.feedback_generator import generate_feedback
from pypdf import PdfReader  


def extract_text_from_pdf(file):
    if file is not None:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    return ""

st.title("AI Assignment Evaluation System")


student_pdf = st.file_uploader("Upload Student Answer PDF", type=["pdf"])
reference_pdf = st.file_uploader("Upload Reference Answer PDF", type=["pdf"])

if st.button("Evaluate"):
    if student_pdf and reference_pdf:
        
        student_answer = extract_text_from_pdf(student_pdf)
        reference_answer = extract_text_from_pdf(reference_pdf)
        
        
        similarity = compute_similarity(student_answer, reference_answer)
        marks = calculate_marks(similarity)
        feedback = generate_feedback(marks, similarity)
        
    
        st.write(f"**Similarity Score:** {float(similarity):.2f}")
        st.write(f"**Marks:** {marks}/10")
        st.subheader("AI Feedback")
        st.text(feedback)
    else:
        st.warning("कृपया दोनों PDF फाइलें अपलोड करें।")
