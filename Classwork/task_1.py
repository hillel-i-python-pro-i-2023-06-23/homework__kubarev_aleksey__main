players = ["Игрок 1", "Игрок 2"]
current_player_index = 0
used_words = []


def get_current_player():
    return players[current_player_index]

def change_turn():
    global current_player_index
    current_player_index = (current_player_index + 1) % len(players)

def is_word_valid(new_word):
    if new_word in used_words:
        return False
    else:
        last_word = used_words[-1]
        if last_word[-1] == 'ь' or last_word[-1] == 'и':
            if last_word[-2] == new_word[0]:
                return True
            else:
                print("Incorrect word")
                return False
        else:
            if last_word[-1] == new_word[0]:
                return True
            else:
                print("Incorrect word")
                return False

def play_game():
    print("===== Игра слов =====")
    print("Введите '!выход' для завершения игры.")
    print("Введите '!помощь' для получения правил игры.")
    print()

    while True:
        current_player = get_current_player()
        word = input(f"[{current_player}] Введите слово: ")

        if word == "!выход":
            print("Игра завершена.")
            break
        elif word == "!помощь":
            print("Правила игры:")
            print("  - Игроки должны вводить слова по очереди.")
            print("  - Последняя буква предыдущего слова должна совпадать с первой буквой следующего слова.")
            print("  - Запрещено использовать ранее использованные слова.")
            print("  - Если последняя буква слова 'ь', 'й', 'ы' или 'ъ', следующее слово должно начинаться с предыдущей буквы.")
            continue

        if not is_word_valid(word):
            print("Слово недопустимо. Попробуйте снова.")
            continue

        used_words.append(word)
        print(f"Игрок {current_player} ввел слово '{word}'.")
        change_turn()

    print("Игра завершена.")

# Запуск игры
play_game()