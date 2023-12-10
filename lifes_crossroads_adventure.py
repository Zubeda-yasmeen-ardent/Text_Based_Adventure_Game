import time

def welcome_message():
    print("\nWelcome to the world!")
    time.sleep(2)
    print("\nAssume you are an elementary school kid.")
    time.sleep(1)
    print("\nYou are completely unaware of the outside world.")
    time.sleep(1)
    print("\nAfter years of studying in adolescence, you finally complete your elementary school.")
    time.sleep(1)
    print("\nAs you stand at the crossroads of life, a mysterious figure appears before you offering two paths.")

def choose_path_education():
    print("\nNow you have two choices:")
    time.sleep(2)
    print("\n1. Join the Formal Education system to get further education.")
    time.sleep(1)
    print("\n2. Quit the formal education system and build skills.")
    time.sleep(1)
    ans_1 = input("\nEnter your choice (1/2): ")
    time.sleep(1)
    if ans_1 == '1':
        formal_education()
    elif ans_1 == '2':
        build_skills()
    else:
        print("\nERROR! Enter a valid input.")
        time.sleep(1)
        choose_path_education()

def formal_education():
    time.sleep(1)
    print("\nCongratulations! You decide to embrace formal education.")
    time.sleep(1)
    print("\nYou find yourself in a prestigious academy, where the pursuit of knowledge is paramount.")
    time.sleep(1)
    print("\nNow you have two choices:")
    time.sleep(1)
    print("\n1. Focus on a particular core subject, aiming to become a master in that field.")
    time.sleep(1)
    print("\n2. Balance your studies, nurturing both academic excellence and practical skills.")
    time.sleep(1)
    ans_2 = input("\nEnter your choice (1/2): ")
    time.sleep(1)
    if ans_2 == '1':
        print("\nOOPS! You are being trapped by the Matrix! You lost.")
        time.sleep(1)
    elif ans_2 == '2':
        print("\nGreat choice! You embark on a journey of holistic development.")
        time.sleep(1)
    else:
        print("\nERROR! Enter a valid input.")
        time.sleep(1)
        formal_education()

def build_skills():
    print("\nCongratulations!")
    time.sleep(1)
    print("\nYou choose to forge your own path, away from the traditional education system.")
    time.sleep(1)
    print("\nFacing challenges, you discover hidden talents and passions.")
    time.sleep(1)
    print("\nNow you are left with two choices:")
    time.sleep(1)
    print("\n1. Face obstacles head-on, pursuing your dreams with determination.")
    time.sleep(1)
    print("\n2. Succumb to the pressure and quit the unconventional path.")
    time.sleep(1)
    ans_3 = input("\nEnter your choice (1/2): ")
    time.sleep(1)
    if ans_3 == '1':
        print("\nYah Champion! You break free from the Matrix and carve your own destiny.")
        time.sleep(1)
    elif ans_3 == '2':
        print("\nYou lost it! The pressure proved too much, and you returned to the ordinary.")
        time.sleep(1)
    else:
        print("\nERROR! Enter a valid input.")
        time.sleep(1)
        build_skills()

def start_game():
    welcome_message()
    choose_path_education()

# Start the game
start_game()
