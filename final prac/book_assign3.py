

#taking the input
n=int(input("Enter the number of books : "))
book=[]
print("Enter the name of book and price:")
for i in range(n):
    l=[]

    name=input("name of the book : ")
    price=int(input("price of the book : "))
    l.append(name)
    l.append(price)
    book.append(l)

print(book)


#delete the duplicate entries

def duplicate(book):
    new_book=[]
    for i in book:
        if i not in new_book:
            new_book.append(i)

    return new_book

print("delete the duplicate copies ", duplicate(book))


#arranging books in ascending order on the basis of cost

def arrange(book):
    
    for i in range(len(book)):
        for j in range(len(book)):
            if book[i][1] < book[j][1]:
                book[i][1], book[j][1] = book[j][1], book[i][1]
                book[i][0],book[j][0]=book[j][0],book[i][0]
    return book
print("arranging books in ascending order on the basis of cost", arrange(book))


#number of books  with cost more than 500

def cost_more(book):
    count = 0
    for i in range(len(book)):
    
        if book[i][1] > 500:
           count += 1
    return count

print("count number of books having cost more than 500 = ",cost_more(book))


#number of books with cost less than 500

def cost_less(book):
    new_list = []
    for i in range(len(book)):

        if book[i][1] < 500:
            new_list.append(book[i])
    return new_list

print("books having price less than 500", cost_less(book))
