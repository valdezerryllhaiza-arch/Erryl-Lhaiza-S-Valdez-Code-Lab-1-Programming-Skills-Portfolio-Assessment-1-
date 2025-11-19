#the function checkes if the number inputed is odd or even
def check_odd_even(number):
    #the if statements checkes if the number given is divisivle by 2
    if number % 2 == 0:
    #if the number is disivisible of 2, it is declared even
        return "Even"
    #else, it is declared odd
    else:
        return "Odd"

#the user is asked to input a number
user_input = int(input("Enter a number:"))

#the function is called and the result is stored in the variable 
result = check_odd_even(user_input)

#f-string is used to display the result
print(f"The number {user_input} is {result}.")