def get_start_input(prompt):
    while True:
        start = input(prompt).strip().lower()
        if start == "start":
            return
        print("=========================================")
        print("Enter only start to actually start buddy!")
        print("=========================================")

def greet_user(username='Quick user'):
    print("======================================================================")
    print("Welcome", username)

    print('''
==================================================================
Welcome to Terminal Trivia: Programming Edition!
Test your coding knowledge with a series of quick,
basic programming questions. Whether you are a se-
asoned developer looking for a fun refresher or a 
beginner testing your roots, this terminal-based
challenge will put your syntax, logic, and compu-
ter science fundamentals to the test.
Type start to start the game and see how many bugs you can squish!
==================================================================
''')

def display_score(score):
    print("============================")
    print(f"===Score: {score}===")
    print("============================")

def display_highest_score(highest_score):
    print("============================")
    print(f"===Highest Score: {highest_score}===")
    print("============================")

def retstart():
    while True:
        selected = input("Restart (yes/no)? ").strip().lower()
        if selected:
            if selected == "no":
                return False
            elif selected == "yes":
                return True
            else:
                print("============================")
                print("only yes/no is accepted")
                continue

        else:
            print("============================")
            print("only yes/no is accepted")
            continue
