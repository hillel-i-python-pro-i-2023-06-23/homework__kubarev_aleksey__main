players = ["Игрок 1", "Игрок 2"]
current_player_index = 0
used_words = []


def get_current_player():
    return players[current_player_index]

def change_turn():
    global current_player_index
    current_player_index = (current_player_index + 1) % len(players)


def is_word_valid(word):
    if word in used_words:
        return False
    if len(used_words) > 0:
        last_word = used_words[-1]
        if last_word[-1] in ["ь", "й", "ы", "ъ"]:
            if word[0].lower() != last_word[-2].lower():
                return False
        else:
            if word[0].lower() != last_word[-1].lower():
                return False
    return True


def play_game():
    print("===== Игра слов =====")
    print("Введите '!выход' для завершения игры.")
    print("Введите '!правила' для получения правил игры.")
    print()

    while True:
        current_player = get_current_player()
        word = input(f"[{current_player}] Введите слово: ")

        if word == "!выход":
            print("Игра завершена.")
            break
        elif word == "!правила":
            print("Правила игры:")
            print("  - Игроки должны вводить слова по очереди.")
            print("  - Последняя буква предыдущего слова должна совпадать с первой буквой следующего слова.")
            print("  - Запрещено использовать ранее использованные слова.")
            print("  - Если последняя буква слова 'ь', 'й', 'ы' или 'ъ', следующее слово должно начинаться с предыдущей буквы.")
            continue

        if not is_word_valid(word):
            print("Слово недопустимо. Попробуйте снова.")
            continue

        used_words.append(word.lower())
        print(f"Игрок {current_player} ввел слово '{word}'.")
        change_turn()

    print("Игра завершена.")

# Запуск игры
play_game()