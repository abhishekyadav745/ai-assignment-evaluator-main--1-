def calculate_marks(similarity):
    if similarity >= 0.8:
        return 10
    elif similarity >= 0.5:
        return 5
    else:
        return 0
