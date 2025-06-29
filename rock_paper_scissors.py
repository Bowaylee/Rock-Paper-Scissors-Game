import random



while True:

    tie=0
    win=0
    lose=0

    name=input("請輸入名字:")

    for i in range(1,4):

        while True:

            try:
                player=int(input("請輸入招式:"))
                if (player<1 or player>3):

                    print("已超出範圍，請重新輸入")

                else:
                    break

            except ValueError:
                print("只能輸入數字,1~3")

        computer=random.randint(1,3)

        player_move="未知"
        computer_move="未知"

        if player==1:
            player_move="剪刀"

        elif player==2:
            player_move="石頭"

        else:
            player_move="布"

        if computer==1:
            computer_move="剪刀"

        elif computer==2:
            computer_move="石頭"

        else:
            computer_move="布"


        if player==computer:
            print("平手"," 玩家動作:"+player_move+" 電腦動作:"+computer_move)
            tie+=1
        
        elif player==1:
            if computer==3:
                print("玩家勝利"," 玩家動作:"+player_move+" 電腦動作:"+computer_move)
                win+=1

            else:
                print("電腦勝利,玩家失敗"," 玩家動作:"+player_move+" 電腦動作:"+computer_move)
                lose+=1

        elif player==2:
            if computer==1:
                print("玩家勝利"," 玩家動作:"+player_move+" 電腦動作:"+computer_move)
                win+=1

            else:
                print("電腦勝利,玩家失敗"," 玩家動作:"+player_move+" 電腦動作:"+computer_move)
                lose+=1

        else:
            if computer==2:
                print("玩家勝利"," 玩家動作:"+player_move+" 電腦動作:"+computer_move)
                win+=1

            else:
                print("電腦勝利,玩家失敗"," 玩家動作:"+player_move+" 電腦動作:"+computer_move)
                lose+=1


    if (tie>win) and (tie>lose):
        print("最終平手,恭喜已完成遊戲!")
    elif (win>tie) and (win>lose):
        print("最終玩家獲勝,恭喜已完成遊戲!")

    elif (lose>tie) and (lose>win):
        print("最終電腦獲勝,再接再厲")
    else:
        print("最終一勝一負一平手,再接再厲")

    again=input("是否要再玩一次?")

    if again.lower()!="y":

        print("下次再來玩~~~")

        break