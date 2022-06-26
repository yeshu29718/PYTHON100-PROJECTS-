#Question
#Enter a two digit number and print the sum of the digits of the number.


#Answer 1.
# 🚨 Don't change the code below 👇
import re


two_digit_number = int(input("Type a two digit number: "))
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
new_td_num = str(two_digit_number)
if(len(new_td_num) == 2):
    print(int(new_td_num[0]) + int(new_td_num[1]))


#Answer 2.
# 🚨 Don't change the code below 👇
two_digit_number = (input("Type a two digit number: "))
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first = int(two_digit_number[0])
second = int(two_digit_number[1])
result = (first + second)
print(result)





