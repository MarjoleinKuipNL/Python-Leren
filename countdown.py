# use recursion to implement a countdown counter

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown
countdown(5)
