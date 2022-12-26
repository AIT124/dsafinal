

m= int(input("ENTER THE NUMBER OF STUDENTS IN COMP-A:- "))
COMP_A=[]
print("Enter the PRN date and month ")
for i in range(m):

    prn= int(input("Enter PRN number:"))
    date= int(input("Enter date of birth:"))
    month= int(input("Enter month of birth:"))
    if (date>31 or month>12) :
            print("Invalid input")
            break
    else:
        list1=[prn,date,month]    
    COMP_A.append(list1)


n= int(input("ENTER THE NUMBER OF STUDENTS IN COMP-B:- "))
COMP_B=[]
print("Enter the PRN date and month")
for i in range(n):

    prn= int(input("Enter PRN number:"))
    date= int(input("Enter date of birth:"))
    month= int(input("Enter month of birth:"))
    if (date>31 or month>12) :
            print("invalid input")
            break
    else:
        list2=[prn,date,month]    
    COMP_B.append(list2)

#sorting of array
def Sort(data): 
    i = len(data)-1 
    while i > 0:
        j = 0
        while j < i:
            if data[j][2] > data[j+1][2]:
                data[j], data[j+1] = data[j+1], data[j]
            if data[j][2]==data[j+1][2]:
                if data[j][1] > data[j+1][1]:
                    data[j], data[j+1] = data[j+1], data[j]
            j+=1
        i-=1
    return(data)

def sorted_list(l1,l2):
    list3=[]
    cnt1=0
    cnt2=0
    while cnt1<len(l1) and cnt2<len(l2):
        if l1[cnt1][2]<l2[cnt2][2]:
            list3.append(l1[cnt1])
            cnt1+=1
        elif l1[cnt1][2]>l2[cnt2][2]:
            list3.append(l2[cnt2])
            cnt2+=1
        else:
            if l1[cnt1][1]<l2[cnt2][1]:
                list3.append(l1[cnt1])
                cnt1+=1
            elif l2[cnt2]<l1[cnt1]:
                list3.append(l2[cnt2])
                cnt2+=1
            else:
                list3.append(l1[cnt1])
                list3.append(l2[cnt2])
                cnt1+=1
                cnt2+=1
    
    while cnt1<len(l1):
        list3.append(l1[cnt1])
        cnt1+=1
    while cnt2<len(l2):
        list3.append(l2[cnt2])
        cnt2+=1
    return(list3)



print("list of COMP-A: " ,Sort(COMP_A))
print("lsit of COMP-B: ",Sort(COMP_B))
print("list of COMP combined:",sorted_list(COMP_A,COMP_B))
