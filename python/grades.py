# for lesson
# logic errors

grade = int(input("Please enter the test result: "))

if grade < 0:
    print("Fail")
if grade > 50:
    print("C Grade")
if grade < 75:
    print("B Grade")
if grade > 100:
    print("A Grade")
