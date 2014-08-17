# -*- coding: utf-8 -*-

import sys
import random

class Heroine:
    def __init__(self, enthusiasm):
        self.enthusiasm = enthusiasm
        self.revealedLove = []
        self.myRealLove = 0

        # 最初に熱狂度順にソート
        # sortedEnthusiasm = sorted(self.enthusiasm)

def readLine():
    return list(map(int, raw_input().split()))

def getEstimation(_heroines, _numHeroines, enthusiasm, point, num):
    estimation = 0
    # 期待値出力
    # print(enthusiasm)
    # print(point)
    # print(num)
    for j in range(0, _numHeroines):
        value = 0
        if j == num:
            value = int(_heroines[j].myRealLove) + point
        else:
            value = int(_heroines[j].myRealLove)
        
        # 最下位のとき
        if min(_heroines[j].revealedLove) >= value:
            estimation = estimation + (-1 * enthusiasm[j])
        # 自分が一位のとき
        elif max(_heroines[j].revealedLove) <= value:
            # 追いつかれそうなときは追加したい
            estimation = estimation + enthusiasm[j]
        # それ以外
        else:
            pass
            # estimation += 0
    return estimation

    

print('READY')
sys.stdout.flush()

stepNum = 2

totalTurns, numPlayers, numHeroines = readLine()
enthusiasm = readLine()
heroines = []
cnt = 0
for i in range(numHeroines):
    heroines.append(Heroine(enthusiasm[i]))

for t in range(totalTurns):
    # ターン数と平日、休日の入力
    turn, day = raw_input().split()
    # ターンをintに変換
    turn = int(turn)

    # プレイヤーごとの好感度の配列
    for i in range(numHeroines):
        heroines[i].revealedLove = readLine()
    
    realLove = readLine()
    
    # 自分への好感度の配列
    for i in range(numHeroines):
        heroines[i].myRealLove = realLove[i]
    
    if day == 'W':
        dated = readLine()
    else:
        dated = [0] * numHeroines

    command = []
    output = []

    out = heroines[0].revealedLove
    out.append(3)
    
    # 期待値
    # トータルの期待値
    estimate = 0

    # ヒロインそれぞれの期待値配列
    estimateArray = [0] * numHeroines
    
    length = 5
    point = 1
    if day == 'H':
        length = 2
        point = 2

    
    # 
    if stepNum == 1:
        pass
    # パターンを分ける 全部同じのに振る、4つ振る
    else:
        estimationMax = []
        voteArray = []
        # フリの回数
        num = length
        # for cnt in range(0, 1):
        # num = num - cnt
        # 紐づいた振り込みかた
        maxEstimation = -100000

        # if (turn > 0):
        tmpArray = heroines
        # for var in range(1, length):
        # 投票する番号
        vote = -100
        # 期待値がマイナスの可能性もあるので
        maxVal = -10000
        for k in range(0, numHeroines):
            # 期待値を計算 振り込む数をポイントにかけて期待値計算
            estimateArray[k] = getEstimation(tmpArray, numHeroines, enthusiasm, point * num, k)
            # print estimateArray[k]
            # print k

            if estimateArray[k] > maxVal:
                maxVal = estimateArray[k]
                vote = k

        # print maxVal
        # print vote
        estimationMax.append(maxVal)
        voteArray.append(vote)

        estMax = -100000
        finalVote = -100
        for estNum in range(0,len(estimationMax)):
            # print estimationMax[estNum]
            if estimationMax[estNum] > estMax:
                maxVal = estimationMax[estNum]
                finalVote = voteArray[estNum]

        output = [finalVote] * length
    
    # 配列の長さが足りない場合は適当に足す
    while len(output) <= length:
        output.append(random.randrange(numHeroines))

    for i in range({'W': 5, 'H': 2}[day]):
        # ここでロジック
        # 自分のプレイヤーナンバーは?
        # 期待値計算したい マイナスとプラス
        # 最も期待値が高いところに
        # command.append(str(random.randrange(numHeroines)))
        
        # ここでヒロインのIDを指定して出力
        heroineNum = cnt % 8
        cnt = cnt + 1
        command.append(str(output[i]))
        

    print(' '.join(command))
    sys.stdout.flush()
