


#taking the input
n=int(input("enetr the number of students in the class: " ))
list=[]
print("If student is absent enter -1")
for i in range(n):
    
    marks=int(input("Enter the  marks of students:"))
    list.append(marks)
print(list)


#The average score of the class
def avg(list):
    total_marks = 0
    avg_marks = 0
    count = 0
    for i in range(n):
        if list[i] != -1:
            total_marks += list[i]
            count += 1
    average_marks = total_marks / count
    return average_marks
print("Average marks :",avg(list))


#higest score of the class
def highest_score(list):
    highest = list[0]
    for i in range(n):
        if list[i] > highest:
            highest = list[i]
    return highest

print("Highest score of the class: ",highest_score(list))


#lowest score of thee class
def lowest_score(list):
    lowest = list[0]
    for i in range(n):
        if list[i] != -1:
            if list[i] < lowest:
                lowest = list[i]
    return lowest
print("Lowest score of the class : ",lowest_score(list))


#student who were absent for the test
def absent_student(list):
    count = 0
    for i in range(n):
        if list[i] == -1:
            count += 1
    return count
print("Number of absent students = ",absent_student(list))


#marks with highest frequency
def freq(list):
    frequency = []
    for i in range(0, 101):
        frequency.append(0)
    for i in range(0, n):
        element = list[i]
        if element != -1:
            frequency[element] += 1
    mode = []
    mark = 0
    for i in range(0, 101):
        if frequency[i] > mark:
            mark = frequency[i]
    for i in range(0, 101):
        if frequency[i] == mark:
            mode.append(i)
    return mode
print("Marks with Highest Frequency: ", freq(list))


#percentage of student passed and failed 
def passed(list):
    pas=0
    fail=0
    abs=0
    for i in range(0,n):
        if list[i]>=40:
            pas+=1
        elif(list[i]!=-1):
            fail+=1
        else:
            abs+=1
    print("Percentage of students passed who appeared: ",(pas/(n-abs))*100)
    print("Percentage of students failed who appeared: ",(fail/(n-abs))*100)
passed(list)


#student with top three highest score
def top_three_student(list):

    for i in range(0,n):
        for j in range(0, n):
            if list[j] > list[i]:
                list[i], list[j] = list[j], list[i]

    if(n<3):
        print("There are less than 3 students")
    else:
        print("Top 3 Highest Scores: ",list[n-1],list[n-2],list[n-3])
top_three_student(list)



