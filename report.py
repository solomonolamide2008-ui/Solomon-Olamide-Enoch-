import json

from numpy.ma.extras import average

from results import calculate_student_results
def generate_summary(students, sort_by = 'average'):
    records =[]
    for s in students:
        total, avg, grade = calculate_student_results(s.student_scores)
        records.append({
            'student_id': s.id,
            'student_name': s.student_name,
            'grade': grade,
            'student_score': avg,
            'total': total,
        })
    if sort_by == 'average':
        records.sort(key=lambda x: x['average'], reverse=True)
    elif sort_by == 'name':
        records.sort(key=lambda x: x['name'].lower(), reverse=True)
    return records
def display_class_statistics(Students):
    average=[calculate_student_results(s.student_scores)[1] for s in Students if s.student_scores ]
    if not average:
        print('No score data available for Students')
        return
    highest=max(average)
    lowest=min(average)
    class_avg = sum(average)/len(average)
    print('Average Student Score:', highest)
    print('Average Student Score:', lowest)
    print('Average Student Score:', class_avg)

def save_summary(students,filename='class_report.txt'):
    records = generate_summary(students)
    try:
        with open(filename, 'w') as f:
            f.write('='*60 +'\n')
            f.write('Student Name\tStudent Score\n')
            f.write('='*60+'\n\n')
            for r in records:
               f.write(f'{r["student_id"]:<12}|{r["student_name"]: <20}'
                       f'{r["total"]: <8}|{r['average']:<8}|{r['grade']:<5}\n')
        print('Summary saved to', filename)
    except FileNotFoundError as e:
        print('Summary not saved to', filename)


