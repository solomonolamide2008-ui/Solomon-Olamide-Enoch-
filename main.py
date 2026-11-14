from student import Student
from storage import load, save
from results import REQUIED_SUBJECTS, calculate_student_results
from report import generate_summary,display_class_statistics,save_summary

def find_student_by_id(students,student_id):
    for s in students:
        if s.student_id.strip() == student_id.strip().upper():
            return s
    return None
def main():
    students = load()
    while True:
        print('\n'+'='*45)
        print('Welcome to the student report generator')
        print('='*45)
        print('1. Add a new student')
        print('2. View all students')
        print('3. Search for a student(by ID or by name)')
        print('4. Update a student details')
        print('5. Delete  student Record')
        print('6. Record/update subject scores')
        print('7. Display individual reports')
        print('8. View Summary & Class Statistics')
        print('9. Export Text Report')
        print('10. Save and Exit')

        choice = input('Enter your choice(1-10): ').strip()
        if choice == '1':
            sid = input('Enter student ID: ').strip()
            if find_student_by_id(students, sid):
                print('Error: Student ID already exists')
                continue
            name = input('Enter student name: ').strip()
            s_class = input('Enter student class: ').strip()
            gender = input('Enter student gender: ').strip()
            date_of_birth = input('Enter student date of birth(YYY-MMM-DDD): ').strip()

            new_student = Student(sid,name,gender,date_of_birth,s_class)
            students.append(new_student)
            print(f'Student{name} was added ')

        elif choice == '2':
            if not students:
                print('Error: Student reports not found')
            else:
                print('\n'+'-'*60)
                for s in students:
                    print(f'Student{s.student_id} |Name:{s.full_name}|Class:{s.student_class}'
                          f' |Gender:{s.student_gender}|Date of birth:{s.student_date_of_birth}|')
                print('-'*60)
        elif choice == '3':
            query = input('Enter student ID: ').strip().lower()
            matches =[s for s in students if query in s.student_id.strip().lower()or
                      query in s.full_name.strip().lower()]
            if matches :
                for s in matches:
                        print(f'Found:ID:{s.student_id}, name :{s.full_name},Class :{s.student_class} ')
            else:
                print('Error: Student ID not found')
        elif choice == '4':
            sid = input('Enter student ID to update: ').strip()
            student = find_student_by_id(students,sid)
            if student:
                student.full_name = input(f'New Name({student.full_name}):')or student.student_name
                student.gender = input(f'New Gender({student.gender}):')or student.student_gender
                print('Student updated')
            else:
                print('Error: Student not found')

        elif choice == '5':
            sid = input('Enter student ID to delete: ').strip()
            student = find_student_by_id(students,sid)
            if student:
                students.remove(student)
                print(f'Student{student.student_id} was removed ')
            else:
                print('Error: Student not found')

        elif choice == '6':
            sid = input('Enter student ID to add/update scores: ').strip()
            student = find_student_by_id(students, sid)
            if student:
                print(f'\nEnter scores for 5 courses:({','.join(REQUIED_SUBJECTS)})')
                for subject in REQUIED_SUBJECTS:
                    while True:
                        try:
                            value = float(input(f'Score for {subject}(0-100): '))
                            if value < 0 or value > 100:
                                student.scores[subject] = value
                                break
                            print('Score must be between 0 and 100')
                        except ValueError:
                            print('Invalid input')
                print('Scores updated')
            else:
                print('Error: Student not found')
        elif choice == '7':
            sid = input('Enter student ID: ').strip()
            student = find_student_by_id(students, sid)
            if student:
                total, avg, grade = calculate_student_results(student.scores)
                print('\n'+'='*40)
                print(f'REPORT CARD: {student.full_name} ({student.student_id})')
                print('='*40)
                print(f'Class:{student.student_class}|Gender:{student.student_gender}')
                print('-'*40)
                print(f'Total:{total}')
                print(f'Average:{avg}')
                print(f' Grade:{grade}')
            else:
                print('Error: Student not found')
        elif choice == '8':
            sort_choice = input('Sort records by(1)Average score or (2)Name?'
                                '[Default 1]: ').strip()
            by = 'name' if sort_choice == '2' else 'average'
            records= generate_summary(students,sort_by=by)
            print('\n'+'='*65)
            print(f'{'ID':<10}{'Name':<20}{'Class':<10}{'Total':<8}{'Avg':<8}{'Grade':<5}')
            print('='*65)
            for r in records:
                s= r['student']
                print(f'{s.student_id:<10}{s.full_name:<20} {s.student_class:<10}{r['total']:<8}'
                      f'{r['average']:<8} {r['grade']:<5}')
            display_class_statistics(students)
        elif choice == '9':
            save_summary(students)
        elif choice == '10':
            save(students)
            print('Existing application. Goodbye!')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()




