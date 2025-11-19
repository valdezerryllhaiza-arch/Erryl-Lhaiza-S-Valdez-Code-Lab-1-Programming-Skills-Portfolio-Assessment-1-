#the names are stored in the tuple
names =("Jake", "Zac", "Ian", "Ron", "Sam", "Dave")

#the user is asked to input Sam to search in the tuple
search_name= str(input("Search name:"))

#the if statement checks if the name id in the tuple and displays the appropriate result
#the capitalized function is used to match the case to the names in the tuple
if search_name.capitalize() in names:
    print (f"{search_name} is found in the list")
else:
    print (f"{search_name} is not found in the list")
    

    

    
