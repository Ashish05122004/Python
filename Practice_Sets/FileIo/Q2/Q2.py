import random

def game():
    score = random.randint(1,100)
    with open("C:/Users/ashis/OneDrive/Desktop/Python/Practice_Sets/FileIo/Q2/Hi-score.txt") as f:
        high_score = f.read()
        if(not(high_score =="")):
            high_score =int(high_score)
        else:
            high_score =0
        print(f"your score is {score}")
        if(score>high_score or high_score ==0):
            with open("C:/Users/ashis/OneDrive/Desktop/Python/Practice_Sets/FileIo/Q2/Hi-score.txt", "w") as fr:
                fr.write(f"{score}")
                
game()