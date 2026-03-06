from studentmarks.marks import total_marks, average_marks
from studentmarks.grade import calculate_grade

m1 = int(input("enter marks for subject 1 : "))
m2 = int(input("enter marks for subject 2 : "))
m3 = int(input("enter marks for subject 3 : "))

total = total_marks(m1,m2,m3)
avg = average_marks()(m1, m2, m3)
grade = calculate_grade(avg)

print("Total Marks:", total)
print("Average Marks:", avg)
print("Grade:", grade)