mathScore = int(input("Enter the Math's Score: "))
engScore = int(input("Enter the English Score: "))
sciScore = int(input("Enter the Science Score: "))

avgScore = (mathScore + engScore + sciScore)/3

print(f"Avg Marks:{avgScore}")

if avgScore >= 80:
    print("Grade: A")
elif avgScore >=70:
    print("Grade : B")
elif avgScore >=50:
    print("Grade : C")
elif avgScore >=40:
    print("Grade : D")
else:
    print("Failed")