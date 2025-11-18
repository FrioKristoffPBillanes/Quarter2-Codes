destcount = input("How many destinations do you have?\n")
try:
    destcount = int(destcount)
except ValueError:
    print("Please enter a valid number.")
    exit()
dests = []
for i in range(0, destcount):
    dest = str(input(f"Destination {i + 1}: \n"))
    dest = dest.capitalize()
    dests.append(dest)
print("\n")
def finalization(): 
    print("Your destinations are: \n")
    for x in range(0, len(dests)):
        print(f"Destination {x+1}: {dests[x]}")
    final = str(input("Is this final? (yes/no) \n"))
    final = final.lower()
    if final == "yes":
        print("\n Your itinerary has been finalized.")
        print("Your destinations are: \n")
        for x in range(0, len(dests)):
            print(f"Destination {x+1}: {dests[x]}")
        exit()
    if final == "no":
        change = str(input("Would you like to change a destination, add a destination, or remove a destination? (change/add/remove) \n"))
        change = change.lower()
        if change == "change":
            destchange = int(input(f"Which item would you like to change? (1 - {len(dests)}) \n"))
            newdest = str(input(f"Enter new destination for destination {destchange}: \n"))
            newdest = newdest.capitalize()
            destchange -= 1
            if dests[destchange] == newdest:
                print("That is already your destination.")
                finalization()
            dests[destchange] = newdest
            finalization()
        if change == "add":
            newdest = str(input("Enter new destination to add: \n"))
            newdest = newdest.capitalize()
            dests.append(newdest)
            finalization()
        if change == "remove":
            removedest = str(input(f"Which destination would you like to remove? \n"))
            removedest = removedest.capitalize()
            if dests.count(removedest) > 0:
                dests.remove(removedest)
                finalization()
            else:
                print("That destination is not in the list.")
                finalization()
        else:
            print("Please answer with 'change', 'add', or 'remove'.")
            finalization()

finalization()
