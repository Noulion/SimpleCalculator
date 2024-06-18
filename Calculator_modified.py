#Calculator By: Hanprince 
#forked/modified by @Noullion June-18-2024
print("Simple Calculator By: Nano")
print(" | Addition = + \n | Subtraction = - \n | Multiplication = x \n | Division = ÷ \n")

def func():
    Operation = input("Operation: ") 
    if Operation == "+":
        Add = float(In1) + float(In2)
        print(Add)
    elif Operation == "-":
        Sub = float(In1) - float(In2)
        print(Sub)
    elif Operation == "x":
        Mult = float(In1) * float (In2)
        print(Mult)
    elif Operation == "÷":
        try:
            Div = float(In1) / float(In2)
            print(Div)
        except ZeroDivisionError:
            print("INVALID! You cannot divide with zero.")
    else:
            print("INVALID! Enter a mathematical operation.")
            
while True:
    try:
        print()
        In1 = input("1st Digit: ")
        In2 = input("2nd Digit: ")
        oper = func()
    
    except ValueError:
        print("string cant be calculates\n")
