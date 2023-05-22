# Get input from the manager or HR personnel
job_responsibilities = input("Enter the employee's job responsibilities rating (1-5): ")
skills = input("Enter the employee's skills rating (1-5): ")
accomplishments = input("Enter the employee's accomplishments rating (1-5): ")
feedback = input("Enter the employee's feedback rating (1-5): ")

# Calculate the overall performance score
performance_score = (int(job_responsibilities) + int(skills) + int(accomplishments) + int(feedback)) / 4

# Print the employee's performance score
print("The employee's performance score is:", performance_score)

# Provide feedback and recommendations for improvement
if performance_score < 3:
    print("The employee needs improvement in their performance.")
elif performance_score < 4:
    print("The employee is performing adequately but there is room for improvement.")
else:
    print("The employee is performing well and meets or exceeds expectations.")
