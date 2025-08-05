print("Emplyee ID Search System \n")

def linear_search(key):
    found=False
    for i in range(len(list)):
        if key==list[i]:
            print(f"Employee ID found at '{i}' index")
            found=True
    if found==False:
        print("Employee ID not found")  

def binary_search(key):
    beg=0
    end=len(list)-1
    found=False
    while beg<=end:

        mid=(beg+end)//2

        if list[mid]==key:
            print(f"Employee ID Found at '{mid}' index")
            found=True
            break
        elif key>list[mid]:
            beg=mid+1
        else:
            end=mid-1
    if found==False:
        print("Employee ID not in the list")            

list=[]
n=int(input("How many Employee Ids do you want to add: "))
for i in range(n):
    x=int(input("Enter Employee ID: "))
    list.append(x)
list.sort()    
target=int(input("Enter Employee ID to find: "))    
while True:
    print("\n Searching Algorithms: ")
    print("1: Linear Search")
    print("2: Binary Search")
    print("3: Exit")
    choice=int(input("Enter your choice (1,2 or 3): "))

    if choice==1:
        linear_search(target)
    elif choice==2:
        binary_search(target)
    elif choice==3:
        print("Thank you")
        break
    else:
        print("Invalid Input")        
