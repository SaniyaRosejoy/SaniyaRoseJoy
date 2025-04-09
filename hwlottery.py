user_numbers = set()
while len(user_numbers) < 7:
    try:
        num = int(input(f"Enter number {len(user_numbers)+1}: "))
        if num in user_numbers:
            print("Error: Number already entered. Try again.")
        else:
            user_numbers.add(num)
    except ValueError:
        print("Invalid input. Please enter a number.")
print("Your numbers are:", user_numbers)
winning_numbers = {10, 25, 32, 41, 43, 45, 50}
correct_numbers = user_numbers & winning_numbers
print(f"Correct numbers: {correct_numbers}")
if len(correct_numbers) == 3:
    print("You win $4!")
elif len(correct_numbers) == 4:
    print("You win $15!")
elif len(correct_numbers) == 5:
    print("You win $200!")
elif len(correct_numbers) == 6:
    print("You win $30,000!")
elif len(correct_numbers) == 7:
    print("You win $5,000,000!")
else:
    print("No prize. Better luck next time!")
