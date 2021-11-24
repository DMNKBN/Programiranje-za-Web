import random

secret = random.randint(1,30)

attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("HIGHSCORE:" + str(best_score))

while True:
    guess = int(input("Pogodite broj od 1 do 30: "))
    
    attempts += 1

    if guess == secret:
        if attempts < best_score:
          with open("score.txt", "w") as score_file:
            score_file.write(str(attempts))

        print("Bravo, tajni broj je pogođen:" + str(secret))
        
        print("Broj pokušaja do pogođenog broja:" + str(attempts))
        break
    
    elif guess > secret:
        print("Netočno, tajni broj nije pogođen.Pokušajte s manjim brojem.")
    elif guess < secret:
            print("Netočno, tajni broj nije pogođen. Pokušajte s većim brojem.")
