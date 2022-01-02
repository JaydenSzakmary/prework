while True:
    response = input("What do you want to do? Say hi[h], say goodbye[g], or quit[q]    "   )
    if response == "h":
        print("Hello!")
    elif response == "g":
        print("Goodbye!")
    elif response == "quit":
        break
    else: 
        print("Invalid Option")
