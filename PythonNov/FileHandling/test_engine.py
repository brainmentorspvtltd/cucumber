options = [["james","tim berners lee","guido van","ryan dhal"],
           ["break","continue","pass","skip"],
           ["return","yield","import","is"]]

answers = [2, 2, 1]

file = open('questions.txt')
data = file.readlines()
file.close()

for i in range(len(data)):
    print(data[i])
    for j in range(len(options[0])):
        print(options[i][j])
    ans = input("Enter your ans : ")
    if ans == answers[i - 1]:
        print("Correct Ans")
    else:
        print("Wrong Ans")
