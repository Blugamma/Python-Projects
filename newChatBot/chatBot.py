###ChatBot###
import random

with open('stopWords.txt', 'r') as doc:
    stopWords = doc.read().split("\n")
    stopWords.append("name")

welcoming = ["Hey there", "Hello", "Hey"]
questions = ["How are you?", "How do you feel today?", "How is it going?"]
positiveAns = ["great", "good", "not bad", "amazing", "fine thanks"]
positiveRes = ["That's great", "Good to know", "Glad to here", "Amazing News"]
negativeAns = ["bad", "really annoyed", "could be better", "pissed off", "not good"]
negativeRes = ["That's a shame", "Cheer up", "Things could be worse", "Atleast you aren't a robot"]
random_welcoming = random.choice(welcoming)
random_question = random.choice(questions)
random_positiveRes = random.choice(positiveRes)
random_negativeRes = random.choice(negativeRes)
response = raw_input("BluBot: Hey what is your name?")

def calculateInput(input,output,useName):
    response = input.split(" ")
    for word in response:
        if word.lower() not in stopWords:
            if useName: print("Blubot: " + output + " " + word)
            else: print("Blubot: " + output)
            
calculateInput(response,random_welcoming,True)
welcoming_response = raw_input(random_question)
if welcoming_response.lower() in positiveAns:
    calculateInput(welcoming_response,random_positiveRes,False)
if welcoming_response.lower() in negativeAns:
    calculateInput(welcoming_response,random_negativeRes,False)

    
