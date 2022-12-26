n=int(input("Total students : "))
student=[]
print("enter roll no of the students: ")
for i in range(n):
    s=input()
    if s not in student:
        student.append(s)
print("students are: ", student)

n_c=int(input("number of students who play cricket : "))
print("enter roll no of the student: ")
cricket=[]
for i in range(n_c):
    c=input()
    if c not in cricket:
        cricket.append(c)

print("students who play cricket")
print(cricket)

n_b=int(input("number of students who play badminton : "))
print("enter roll no ")
badminton=[]
for i in range(n_b):
    b=input()
    if b not in badminton:
        badminton.append(b)
print("students who play badminton :", badminton)


n_f=int(input("number of students who play football :"))
print("enter roll no ")
football=[]
for i in range(n_f):
    f=input()
    if f not in football:
        football.append(f)
print("students who play football :", football)

#1.play both cricket and badminton
def cr_bad(cricket,badminton):
    both_c_b=[]
    for i in cricket:
        if i in badminton:
            both_c_b.append(i)
    return both_c_b
print("Students who play both cricket and badminton are :", cr_bad(cricket, badminton))

#2.students playing either cricket or badminton but not both
def no_intersec(cricket, badminton):
	final = []
	for i in cricket:
		if i not in badminton:
			final.append(i)
	for i in badminton:
		if i not in cricket:
			final.append(i)
	return final
print("students playing either cricket or badminton but not both",no_intersec(cricket, badminton))		

#3.number of students who neither play cricket nor badminton
def neither_c_b(cricket,badminton):
    crik_bad = []
    for i in range(n_c):
        crik_bad.append(cricket[i])
    for i in range(n_b):
        flag = 0
        for j in range(n_c):
            if badminton[i] == crik_bad[j]:
                flag = 1
        if flag == 0:
            crik_bad.append(badminton[i])
    #print("union of cricket badminton")
    #print(crik_bad)
    neither = []
    for i in range(n):
        flag = 0
        for j in range(len(crik_bad)):
            if student[i] == crik_bad[j]:
                flag = 1
        if flag == 0:
            neither.append(student[i])
    return len(neither)
    #print("number of student who play neither cricket nor badminton", len(neither))
    #print(neither)
print("number of student who play neither cricket nor badminton:", neither_c_b(cricket,badminton))

#4.students who play cricket and football but not badminton

def cr_foot_bad(cricket,badminton,football):
    crik_foot = []
    for i in cricket:
        if i in football:
            crik_foot.append(i)
    
    ##print("students who play both cricket and football")
    #print(crik_foot)

    not_bad = []
    for i in range(len(crik_foot)):
        flag = 0
        for j in range(n_b):
            if crik_foot[i] == badminton[j]:
                flag = 1
        if flag == 0:
            not_bad.append(crik_foot[i])
    return len(not_bad),not_bad

    #print("number of students who play both criket and football nor badminton = ", len(not_bad))
    #print(not_bad)
print("number of students who play both criket and football nor badminton : ", cr_foot_bad(cricket, badminton, football))

## students playing at least one game
def at_least_one(crick,bad,foot,std) :
    ans = []
    for i in std :
        if i in crick or i in bad or i in foot :
            ans.append(i)
    return ans

print('students playing at least one game : ',at_least_one(cricket,badminton,football,student))

# students playing all three games games
def all_games(cricket,badminton,football):
    all=[]
    for i in cr_bad(cricket,badminton):
        if i in football:
            all.append(i)
    return all
print('students playing all three games games : ', all_games(cricket,badminton,football))

#number of students not playing any game
print("number of students not playing any game : ", n - len(at_least_one(cricket,badminton,football,student)))








