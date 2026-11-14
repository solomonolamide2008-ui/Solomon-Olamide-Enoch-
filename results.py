from datetime import datetime
REQUIED_SUBJECTS =['Math','English','Science','Physics','Chemistry']

def student_results(average):
    if average >= 70 :
        return "A"
    elif average >= 60 :
        return "B"
    elif average >= 50 :
        return "C"
    elif average >= 40 :
        return "D"
    elif average >= 30 :
        return "F"
def calculate_student_results(student_scores):
    if not student_scores:
        return 0.0, 0.0, 'N/A'
    total = sum(student_scores.values())
    average = total / len(student_scores)
    grade = student_results(average)
    return (total,2), (average,2), grade
