# Chatbot
#Author: Colton Farbatuk
#Date: 2018-06-13

# Program is a chat bot that allows two questions and gives random answers
#Step1: create lists of possible answers and functions to run program
#step2: create variables to hold inputs that strip away unessecary characters
#step3: create decision structure to proceed if the right input is in the list
#step4: create decision structure to proceed if the wrong input is entered
#step5: create accumlator x & count-controlled while loop to run two iterations
#step6: take inputs, search for keyword in input and create decision structure
#step7: create functions for random numbers to randomly select answers
#step8: increase accumlators to end loop and program
def main():
    yeses = ["yes","certainly","sure","y","of course"]
    noses = ["no","n","of course not","certainly not","never"]
    goodbye = ["ciao", "goodbye", "Dasvedanya", "adios"]
    answer = input("Do you want to chat?")
    answer = answer.lower().strip("!?.")
    if answer in yeses and answer not in noses:
        print("Great you can ask me some questions!")

        x = 0
        while x < 2:
            answer = input("\nAsk me a question ")
            if "name" in answer:
                print("\nMy name is chatbot3000 !")
                x+=1
            else:
                randomnum()
                list1or2, number = randomnum()
                if list1or2 == 1:
                    print(yeses[number])
                    x+=1
                else:
                    print(noses[number])
                    x+=1
                
    elif answer not in yeses and answer in noses:
        print("I guess you dont want to chat, goodbye!")
    else:
        print("im sorry i didnt understand!")
        main()
    ending()
    bye = ending()
    print(goodbye[bye])



def randomnum():
    list1or2 = random.randint(0,2)
    number = random.randint(0,4)
    return list1or2, number
def ending():
    bye = random.randint(0,3)
    return bye
   
import random
main()
