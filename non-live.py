from Transformations import Trans



t = Trans("((x+2)**2)")

while True:
    print(t.ListToString())
    uinput = input("\n> ")
    if uinput == "quit":
        exit(0)
    elif uinput == "up":
        t.translate(axis="y", val=1)
    elif uinput == "down":
        t.translate(axis="y", val=-1)
    elif uinput == "left":
        t.translate(axis="x", val=1)
    elif uinput == "right":
        t.translate(axis="x", val=-1)
    elif uinput == "x":
        t.reflect(axis="x")
    elif uinput == "y":
        t.reflect(axis="y")
    elif uinput == "plot":
        t.plot()


        
