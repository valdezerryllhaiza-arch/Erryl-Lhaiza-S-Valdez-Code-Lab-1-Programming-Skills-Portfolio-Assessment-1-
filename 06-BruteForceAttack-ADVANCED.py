#the correct password is stored in the variable
correct_password= "Secret123" 

#the maxium attempts is set to 5
max_attempts = 5

#the variable is used to track the number of attempts left
attempt_left = max_attempts

#the while loop statement countinues until the user runs out of attempt or enter the correct password
while attempt_left > 0:
    user_input = input("Enter Password:")
    if user_input == correct_password:
    
        #if the user input the correct password, access is granted and the loop breaks
        print ("Access Granted")
        break

    else:
        #if the user input the wrong password, the attempt left is decreased by 1
        attempt_left -= 1

        #the f-string displays the number of attempts left
        print (f"Access denied. You have {attempt_left} attempts left")
        
        #if the user reached the maxium attempts, a notification message is displayed 
        if attempt_left == 0:
            print ("Maxium attempts reached. Authorities have been notified.")
