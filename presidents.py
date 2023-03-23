from dataclasses import dataclass
import random

presidents = [{"number": 46, "name": "Joe Biden"},
{"number": 45, "name": "Donald Trump"},
{"number": 44, "name": "Barack Obama"},
{"number": 43, "name": "George W. Bush"},
{"number": 42, "name": "Bill Clinton"},
{"number": 41, "name": "George H.W. Bush"},
{"number": 40, "name": "Ronald Reagan"},
{"number": 39, "name": "Jimmy Carter"},
{"number": 38, "name": "Gerald Ford"},
{"number": 37, "name": "Richard Nixon"},
{"number": 36, "name": "Lyndon Johnson"},
{"number": 35, "name": "John F. Kennedy"},
{"number": 34, "name": "Dwight Eisenhower"},
{"number": 33, "name": "Harry Truman"},
{"number": 32, "name": "Franklin Roosevelt"},
{"number": 31, "name": "Herbert Hoover"},
{"number": 30, "name": "Calvin Coolidge"},
{"number": 29, "name": "Warren Harding"},
{"number": 28, "name": "Woodrow Wilson"},
{"number": 27, "name": "Howard Taft"},
{"number": 26, "name": "Theodore Roosevelt"},
{"number": 25, "name": "William McKinley"},
{"number": 24, "name": "Grover Cleveland"},
{"number": 23, "name": "Benjamin Harrison"},
{"number": 22, "name": "Grover Cleveland"},
{"number": 21, "name": "Chester Arthur"},
{"number": 20, "name": "James Garfield"},
{"number": 19, "name": "Rutherford B. Hayes"},
{"number": 18, "name": "Ulysses S. Grant"},
{"number": 17, "name": "Andrew Johnson"},
{"number": 16, "name": "Abraham Lincoln"},
{"number": 15, "name": "James Buchanan"},
{"number": 14, "name": "Franklin Pierce"},
{"number": 13, "name": "Millard Fillmore"},
{"number": 12, "name": "Zachary Taylor"},
{"number": 11, "name": "James K. Polk"},
{"number": 10, "name": "John Tyler"},
{"number": 9, "name": "William Harrison"},
{"number": 8, "name": "Martin Van Buren"},
{"number": 7, "name": "Andrew Jackson"},
{"number": 6, "name": "John Quincy Adams"},
{"number": 5, "name": "James Monroe"},
{"number": 4, "name": "James Madison"},
{"number": 3, "name": "Thomas Jefferson"},
{"number": 2, "name": "John Adams"},
{"number": 1, "name": "George Washington"},
]

@dataclass
class Question:
    qname: str
    qnum: int

preslist = []

for item in presidents:
    presname = item["name"]
    presnum = item["number"]
    new_question = Question(presname, presnum)
    preslist.append(new_question)

def quizprompt():
    x = random.choice(preslist)
    return x

def percent(x,y):
    percent = round((y/x) * 100)
    return percent

def quizloop():
    print('''
    ################ PRESIDENT NUMBER GAME ################

    You will be prompted with the name of a president, the goal is to guess the number.
    Example:  George Washington is 1st, so enter 1

    ''')
    correct = 0
    incorrect = 0
    counter = 0
    x = int(input('How many questions would you like? '))
    while (correct + incorrect) !=x:
        president = quizprompt()
        print(president.qname)
        answer = int(input("\nEnter president number or 0 to quit: "))
        if answer == president.qnum:
            print('\ncorrect!\n')
            correct +=1
        elif answer == 0:
            break
        else:
            print('wrong!\n')
            incorrect +=1
    else:
        print(f'Game Over!  You got {correct} right and {incorrect} wrong! ({percent(correct,incorrect)}%)')

if __name__ == '__main__':

    quizloop()


        






