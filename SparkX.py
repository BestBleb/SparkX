def cls() :
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
print("░██████╗██████╗░░█████╗░██████╗░██╗░░██╗██╗░░██╗")
print("██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚██╗██╔╝")
print("╚█████╗░██████╔╝███████║██████╔╝█████═╝░░╚███╔╝░")
print("░╚═══██╗██╔═══╝░██╔══██║██╔══██╗██╔═██╗░░██╔██╗░")
print("██████╔╝██║░░░░░██║░░██║██║░░██║██║░╚██╗██╔╝╚██╗")
print("╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝")
print(" Version 0.01  By William Page (BestBleb) !! Only for use in calculator alowed questions !!")
print("    !! Please do not abuse this software !!")
running = int(1)
while running == int(1) :
    cls()
    bc = input("Please enter your bookwork code:")
    cls()
    print("███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░░██████╗")
    print("████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗██╔════╝")
    print("██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝╚█████╗░")
    print("██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗░╚═══██╗")
    print("██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║██████╔╝")
    print("╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░")
    print("Enter the numbers in this question, This is like 1 and 2 in 1 + 2")
    num1 = int(input("Enter the first number"))
    num2 = int(input("Second number (The % if doing that)"))
    num3 = int(input("Third number (if none, just put a 0 (But if dividing or multiplying put 1)"))
    cls()
    print("░██████╗███████╗██╗░░░░░███████╗░█████╗░████████╗")
    print("██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗╚══██╔══╝")
    print("╚█████╗░█████╗░░██║░░░░░█████╗░░██║░░╚═╝░░░██║░░░")
    print("░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗░░░██║░░░")
    print("██████╔╝███████╗███████╗███████╗╚█████╔╝░░░██║░░░")
    print("╚═════╝░╚══════╝╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░")
    print("1) Multiply")
    print("2) Divide")
    print("3) Subtract")
    print("4) Add")
    print("5) Percentage")
    print("--- UNUSED SPACE ---")
    print("Type anything else to exit")
    sel = input("Select one")
    cls()
    print("░██╗░░░░░░░██╗██████╗░██╗████████╗███████╗  ████████╗██╗░░██╗██╗░██████╗")
    print("░██║░░██╗░░██║██╔══██╗██║╚══██╔══╝██╔════╝  ╚══██╔══╝██║░░██║██║██╔════╝")
    print("░╚██╗████╗██╔╝██████╔╝██║░░░██║░░░█████╗░░  ░░░██║░░░███████║██║╚█████╗░")
    print("░░████╔═████║░██╔══██╗██║░░░██║░░░██╔══╝░░  ░░░██║░░░██╔══██║██║░╚═══██╗")
    print("░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░███████╗  ░░░██║░░░██║░░██║██║██████╔╝")
    print("░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░")
    if sel == str(1) :
        ants = int(num1 * num2)
        ans = int(ants * num3)
        print("In you book write this:")
        print(bc, ans)
        input("Press ENTER to restart")
    elif sel == str(2) :
        ants = int(num1 / num2)
        ans = int(ants / num3)
        print("In you book write this:")
        print(bc, ans)
        input("Press ENTER to restart")
    elif sel == str(3) :
        ants = int(num1 - num2)
        ans = int(ants - num3)
        print("In you book write this:")
        print(bc, ans)
        input("Press ENTER to restart")
    elif sel == str(4) :
        ants = int(num1 + num2)
        ans = int(ants + num3)
        print("In you book write this:")
        print(bc, ans)
        input("Press ENTER to restart")
    elif sel == str(5) :
        ans = int((num1 * num2) / 100)
        print("In you book write this:")
        print(bc, ans)
        input("Press enter to continue")
    else :
        exit()
