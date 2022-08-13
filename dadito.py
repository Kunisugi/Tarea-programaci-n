import random
print("hola mundo")

variable = input("quieres jugar al dado s/n")

if variable == "s":

    dado = random.randrange(7) 

    if dado == 1:
        print("1")
    if dado == 2:
        print("2")
    if dado == 3:
        print("3")
    if dado == 4:
        print("4")
    if dado == 5:
        print("5")
    else:
        print("6")

else:
    print (".I.")

