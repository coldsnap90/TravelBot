
#This code is a travel bot that asks user based on questions asked what type of trip they would like 
#The travel bot will display info like name,age,preferences,flight price,hotel price,and possible discount

#Steps
#1: Make travel bot display a welcome message to user
#2: Travel bot will ask questions that will match user's preference for flights
#3. Travel bot will ask for name and age first
#4. Travel bot will then ask whether they like culture and classical music
#5. Travel bot will then ask whether they like beaches and surfing 
#6. Based of #4 and #5 the bot will then match offers to user's preference
#7. Senior discount will be added on if age over or equal to 65
#8. Every age after 65 will be 1+ (1%) percent discount
#9. If they are elligble for senior discount,display message 
#10.If user decides to say no to both preferences, user is asked if they want account
#11.If user doesn't want to create it will give a sorry and goodbye message
#12.If user wants account, user gets a one time password to create acc
#13.If user selects culture over beaches, bot suggests trip to Vienna
#14.If user selects beached over culture, bot suggets trip to Bali 
#15.If user selects both type of preferences, bot suggests pricier trip
#16.Bot will ask whether they're interested in making account even if no offer chosen
#17.User will be able to choose whether they want to make an account
#18.Bot will display their name, age, how many nights, their answers to preferences
#19.Bot will then display the details of their trip
#20.Details displayed is trip to where,price of flight, hotel, discount,total of all
#21.If user says no to both preferences display apology for not having trips right now
#22.Then display if they want account, if they do want acc give them a one time password
#23.If they don't want an account, display a goodbye message
#24.Display goodbye message at end no matter whether they pick preference, or make acc
#25.Display sorry to hear that message near end if they dont want acc, before goodbye
#26. Display looking forward to working with you, if they want acc, then goodbye

import random

def main():
   
    print("Welcome ! I am your friendly travel agent bot.I will ask you some questions,",
          "and make a recommendation based\non your answer. If you are interested ,",
          "I will provide you with a one-time password to create a user\naccount",
          "our website.\n")
    
    name = input("What is your name ? --> ")
    print("\nHello dear ", name,"!")
    age = int(input("\nWhat is your age? "))
    
    if age > 65:
        print("\nGreat! we offer a senior discount.\nFor every year over 64,",
              "you get 1% off.")

    discount(age)
    r = discount(age)
    
    trip_length = int(input("For how many nights do you want stay? "))
    print("Do you like culture and classical music?\n")
    
    choice1 = input("Please answer y/ n. --> ")
    print("Do you like beaches and surfing?\n")
    
    choice2 = input("Do you like beaches and surfing?\n",
    "Please answer y/ n. --> ")
    
    if choice1 == 'y'  and choice2 == 'n' :
        vienna(r,trip_length)
        Vienna_price,vienna_hotel,vienna_flight,r = vienna(r,trip_length)
        vienna_trip_print(Vienna_price,vienna_hotel,vienna_flight,r,trip_length)
        password(name,age)
        
    elif choice1 == 'n' and choice2 == 'y':
        bali(r,trip_length)
        Bali_price,bali_flight,bali_hotel,r = bali(r,trip_length)
        bali_trip_print(Bali_price,bali_flight,bali_hotel,r,trip_length)
        password(name,age)
        
    elif choice1 == 'y' and choice2 == 'y' and trip_length >= 2:
        bali(r,trip_length)
        Bali_price,bali_flight,bali_hotel ,r = bali(r,trip_length)
        bali_trip_print(Bali_price,bali_flight,bali_hotel,r,trip_length)
        password(name,age)
        
    elif choice1  == 'y' and choice2 == 'y' and trip_length < 2:
        vienna(r,trip_length)
        Vienna_price,vienna_hotel,vienna_flight,r = vienna(r,trip_length)
        vienna_trip_print(Vienna_price,vienna_hotel,vienna_flight,r,trip_length)
        password(name,age)
        
    elif choice1 =='n' and choice2 =='n':
        print("I am sorry, we dont have any trips to offer at this point.\n")
        password(name,age)

   
def discount(rate):
    if rate < 65:
        r = 0
        return r
      
    else:
        r = rate % 64
        r = float(r*0.01)
        return r

def bali(r,trip_length):
    if r == 0:
        bali_flight = 849.93
        bali_hotel = 235.35
        Bali_price = (bali_flight + (bali_hotel * trip_length))
        Bali_price = round(Bali_price,2)
        return Bali_price,bali_flight,bali_hotel, r
        
    else:
        bali_flight = 849.93
        bali_hotel = 235.35
        Bali_price = (bali_flight + (bali_hotel * trip_length))
        Bali_price = Bali_price - (r*(bali_flight + (bali_hotel * trip_length)))
        Bali_price = round(Bali_price,2)
        r = int(r*100)
        return Bali_price,bali_flight,bali_hotel,r
        
def vienna(r,trip_length):
    if r == 0:
        vienna_flight = 997.93
        vienna_hotel = 143.84
        Vienna_price = (vienna_flight + (vienna_hotel * trip_length))
        Vienna_price = round(Vienna_price,2)
        return Vienna_price, vienna_hotel, vienna_flight, r
    else:
        vienna_flight = 997.93
        vienna_hotel = 143.84
        Vienna_price = vienna_flight + (vienna_hotel * trip_length)
        Vienna_price = Vienna_price - (r*(vienna_flight +(vienna_hotel * trip_length)))
        Vienna_price = round(Vienna_price,2)
        r = int(r*100)
        return Vienna_price, vienna_hotel, vienna_flight,r

def bali_trip_print(Bali_price,bali_flight,bali_hotel,r,trip_length):
    print("How about a trip to Bali ?")
    print("Flight: ",bali_flight,"$")
    print("Hotel: ",bali_hotel,"$/night" )
    print("Discount: ",r,"%")
    print("Total for", trip_length, " nights (incl. discounts): ",Bali_price, "$")
    
def vienna_trip_print(Vienna_price,vienna_hotel,vienna_flight,r,trip_length):
    print("How about a trip to Vienna ?")
    print("Flight: ",vienna_flight,"$" )
    print("Hotel: ",vienna_hotel,"$/night" )
    print("Discount: ",r,"%")
    print("Total for", trip_length, " nights (incl. discounts): ",Vienna_price, "$")
    
def password(name,age):
    print("\nAre you interested, and want to create a user account?")
    password = input("Please answer y/ n. --> ")
    if(password == 'y'):
        print("\nLooking forward to working with you!")
        length = len(name)
        last_letter = name[length-1]
        password_second = name[0]
        n_multiplier = (age % 8)
        password_first = (last_letter * n_multiplier)
        ran_number = random.randint(0,5)
        password_third = (ran_number * '!')
        password = (password_first + password_second + password_third)
        print("\nYour one-time password is: ",password,"\nGoodbye.")

                                 

    elif(password =='n'):
        print("\nSorry to hear that. Please consider using our service again.",
              "\nGoodbye.")

main()
