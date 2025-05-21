correct_username = "ayush100"
correct_password = 123
attempts = 0
max_attempts = 3
while attempts < max_attempts:
     username = input("enter your username:")
     password = int(input("enter your password:"))
     if password == correct_password and username == correct_username:
        print("Welcome")
        break
     else:
         print("Wrong password or username, try again")
         attempts += 1
if attempts == max_attempts:
   print("Access denied, too many wrong attempts")
