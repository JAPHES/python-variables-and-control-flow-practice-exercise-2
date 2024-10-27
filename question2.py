# THE WHILE LOOP
#THE FOLLOWING IS A PROGRAM THAT IS USED TO ASK FOR A INPUTS UNTIL SOMEONE TO TYPE EXIT FOR IT TO STOP

def continuous_input():
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print(f"You entered: {user_input}")

# Call the function
continuous_input()

