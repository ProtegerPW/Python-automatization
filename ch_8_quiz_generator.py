#! /usr/bin/python3
# Program to generate 35 random quizes with answers and to save everything in files
import random, os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

if os.path.isdir("./folderWithTests"):
    os.chdir("./folderWithTests")
else:
    os.makedirs("./folderWithTests")
    os.chdir("./folderWithTests")


for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    quizFile = open("capitalQuiz_%s.txt" % (quizNum + 1), "w")
    answerFile = open("capitalQuiz_%s_Answer" % (quizNum + 1), "w")

    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')    
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))    
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states.   
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for question in range(50):
        trueAnswer = capitals[states[question]]
        falseAnswer = list(capitals.values())
        del falseAnswer[falseAnswer.index(trueAnswer)]
        falseAnswer = random.sample(falseAnswer, 3)         
        answerOptions = falseAnswer + [trueAnswer]       
        random.shuffle(answerOptions)

        quizFile.write('%s. What is the capital of %s?\n' % (question + 1, states[question]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))        
        quizFile.write('\n')       
        answerFile.write('%s. %s\n' % (question + 1, 'ABCD'[answerOptions.index(trueAnswer)]))    
    quizFile.close()    
    answerFile.close()