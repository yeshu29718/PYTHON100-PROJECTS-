# #question
# Create a program using maths and f-Strings that tells us how many days, weeks, months
# we have left if we live until 90 years old.

# It will take your current age as the input and output a
# message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

#Answer
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = 90*365
days_left = days - int(age)*365
weeks = 90*52
weeks_left = weeks -int(age)*52
months = 12*90
months_left = months - int(age)*12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")



#Answer 2.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")