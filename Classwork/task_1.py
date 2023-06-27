players = ["Игрок 1", "Игрок 2"]
used_words = ["Лак"]

def is_word_valid(used_words, new_word):
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
    print("Введите '!правила' для получения правил игры.")
    print("Введите '!выход' для завершения игры.")
    print()

    while True:
        word = input(f"[Player1] Введите слово: ")
        is_word_valid(used_words, word)
        used_words.append(word)
        print(f"Игрок ввел слово '{word}'.")
        word = input(f"[Player2] Введите слово: ")
        is_word_valid(used_words, word)
        used_words.append(word)
        print(f"Игрок ввел слово '{word}'.")

        if word == "!выход":
            print("Игра завершена.")
            break
        elif word == "!правила":
            print("Правила игры:")
            print("  - Игроки должны вводить слова по очереди.")
            print("  - Последняя буква предыдущего слова должна совпадать с первой буквой следующего слова.")
            print("  - Запрещено использовать ранее использованные слова.")
            print("  - Если последняя буква слова 'ь', 'й', 'ы' или 'ъ', следующее слово должно начинаться с предыдущей буквы.")
            print()
            continue

    print("Игра завершена.")


play_game()