#list=[101,102,103,104,105,106,107]
list=[]
list1=[]
n=int(input("How many elements do you want to add: "))
for i in range(n):
    x=int(input("Enter Element: "))
    list.append(x)

#list.sort()
print(list)

list1=list
list.sort()
print(list1)


key=int(input("Enter element to find: "))
beg=0
end=len(list1)-1
found=False
while beg<=end:

    mid=(beg+end)//2

    if list1[mid]==key:
        print(f"Element Found at '{mid}' index")
        found=True
        break
    elif key>list1[mid]:
        beg=mid+1
    else:
        end=mid-1
if found==False:
    print("Element not in the list")            
