import datetime

user_input = input("Whats your name: \n")
user_input2 = input("Food or Excercise? \n")


def HMsys():
    with open(f"{user_input}s{user_input2}.txt", "a") as f:
        f.write(datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p '))
        f.write("\n")
        f.write(input("Write down here: \n"))
        f.write("\n")
        f.write("\n")


print(HMsys())


def readHM():
    with open(f"{user_input}s{user_input2}.txt") as f:
        output = f.readlines()
        for items in output:
            return items
            


def getdate():
    import datetime
    return datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p')


print(f"You have been locked {user_input}s {user_input2} routine at..")
print(getdate())
print("Check it out ...")
print(readHM())
