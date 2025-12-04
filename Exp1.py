import numpy as np

student_scores = np.array([
    [85, 78, 90, 88],
    [76, 82, 89, 91],
    [90, 85, 88, 84],
    [70, 75, 80, 79]
])

average_scores = np.mean(student_scores, axis=0)
subjects = ["Math", "Science", "English", "History"]

highest_subject = subjects[np.argmax(average_scores)]

print("Average Scores:", average_scores)
print("Highest Average Subject:", highest_subject)
