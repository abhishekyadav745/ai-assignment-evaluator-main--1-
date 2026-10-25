def generate_feedback(marks, similarity):
    if float(similarity) >= 0.8:
        return (
            "Excellent answer.\n"
            "The response is correct and accurate.\n"
            "Concept is clearly understood.\n"
            "Keep up the good work."
        )
    elif float(similarity) >= 0.5:
        return (
            "Partially correct answer.\n"
            "The response has some relevance.\n"
            "However, key facts are incorrect.\n"
            "Please revise the concept."
        )
    else:
        return (
            "Incorrect answer.\n"
            "The response does not match the reference.\n"
            "Core concept is misunderstood.\n"
            "Significant improvement is required."
        )
