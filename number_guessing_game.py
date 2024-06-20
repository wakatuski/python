import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("1から100までの数を当ててください。")

    while True:
        guess = int(input("あなたの予想: "))
        attempts += 1

        if guess < number_to_guess:
            print("もっと大きい数です。")
        elif guess > number_to_guess:
            print("もっと小さい数です。")
        else:
            print(f"おめでとうございます！{attempts}回で当たりました。")
            break

if __name__ == "__main__":
    number_guessing_game()