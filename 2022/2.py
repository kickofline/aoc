f = open("2.txt", "r")
score = 0
splitMoves = f.read().split('\n')

for i in splitMoves:
    moves = i.split(" ")
    elfMove = "rock" if moves[0] == "A" else "paper" if moves[0] == "B" else "scissors"
    myMove = "rock" if moves[1] == "X" else "paper" if moves[1] == "Y" else "scissors"
    print(myMove)
    if myMove == elfMove:
        score += 3
        print("tie +3 ")
    elif (myMove == "rock" and elfMove == "scissors") or (myMove == "paper" and elfMove == "rock") or (myMove == "scissors" and elfMove == "paper"):
        score += 6
        print("win + 6")
    score += (1 if myMove == "rock" else 2 if myMove == "paper" else 3)
    
    
    
print(score)