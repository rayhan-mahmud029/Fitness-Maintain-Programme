import datetime


def getdate():
    import datetime
    return datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')

#intro
print("***Hello sir, This is a fitness maintain Programme. Here you can write down your Food routine or Excercise routine.**** \n **//THIS PROGRAM IS PROGRAMMED BY RAYHAN MAHMUD**//")


#ask read or write?
r_w = input("What do you want? Write down routines or read? Type 'r' for read and 'w' for wite__ \n")
user_input = input("Whats your name: \n")
user_input2 = input("Food or Excercise? \n")


#if choose 'w'(write)
if r_w == "w":
    def HMsys():
        with open(f"{user_input}s{user_input2}.txt", "a") as f:
            f.write(getdate() + " : " + input("write down here: \n") + "\n")
        return f"You have been logged {user_input}s {user_input2} routine at.." + getdate()
        
    print(HMsys())
    wish = input("If want to read logs type 'r'. To leave type 'e': ")

    if wish == 'r':
      def readHM():
        with open(f"{user_input}s{user_input2}.txt") as f:
            output = f.readlines()
            print(f"{user_input}s {user_input2} log details...")
            for item in output:
                print(item)
        return exit()
               
      print(readHM()) 
    
    elif wish == 'e':
        print(exit())



#if choose 'r'(read)
elif r_w == 'r':
    def readHM():
        with open(f"{user_input}s{user_input2}.txt") as f:
            output = f.readlines()
            print(f"{user_input}s {user_input2} log details...")
            for item in output:
                print(item)
               
    print(readHM())
    wish = input("If want to write logs type 'w'. To leave type 'e': ")

    if wish == 'w':
      def HMsys():
        with open(f"{user_input}s{user_input2}.txt", "a") as f:
            f.write(getdate() + " : " + input("write down here: \n") + "\n")
        return f"You have been logged {user_input}s {user_input2} routine at.." + getdate()
        

      print(HMsys()) 
    
    elif wish =='e':
        print(exit())
    
