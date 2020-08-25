import random


def reveal_attempted_letters(mystery_word, attempted_letters):
    revealed_word = ''
    for letter in mystery_word:
        is_found = attempted_letters.count(letter) > 0
        if is_found:
            revealed_word += letter
        else:
            revealed_word += '-'

    return revealed_word


def detect_errors(input_string, attempted_letters):
    is_one_char = len(input_string) == 1
    if not is_one_char:
        err_mess = "You should input a single letter"
        return err_mess

    is_lower_ascii = input_string.isascii() and input_string.islower()
    if not is_lower_ascii:
        err_mess = "It is not an ASCII lowercase letter"
        return err_mess

    is_already_tried = attempted_letters.count(input_string) > 0
    if is_already_tried:
        err_mess = "You already typed this letter"
        return err_mess

    err_mess = None
    return err_mess


def new_game():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    correct_answer = random.choice(word_list)
    remaining_attempts = 8
    all_attempted_letters = []

    game_is_over = False
    game_is_win = False
    while not game_is_over and not game_is_win:
        print("\n" + reveal_attempted_letters(correct_answer, all_attempted_letters))

        entered_char = input('Input a letter:')

        err_mess = detect_errors(entered_char, all_attempted_letters)
        if err_mess is not None:
            print(err_mess)
            continue

        all_attempted_letters.append(entered_char)
        in_the_word = correct_answer.find(entered_char) >= 0
        if not in_the_word:
            remaining_attempts -= 1
            print('No such letter in the word')

        game_is_over = remaining_attempts <= 0
        game_is_win = reveal_attempted_letters(correct_answer, all_attempted_letters).count('-') == 0

    if game_is_win:
        print("You guessed the word!")
        print("You survived!")
    elif game_is_over:
        print("You are hanged!")

    return


if __name__ == '__main__':
    want_to_play = True
    while want_to_play:
        print("H A N G M A N")
        answer = input("Type \"play\" to play the game \"exit\" to quit:")

        if answer == 'exit':
            want_to_play = False
        elif answer == 'play':
            new_game()
        else:
            continue
