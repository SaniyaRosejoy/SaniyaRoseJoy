total = 0 
while True: 
    number = int(input("Enter a number (enter 0 to exit)\n"))
    if number == 0 :
      break
    else:
       total += number
print(f"The total is:{total}")