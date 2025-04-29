import random
    
questions = {
    "science": [
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
        {"question": "How many bones are in the adult human body?", "answer": "206"}
    ],
    "history": [
        {"question": "Who was the first President of the United States?", "answer": "George Washington"},
        {"question": "In which year did World War II end?", "answer": "1945"},
        {"question": "Who was the Egyptian queen famous for her beauty and relationship with Julius Caesar?", "answer": "Cleopatra"},
        {"question": "What wall was torn down in 1989 symbolizing the end of the Cold War?", "answer": "The Berlin Wall"}
    ],
    "pop": [
        {"question": "Who played Iron Man in the Marvel movies?", "answer": "Robert Downey Jr"},
        {"question": "Which singer is known as the 'Queen of Pop'?", "answer": "Madonna"},
        {"question": "Which movie features a talking snowman named Olaf?", "answer": "Frozen"},
        {"question": "What is the name of the coffee shop in Friends?", "answer": "Central Perk"}
    ]
}

num_of_players = int(input("\nEnter Number  of players : "))
players=[]

for player in range(1, num_of_players + 1):
    players.append(input(f"\nPlayer {player} enter your name : "))

print(players)
scores = {}

for name in players:
   scores[name] = 0



rounds = int(input("\nHow many rounds you want to play ? "))

def ask_question(player):

    print(f"\n{player} its your turn : ")
    category = input(f"Choose a category (science, history, pop): ").lower()
    q =  random.randint(0, 3)

    if not (category == "science" or category == "history" or category == "pop"):
        print("\nWrong input!!!\n")

    elif category == "science":
        q1 = questions[category][q]["question"]
        print(f"\n The question is -> {q1}")
        answer = input("\nEnter you answer : ")
        if str(questions[category][q]["answer"]).lower() == answer.lower():
            print("\nYou are Right!")
            temp = scores[player] + 1
            scores[player] = temp
        else:
            print("\nWrong!!!")
            print(f"The right answer is : {questions[category][q]["answer"]}")

    elif category == "history":
        q1 = questions[category][q]["question"]
        print(f"\n The question is -> {q1}")
        answer = input("\nEnter you answer : ")
        if str(questions[category][q]["answer"]).lower() == answer.lower():
            print("\nYou are Right!")
            temp = scores[player] + 1
            scores[player] = temp
        else:
            print("\nWrong!!!")
            print(f"The right answer is : {questions[category][q]["answer"]}")

    elif category == "pop":
        q1 = questions[category][q]["question"]
        print(f"\n The question is -> {q1}")
        answer = input("\nEnter you answer : ")
        if str(questions[category][q]["answer"]).lower() == answer.lower():
            print("\nYou are Right!")
            temp = scores[player] + 1
            scores[player] = temp
        else:
            print("\nWrong!!!")
            print(f"The right answer is : {questions[category][q]["answer"]}")

winner = {}


def show_score(i, name):
    print(f"\n The scores are - {players[i]} : {scores[players[i]]}")
    

for round in range(1,rounds + 1):
    i = 0
    for name in players:
        ask_question(name)
        show_score(i, name)
        #print(f"\n The scores are - {players[i]} : {scores[players[i]]}")
        i = i + 1

def declare_winner():
    highest_score = 0
    for player in scores:
        #print(f"message: {scores[player]}")

        if scores[player] >= highest_score:
            highest_score = scores[player]
            
    print("\n~~~~~~~~~~~~~~~~~\n")        
    print(f"\n\nThe highest score is : {highest_score}")  

    print("The winners are : ")

    for player in scores:
        if highest_score == scores[player]:
            print(f"{player}" )        

declare_winner()


print(f"\n\n\n ~~~~~~~~~~~~~~~~ Game over ! ~~~~~~~~~~~~~~~~")

i