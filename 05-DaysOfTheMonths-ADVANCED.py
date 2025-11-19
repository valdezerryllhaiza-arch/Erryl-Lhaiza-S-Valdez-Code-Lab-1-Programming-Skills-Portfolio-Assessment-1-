#the calendar dictionary stored the month and their assigned number of days 
#the calendar is not considering the leap year for Febuary
calendar ={ 1:31,
            2:28,
            3:31, 
            4:30, 
            5:31, 
            6:31, 
            7:31, 
            8:31, 
            9:31, 
            10:31, 
            11:31, 
            12:31, 
                   }

#the user is asked to input a month number
month_number= int(input("Enter number:"))

#if the user input less than 1 or greater than 12, it will print invalid
if month_number <1 or month_number >12:
    print ("Invalid")

#if the user input 2 for febuary, it will ask if it is a leap year or not
elif month_number ==2:
    leap_year_input = input("Is the date leap year? yes/no:" ) 

#if the user input yes, it will display 29 days
    if leap_year_input.lower() =="yes": 
        leap_year_day= 29
        print (f"Month {month_number} has {leap_year_day} days")
    else: 
        normal_day= 28
        print (f"Month {month_number} has {normal_day} days")

#for the other months, it will display the number of days from the dictionary
else:
    days= calendar [month_number]
    print(f" Month {month_number} has {days} days")

