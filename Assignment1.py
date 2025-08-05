
lib_records={"Parth":3,
         "Sarthak":2,
         "Arnav":6,
         "Shreya":0,
         "Vini":3,
         "Sahil":10,
         "Vidisha":0
         }

def compute_average(records):
    total=sum(records.values())
    length=len(records)
    average=total/length
    print("Average= ",average,"\n")

def max_min(records): 
    non_zero=[]
    for val in records.values():
        if val>0:
            non_zero.append(val)
    maxim=max(non_zero)
    minim=min(non_zero)
    print("Maximum=",maxim," Minimum=",minim,"\n")

def count_zero_borrower(records):
    x=list(records.values()).count(0)
    print(x," People have borrowed zero books\n")

def most_frequent(records):
    from collections import Counter
    non_zero_vals=[val for val in records.values() if val>0]
    freq=Counter(non_zero_vals)  
    common=freq.most_common(1)[0][0]
    print("Mostly People buy ",common," books")



def menu():
    print("1.Average")
    print("2.Maximum and Minimum")
    print("3.Zero borrowed")
    print("4.Most Common")
    choice=int(input("Enter choice (1,2,3,4) for the operation to perform: "))
    print()
    if choice==1:
        compute_average(lib_records)
    elif choice==2:
        max_min(lib_records)
    elif choice==3:
        count_zero_borrower(lib_records) 
    elif choice==4:
        most_frequent(lib_records)     
    else:
        print("Invalid Input")
        
while True:
    menu()   
    exit=input("Do you want tp exit program (yes/no): ").lower()
    if exit=="yes":
        break              






