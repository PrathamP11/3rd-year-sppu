# Define a dictionary of evaluation criteria and corresponding weights
evaluation_criteria = {
    "job_responsibilities": 0.4,
    "skills": 0.3,
    "accomplishments": 0.2,
    "feedback": 0.1
}

# Get input from the manager or HR personnel
employee_data = {}
for criterion in evaluation_criteria:
    employee_data[criterion] = input(f"Enter the employee's {criterion.replace('_', ' ')}: ")

# Calculate the overall performance score
performance_score = 0
for criterion, weight in evaluation_criteria.items():
    rating = int(employee_data[criterion])
    performance_score += rating * weight

# Print the employee's performance score
print("The employee's performance score is:", performance_score)

# Provide feedback and recommendations for improvement
if performance_score < 2:
    print("The employee needs improvement in all areas.")
elif performance_score < 3.5:
    print("The employee is performing adequately but there is room for improvement.")
else:
    print("The employee is performing well and meets or exceeds expectations.")
