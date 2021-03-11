###Solution to problem 52 from ben stephenson's "the python workbook".

print("Enter a numerical grade:")
grade = float(input())

if grade < 0:
  grade = 0

grades = {  0:    'F',
            1:    'D',
            1.3:  'D+',
            1.7:  'C-',
            2.0:  'C',
            2.3:  'C+',
            2.7:  'B-',
            3.0:  'B',
            3.3:  'B+',
            3.7:  'A-',
            4.0:  'A'  }

grade_points = [i for i in grades.keys()]
letter_grade = ''

for i in range(len(grade_points)):
  if grade >= 4.0:
    letter_grade = 'A+'
  elif grade >= grade_points[i] and grade < grade_points[i+1]:
    if abs(grade - grade_points[i]) <= abs(grade - grade_points[i + 1]):
      letter_grade = grades.get(grade_points[i])
    else:
      letter_grade = grades.get(grade_points[i + 1])

print(letter_grade)
