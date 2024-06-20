import random

def create_deck():
    suits = ['ハート', 'ダイヤ', 'クラブ', 'スペード']#aaaaa
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'スート': suit, 'ランク': rank} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        rank = card['ランク']
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            ace_count += 1
            value += 11
        else:
            value += int(rank)
    
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    
    return value

def display_hand(hand, name):
    print(f"{name}の手札: " + ", ".join([f"{card['スート']}の{card['ランク']}" for card in hand]))

def blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("ブラックジャックへようこそ！")
    display_hand(player_hand, "プレイヤー")
    print(f"ディーラーの手札: {dealer_hand[0]['スート']}の{dealer_hand[0]['ランク']} と [伏せ札]")

    while calculate_hand_value(player_hand) < 21:
        action = input("ヒットしますか？スタンドしますか？ (h/s): ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            display_hand(player_hand, "プレイヤー")
        elif action == 's':
            break
        else:
            print("無効な入力です。h か s を入力してください。")

    player_value = calculate_hand_value(player_hand)
    if player_value > 21:
        print("バーストしました！ディーラーの勝ちです。")
        return

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    display_hand(dealer_hand, "ディーラー")
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("おめでとうございます！プレイヤーの勝ちです。")
    elif player_value < dealer_value:
        print("ディーラーの勝ちです。")
    else:
        print("引き分けです。")

if __name__ == "__main__":
    blackjack()