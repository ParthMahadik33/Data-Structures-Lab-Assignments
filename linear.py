#list=[100,101,102,103,104,105,106]
list=[]
n=int(input("How many elements do you want to add: "))
for i in range(n):
    x=int(input("Enter Element: "))
    list.append(x)


key=int(input("Enter element to find: "))

found=False
for i in range(len(list)):
    if key==list[i]:
        print(f"Element found at '{i}' index")
        found=True
if found==False:
    print("Element not found")
        