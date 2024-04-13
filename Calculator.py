#Calculator By: Hanprince
print("Simple Calculator By: Nano")
print(" | Addition = + \n | Subtraction = - \n | Multiplication = x \n | Division = ÷ \n")

def rep():
 while True:
    try:
     In1 = int(input("1st Digit: "))
     break
    except ValueError:
        print("INVALID! Enter a valid digit.")
        
 while True:
    try:
        In2 = int(input("2nd Digit: "))
        break
    except ValueError:
        print("INVALID! Enter a valid digit.")
        
 while True:
        Operation = input("Operation: ") 
        if Operation == "+":
            Add = float(In1) + float(In2)
            print(Add)
            break
        elif Operation == "-":
            Sub = float(In1) - float(In2)
            print(Sub)
            break
        elif Operation == "x":
            Mult = float(In1) * float (In2)
            print(Mult)
            break
        elif Operation == "÷":
            try:
                Div = float(In1) / float(In2)
                print(Div)
                break
            except ZeroDivisionError:
                print("INVALID! You cannot divide with zero.")
        else:
            print("INVALID! Enter a mathematical operation.")
rep()
 
def repeat():
        while True:
              repeat = input("Repeat the program? (Y/N): ")
              if repeat == "Y":
               rep()
              if repeat == "N":
               break
            
repeat()
