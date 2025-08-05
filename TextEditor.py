undo_stack=[]
redo_stack=[]
class TextEditor:

    
    def __init__(self,undo,redo):
        self.undo=undo
        self.redo=redo
        

    def make_change(self):
        
        text=input("Enter a string: ")
        self.undo.append(text)
        self.redo.clear()

    def Undo(self):
        
        
        try:
            x=self.undo.pop()
        except IndexError:
            print("Nothing to Undo\n")
            return
        self.redo.append(x)

    def Redo(self):
        try:
            x=self.redo.pop()
        except IndexError:
            print("Nothing to Redo\n")
            return    
        self.undo.append(x)

    def display(self):
        for i in self.undo:
            print(i,end=" ")  

s1=TextEditor(undo_stack,redo_stack)


while True:
    print("\n \n1.Enter Text")
    print("2.Undo")
    print("3.Redo") 
    print("4.Exit")
    
    choice=input("Enter your choice: ")
    print()
    if choice=='1':
        s1.make_change()
        print()
        s1.display()
    elif choice=='2':
        s1.Undo()
        print()
        s1.display()
    elif choice=='3':
        s1.Redo()
        print()
        s1.display()
    elif choice=='4':
        print("Thank You")
        break
    else:
        print("Invalid Input")   