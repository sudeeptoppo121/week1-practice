name = input("Enter Customer Name: ")

marks = []
for i in range(1,6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / 5
highest_mark = max(marks)
lowest_mark = min(marks)

#pass and fail subjects
pass_subjects = [mark for mark in marks if mark >= 40]
fail_subjects = [mark for mark in marks if mark < 40]

if average_marks >= 90:
    grade = 'A'
elif average_marks >= 75:
    grade = 'B'
elif average_marks >= 60:
    grade = 'C'
elif average_marks >= 40:
    grade = 'D'
else:
    grade = 'F'

above_avg_marks = [mark for mark in marks if mark > average_marks]

print(f"Customer Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Number of Pass Subjects: {len(pass_subjects)}")
print(f"Number of Fail Subjects: {len(fail_subjects)}")
print(f"Number of Subjects Above Average: {len(above_avg_marks)}")