def profile(student_name, student_age, student_email, student_grade):
    profile_data = {
        'name': student_name,
        'age': student_age,
        'email': student_email,
        'grade': student_grade
    }
    return profile_data
print("Welcome to our admission form. Please enter your details to check eligibility.")
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
grade = input("Enter your grade: ")

if grade == 'A':
    print(f"Congratulations {name}, you have been admitted to our school.")
    print(profile(name, age, email, grade))
elif grade == 'B':
    print(f"Congratulations {name}, you have been admitted to our school.")
    print(profile(name, age, email, grade))   
elif grade == 'C':
    print(f"Congratulations {name}, you have been admitted to our school.")
    print(profile(name, age, email, grade))
else:
    print(f"Sorry {name}, you are not eligible for admission")  

