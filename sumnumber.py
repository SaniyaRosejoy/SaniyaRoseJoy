total = 0 
while True:
    try:
        number = int(input("Enter a number  (enter 0 to exit)\n"))
        if number == 0:
            break 
        else:
            total += number
    except ValueError:
        print("Invalid.please enter only numbers")
print(f"The total is : {total}")