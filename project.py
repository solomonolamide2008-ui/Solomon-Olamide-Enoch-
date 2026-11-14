import random

from numpy.ma.extras import average

from test import student_list

student_id = random.randint(1, 100)

def Student_search():
    if student_id <1 or student_id > 100:
        raise Exception("Student ID must be between 1 and 100")
    else:
        return student_id

def student_course_result():
    student_list = []
    student_name = input("Enter Student Name : ")
    while True:
        if student_name == "":
            break
        student_list.append(student_name)
        for student_name in student_list:
            return student_name
        return student_list
    # student_id = Student_search()
    student_course_result = {}

    student_course = input("Enter your course and type when your 'done'  ")

    while True:
        student_course = input("Enter Student course(or type 'done' to stop): ")
        if student_course == 'done':
            break
        student_course +=1
        print(student_course.index(student_course) + 1)
        student_course_result[student_course] = student_course
        student_result = int(input(f'Enter score for {student_course}:'))
        student_course_result[student_course] = student_result
        print('\nStudent Courses&Result:',student_course_result)
    if student_course_result:
        student_result_addition = sum(student_course_result.values())
        student_average = int(student_result_addition / len(student_course_result.keys()))
        student_course_result[student_average] = student_average
        grade = student_course_result[student_average]
        if student_average >= 70:
            # print(grade == 'A')
        elif student_average >= 60 & student_average < 70:
            # print(grade=='B')
        elif student_average >= 50 & student_average < 60:
            # print(grade=='C')
        elif student_average >= 40 & student_average < 50:
            # print(grade=='D')
        else:
            # print(grade =='F')


        # student_course_result = print(f'the following students: {student_list} '
        #                               f'| average score: {average}| grade: {grade}')

        # return student_course_result

def student_report(result_dicty):
    courses = result_dicty.keys()
    print('courses&Result:',courses)
    if 'average' in result_dicty:
        average = (result_dicty['average'].sort_values(by=['score'], ascending=False)
                   .reset_index(drop=True))
        lowest_score = average.iloc[0]['score']
        result_dicty['average']= average
        result_dicty['lowest_score'] = lowest_score

result_dicty = student_course_result()
student_report(result_dicty)













