n = int(input("Enter The Value of N"))
list1 =[]

for i in range(1,n+1,2):

    list1.append(i)
    a = len(list1)
    
print("Count of Odd Numbers is",a)