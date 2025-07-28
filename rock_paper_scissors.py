import random

choices = {1: "剪刀", 2: "石頭", 3: "布"}

def get_user_choice():
    while True:
        try:
            user = int(input("請輸入招式:1.剪刀 2.石頭 3.布: "))
            if user in choices:
                return user
            else:
                print("請重新輸入 1,2,3")
        except ValueError:
            print("請重新輸入 1,2,3")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user, computer):
    if user == computer:
        return "平手"
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        return "玩家"
    else:
        return "電腦"

def print_round_result(user, computer, winner):
    print(f"玩家出：{choices[user]}, 電腦出：{choices[computer]}")
    if winner == "平手":
        print("結果: 平手\n")
    else:
        print(f"結果: {winner} 贏!\n")

def print_final_result(scores):
    print("=== 最終戰績 ===")
    print(f"玩家勝利: {scores['玩家']} 次")
    print(f"電腦勝利: {scores['電腦']} 次")
    print(f"平手次數: {scores['平手']} 次")

    if scores["玩家"] > scores["電腦"]:
        print("恭喜玩家贏！")
    elif scores["玩家"] < scores["電腦"]:
        print("恭喜電腦贏！")
    else:
        print("雙方平手！")

def play_game(round=3):
    scores = {"玩家": 0, "電腦": 0, "平手": 0}
    print("=== 歡迎來到剪刀石頭布 ===")

    for _ in range(round):
        user = get_user_choice()
        computer = get_computer_choice()
        winner = determine_winner(user, computer)
        print_round_result(user, computer, winner)
        scores[winner] += 1

    print_final_result(scores)

if __name__ == "__main__":
    play_game()
