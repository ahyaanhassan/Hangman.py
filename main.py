import random
from replit import clear
from assccii import stages
from hangman_words import word_list
# word_list=["ardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
lives=6
display=[]
word_length=len(chosen_word)
for _ in range(word_length):
    display.append("_")#display+=_
print(display)
end_of_game=False
while not end_of_game:#while end_of_game==false
    guess=input("guess the letter:- ").lower()
    clear()
    if guess in display:
        print("you already guessed it! kuch nya soch !!")

    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("you run out of the lives")
    print(lives)
    print(display)
    if "_" not in display:
        end_of_game=True
        print("you win")
    print(stages[lives])
