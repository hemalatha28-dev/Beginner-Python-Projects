try:
    num1=int(input("Enter First number: "))
    num2=int(input("Enter Second number: "))

    print("Choose Calculations to Perform: \n",
        "1. Add\n",
        "2. Subtract\n",
        "3. Multiply\n",
        "4. Divide\n")
    cal = input().strip().lower()

    if cal == "add":
        ans = num1 + num2
    elif cal == "subtract":
        ans= num1 - num2
    elif cal == "mutliply":
        ans = num1 * num2
    elif cal == "divide":
        if num2 == 0:
            print("Error! Can't Divide By Zero")
            ans = None
        else:
            ans = num1 / num2
    else:
        print("Invalid Operation!")
        ans = None
    if ans is not None:
        print(f'The Answer is: {ans}')
except ValueError:
    print("Invalid Input! Please Enter Valid Number.")
