print("Do you want to calculate? OK, enter the numbers and the equation symbol and i will tell you the answer. ")
print("Ready? Let's Go! ")

First_Number = input("Enter The First Number Please: ")
Equation_Symbol = input("Enter The Equation Symbol please: " )
Second_Number = input("Enter The Second Number Please: ")

if Equation_Symbol == "+" :
    print("The Answer is: ", int(First_Number) + int(Second_Number))

if Equation_Symbol == "-" :
    print("The Answer is: ", int(First_Number) - int(Second_Number))

if Equation_Symbol == "*" :
    print("The Answer is: ", int(First_Number) * int(Second_Number))

if Equation_Symbol == "/" :
    print("The Answer is: ", int(First_Number) / int(Second_Number))

if Equation_Symbol == "^" :
    print("The Answer is: ", int(First_Number) ** int(Second_Number))

if Equation_Symbol == "%" :
    print("The Answer is: ", int(First_Number) % int(Second_Number))

print("Thank You For Using Our Program, Well Done!")