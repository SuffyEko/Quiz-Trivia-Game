import random
import file_operations

def display_questions(questions):
    selected_question = random.choice(questions)
    print("Question:",selected_question['question'])
    print("OPtions:", selected_question['options'])
    original_answer = selected_question['answer']
    answer = input("Enter answer: ").upper()
    is_right = validate_answer(answer, original_answer)
    return is_right


def validate_answer(answer, original_answer):
    if answer == original_answer:
        is_correct = True
    else:
        is_correct = False

    return is_correct


def update_score(is_right, score):
    if is_right:
        score += 10

    return score



def get_highest_score(score, highest_score):
    if score > highest_score:
        highest_score = score
    return highest_score



def create_new_user():
    users = file_operations.load_file("users.json")
    exist = []
    for u in users:
        exist.append(u['username'])

   
    while True:
        print("=========================")
        username = input("Choose a username: ").strip()
        if not username:
            print("Username cannot be empty")
            continue

        if username in exist:
            print("username exists!")
            continue
        
        break

        

    while True:
        print("=========================")
        print("password must be 4 letters")
        print("=========================")
        password = input("Enter password: ").strip()
        if len(password) == 4:
            break

    user = {
        "username": username,
        "password": password,
        "score": 0,
        "highest score": 0
    }

    users.append(user)
    highest_score = user['highest score']
    score = 0
    try:
        file_operations.save_file(users, "users.json")
    except:
        pass
    else:
        print("==========================")
        print("User created successfully!")
    return username, highest_score

def check_user():
    '''
    load users
    extract name, score and highest_score
    get username and password from user
    let user play game
    modify the user details
    save the new details

    
    '''
    while True:
        choose = input("New user enter new | Existing user enter exist | Type exit to quit: ").strip()
        if choose == 'new':
            name, highest_score = create_new_user()
            return name, highest_score
        elif choose == 'exist':
            name, highest_score = get_existing_user()
            return name, highest_score
        elif choose == 'exit':
            exit()
        else:
            print("============================")
            print("Enter new | exist | exit")
            continue
    

    
def get_existing_user():
    users = file_operations.load_file("users.json")
    users_list = []
    name = None
    password = None
    score = None
    highest_score = None
    matched_user = None

    for u in users:
        users_list.append(u["username"])
    
    while True:
        username = input("Enter your username: ").strip()
        if username in users_list:
            for u in users:
                if username == u["username"]:
                    matched_user = u
                    password = u["password"]
                    break
            break
        else:
            print("==========================")
            print("incorrect username")
            continue

    while True:
        passcode = input("Enter password: ").strip()
        if passcode == password:
            name = matched_user['username']
            score = matched_user['score']
            highest_score = matched_user["highest score"]
            break
        else:
            print("==========================")
            print("incorrect password")
            continue

    return name, highest_score
