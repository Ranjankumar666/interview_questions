import math

def sqrt(x):
    lastGuess = x/2
    
    while True:
        guess = (lastGuess + x/lastGuess)/2
        if abs(guess - lastGuess) < 0.0000001:
            return math.floor(guess)
        lastGuess = guess

print(sqrt(4))