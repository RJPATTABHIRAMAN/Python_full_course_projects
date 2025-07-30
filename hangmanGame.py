import random

words = ["apple","orange","banana","pineapple","coconut"]

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}


def display_man(wrong_answer):
    print("**************")
    for line in hangman_art[wrong_answer]:
        print(line)
    print("***************")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    pass
def main():
    answer = random.choice(words)
    hint =['_']*len(answer)
   #  print(hint)
    wrong_gusses = 0
    gussed_leters = set()
    is_running = True
    while is_running:
        display_man(wrong_gusses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in gussed_leters:
            print(f"{guess} is already guessed")
            continue
        gussed_leters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i] =guess
        else:
            wrong_gusses+=1
        if "_" not in hint:
            display_man(wrong_gusses)
            display_answer(answer)
            print("You win")
            is_running = False
        elif wrong_gusses >= len(hangman_art)-1 :
            display_man(wrong_gusses)
            display_answer(answer)
            print("you Losss!")
            is_running = False
        
         

  


if __name__ == "__main__":
    main()