# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you
User_input1 = raw_input("Enter your name")
User_input2 = raw_input("Enter your age:")
User_input3 = raw_input("Have you had your birthday yet? Y/N:")
if User_input3 == "Y":
    My_str4= 101 - int(User_input2)
else:
    My_str4 = 100 - int(User_input2)
N = 2017
for year in range(100- int(User_input2)):
    N = N + 1
My_str = "will be 100 years old in"
My_str2= "years! Which is the year"
My_str3= "so you better start living your life."
print User_input1, My_str, 100- int(User_input2), My_str2, N, My_str3

