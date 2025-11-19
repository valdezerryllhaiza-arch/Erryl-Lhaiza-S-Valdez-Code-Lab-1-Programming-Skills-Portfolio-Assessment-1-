#The dictionary stores countries and their capitals
Capitals= {
    "France": "Paris",
    "Norway": "Oslo",
    "Sweden": "Stockholm",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Ireland": "Dublin",
    "Russia": "Moscow",
    "Finland": "Helsinki",
    "Armenia": "Yerevan",
    "Croatia": "Zagreb"
}

#The input function gathers the user's name
name= str(input("Enter name:"))
print (f"You may start the quiz now, {name}. Good luck!")

#the variable score is used to track the score as the user answer the questions
score = 0

#the for loop ask the capitals of the country in the dictionary 
for country, capital in Capitals.items():
    answer= str(input(f"What is the capital of {country}?"))

    #the lower() sytax makes the answer case insensitive
    if answer.lower() == capital.lower():
        print("Correct!")

        #the score increases by 1 for each correct answer
        score +=1

#if the answer is incorrect the correct answer is displayed by using an f-string
    else:
        print(f"Incorrect. The answer is {capital}.")

#the final score is displayed and the total number of questions is shown using len()
print (f"Your final score is {score} out of {len(Capitals)}")




