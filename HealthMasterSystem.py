import datetime


def getdate():
    import datetime
    return datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')


r_w = input(
    "Do you want to write the log or read? Type 'r' for read and 'w' for wite__ \n")
user_input = input("Whats your name: \n")
user_input2 = input("Food or Excercise? \n")


if r_w == "w":
    def HMsys():
        with open(f"{user_input}s{user_input2}.txt", "a") as f:
            f.write(getdate() + " : " + input("write down here: \n") + "\n")

    print(HMsys())
    print(f"You have been logged {user_input}s {user_input2} routine at.." + getdate())
    # print(getdate())



elif r_w == "r":
    def readHM():
        with open(f"{user_input}s{user_input2}.txt") as f:
            output = f.readlines()
            print(f"{user_input}s {user_input2} log details...")
            for item in output:
                print(item)
               

    print(readHM())
    
