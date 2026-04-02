
import random

J = 5
Q = 10
K = 15
B = 25
Coins = 100
while Coins > 0:
    X = int(input("Bet: \n"))
    while X <= 0 or X > Coins:
        X = int(input("Invaild..Bet:  \n"))
    def slots():
        reel_1 = random.randint(1, 20)
        if reel_1 in [1, 3, 5, 15, 16, 17]:
            R1 = J
            r1 = "J"
        elif reel_1 in [4, 6, 11]:
            R1 = Q
            r1 = "Q"
        elif reel_1 in [7, 11]:
            R1 = K
            r1 = "K"
        elif reel_1 in [2, 20]:
            R1 = B
            r1 = "$"
        else:
            R1 = 0
            r1 = "#"
        reel_2 = random.randint(1, 20)
        if reel_2 in [1, 3, 5, 15, 16, 17]:
            R2 = J
            r2 = "J"
        elif reel_2 in [6, 4, 12]:
            R2 = Q
            r2 = "Q"
        elif reel_2 in [7, 11]:
            R2 = K
            r2 = "K"
        elif reel_2 in [2, 20]:
            R2 = B
            r2 = "$"
        else:
            R2 = 0
            r2 = "#"
        reel_3 = random.randint(1, 20)
        if reel_3 in [1, 3, 5, 15, 16, 17]:
            R3 = J
            r3 = "J"
        elif reel_3 in [6, 4, 12]:
            R3 = Q
            r3 = "Q"
        elif reel_3 in [7, 11]:
            R3 = K
            r3 = "K"
        elif reel_3 in [2, 14, 18, 20]:
            R3 = B
            r3 = "$"
        else:
            R3 = 0
            r3 = "#"
        return r1, r2, r3, R1, R2, R3
    r1, r2, r3, R1, R2, R3 = slots()
    if R1 == 0 and R2 == 0 or R2 == 0 and R3 == 0 or R1 == 0 and R3 == 0:
        print("You lose")
        win = Coins - X
    elif R1 == R2 and R2 == R3 and R1 == B:
        print ("BONUS", r1, r2, r3)
        win = (X * R2)
        print (win)
        bonus = 6
        bonus_win = 0 + win
        while bonus > 1:
            win = (win)
            r1, r2, r3, R1, R2, R3 = slots()
            reel_win = (R1 + R2 + R3)
            print (r1,r2,r3)
            bonus -= 1
            bonus_win = bonus_win + reel_win
            print (bonus_win)
        win = (bonus_win + Coins)
    elif R1 == R2 and R2 == R3:
        print ("Congrats!", R2 * X + Coins)
        win = (R2 * X + Coins)
    elif R1 == R2 or R2 == R3:
        print ("Winner Winner!", X / 2 * R2 + Coins)
        win = (X / 2 * R2 + Coins)
    elif R1 == R3:
        print ("Wow! Awesome!", X / 2 * R3 + Coins)
        win = (X / 2 * R3 + Coins)
    elif R1 != R2 and R2 != R3:
        print("You lose")
        win = Coins - X
    print(r1,r2,r3)
    Coins = win


    print ("balance", Coins)
    E = str(input("Cash out? y or n \n"))
    if E == "y":
        Coins = 0
