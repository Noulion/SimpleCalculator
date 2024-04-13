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
            try:
              repeat = int(input("1 = Yes, 2 - No \nRepeat the program?: "))
              if repeat == 1:
               rep()
              if repeat == 2:
               break
              if not repeat == 1 or 2:
                  print("INVALID! Please type 1 or 2.")
            except ValueError:
                print("INVALID! Please type 1 or 2.")
            
repeat()