correct_city = "Tokyo"
attempt = 0
max_attempt = 5
input_city = ""

while True:
     capital = input("What is your capital city of Japan?\n")
     if (capital == "tokyo"):
      print("you are correct")
      break
     else:
      attempt += 1
      print(f"Incorrect city. Number of attempt {attempt}/{max_attempt}")
     if  attempt >= max_attempt:
      print("Too many attempts. Your answer is wrong")
      break
   
    