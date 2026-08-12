def match_skills(student_skills, required_skills):
    matched_skills = student_skills & required_skills  # Intersection
    missing_skills = required_skills - student_skills  # Difference
    extra_skills = student_skills - required_skills  # Difference

    if len(required_skills) > 0:
        match_percentage = (len(matched_skills) / len(required_skills)) * 100
    else:
        match_percentage = 0.0

    return matched_skills, missing_skills, extra_skills, match_percentage


# Read inputs and convert directly to sets
student_skills = set(input("Enter Student Skills: ").split())
required_skills = set(input("Enter Required Job Skills: ").split())

# Call the function
matched, missing, extra, match_percentage = match_skills(
    student_skills, required_skills
)

# Determine eligibility status
if match_percentage >= 70:
    status = "Eligible"
else:
    status = "Needs More Skills"

# Display results
print("\n--- Skill Matching Results ---")
print(f"Student Skills: {student_skills}")
print(f"Required Skills: {required_skills}")
print(f"Matched Skills: {matched}")
print(f"Missing Skills: {missing}")
print(f"Extra Skills: {extra}")
print(f"Match Percentage: {match_percentage:.2f}%")
print(f"Status: {status}")