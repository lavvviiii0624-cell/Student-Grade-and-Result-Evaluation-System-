print ("=" * 60) 
print("       SMART STUDENT PERFORMANCE & RESULT SYSTEM") 
print("=" * 60) 
 
# 1. STUDENT DETAILS 
 
name = input("\nEnter Student Name: ") 
student_id = input("Enter Student ID: ") 
department = input("Enter Department: ") 
semester = input("Enter Semester: ") 
 
# 2. SUBJECTS 
 
subjects = [ 
    "Python", 
    "Mathematics", 
    "Physics", 
    "English", 
    "Electronics" 
] 
 
marks = {} 
 
# 3. MARKS INPUT AND VALIDATION 
 
print("\n" + "=" * 60) 
print("              ENTER SUBJECT MARKS") 
print("=" * 60) 
 
for subject in subjects: 
 
    while True: 
        try: 
            mark = float(input(f"Enter marks for {subject} (0-100): ")) 
 
            if 0 <= mark <= 100: 
                marks[subject] = mark 
                break 
            else: 
                print("Invalid marks! Enter a value between 0 and 100.") 
 
        except ValueError: 
            print("Invalid input! Please enter a number.") 
 
# 4. TOTAL AND PERCENTAGE 
 
def calculate_total(marks): 
    return sum(marks.values()) 
 
 
def calculate_percentage(total, number_of_subjects): 
    return total / number_of_subjects 
 
 
total = calculate_total(marks) 
percentage = calculate_percentage(total, len(subjects)) 
 
# 5. GRADE CALCULATION 
 
def calculate_grade(percentage): 
 
    if percentage >= 90: 
        return "A+" 
    elif percentage >= 80: 
        return "A" 
    elif percentage >= 70: 
        return "B" 
    elif percentage >= 60: 
        return "C" 
    elif percentage >= 50: 
        return "D" 
    else: 
        return "F" 
 
 
grade = calculate_grade(percentage) 
 
# 6. PASS / FAIL EVALUATION 
 
def evaluate_result(marks, percentage): 
 
    for mark in marks.values(): 
        if mark < 40: 
            return "FAIL" 
 
    if percentage < 50: 
        return "FAIL" 
 
    return "PASS" 
 
 
result = evaluate_result(marks, percentage) 
 
# 7. STRONGEST AND WEAKEST SUBJECT 
 
def find_strongest_subject(marks): 
    return max(marks, key=marks.get) 
 
 
def find_weakest_subject(marks): 
    return min(marks, key=marks.get) 
 
 
strongest_subject = find_strongest_subject(marks) 
weakest_subject = find_weakest_subject(marks) 
 
# 8. PERFORMANCE ANALYSIS 
 
def performance_level(percentage): 
 
    if percentage >= 90: 
        return "Outstanding" 
    elif percentage >= 80: 
        return "Excellent" 
    elif percentage >= 70: 
        return "Very Good" 
    elif percentage >= 60: 
        return "Good" 
    elif percentage >= 50: 
        return "Average" 
    else: 
        return "Needs Improvement" 
 
 
performance = performance_level(percentage) 
 
# 9. PERSONALIZED RECOMMENDATION 
 
def generate_recommendation(marks, percentage): 
 
    weakest = min(marks, key=marks.get) 
 
    if percentage >= 90: 
        return "Excellent performance! Maintain your current study routine." 
 
    elif percentage >= 80: 
        return f"Very good performance! Give extra attention to {weakest}." 
 
    elif percentage >= 70: 
        return f"Good performance! Focus more on {weakest} to improve your grade." 
 
    elif percentage >= 50: 
        return f"You have passed, but you should improve {weakest} and revise regularly." 
 
    else: 
        return f"Your performance needs improvement. Give high priority to {weakest}." 
 
 
recommendation = generate_recommendation(marks, percentage) 
 
# 10. FINAL STUDENT REPORT 
 
print("\n" + "=" * 60) 
print("             SMART STUDENT PERFORMANCE REPORT") 
print("=" * 60) 
 
print("\nSTUDENT INFORMATION") 
print("-" * 40) 
print("Student Name :", name) 
print("Student ID   :", student_id) 
print("Department   :", department) 
print("Semester     :", semester) 
 
print("\nSUBJECT-WISE MARKS") 
print("-" * 40) 
 
for subject, mark in marks.items(): 
    print(f"{subject:15} : {mark:.2f}") 
 
print("\nACADEMIC SUMMARY") 
print("-" * 40) 
print(f"Total Marks       : {total:.2f} / 500") 
print(f"Percentage        : {percentage:.2f}%") 
print(f"Grade             : {grade}") 
print(f"Result            : {result}") 
print(f"Performance Level : {performance}") 
 
print("\nPERFORMANCE ANALYSIS") 
print("-" * 40) 
print(f"Strongest Subject : {strongest_subject}") 
print(f"Weakest Subject   : {weakest_subject}") 
 
print("\nPERSONALIZED RECOMMENDATION") 
print("-" * 40) 
print(recommendation) 
 
print("\n" + "=" * 60) 
print("              END OF REPORT") 
print("=" * 60) 
 
