courses = {"Python": 25, "Java": 18, "SQL": 30, "Web": 15}

#1 display all courses and their enrollments count

print("--- All Courses and Enrollments ---")
for course, enrollment in courses.items():
    print(f"{course}: {enrollment}")

# 2 search for a specific course 
user_course = input("Enter the course name to search for: ")

if user_course in courses:
    print(f"{user_course} has {courses[user_course]} enrollments.")
else:
    print("Course not found.")

#3 calculate statistics
total_enrollments = sum(courses.values())
highest_course = max(courses, key=courses.get)

#4 create a set of courses with more than 20 student
more_than_20 = {course for course, count in courses.items() if count > 20}

#display  calculation
print("\n--- Course summray ---")
print(f"Total Enrollments: {total_enrollments}")
print(f"Highest Course: {highest_course} with {courses[highest_course]} enrollments")
print(f"Courses with More than 20 Enrollments: {more_than_20}")
