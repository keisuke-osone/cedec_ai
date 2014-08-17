# -*- coding: utf-8 -*-

import copy
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
    # revealedLoveArray = [0] * 

    for j in range(0, _numHeroines):
        value = 0
        if j == num:
            value = int(_heroines[j].myRealLove) + point
        else:
            value = int(_heroines[j].myRealLove)
        
        # 最下位のとき
        if min(_heroines[j].revealedLove) >= value:
            minNum = _heroines[j].revealedLove.count(value)
            if minNum > 1:
                estimation = (estimation + (-1 * enthusiasm[j])) / minNum
            else: 
                estimation = (estimation + (-1 * enthusiasm[j]))
        # 自分が一位のとき
        elif max(_heroines[j].revealedLove) <= value:
            maxNum = _heroines[j].revealedLove.count(value)
            # 追いつかれそうなときは追加したい
            if maxNum > 1:
                estimation = (estimation + enthusiasm[j]) / maxNum
            else:
                estimation = (estimation + enthusiasm[j])
        # それ以外
        else:
            pass
            # estimation += 0
    # print estimation
    return estimation

#  休日を考慮
def getEstimationWithHolidayDate(_heroines, _numHeroines, dated, enthusiasm, point, num):
    estimation = 0
    estimationWithHolidayDate = 0
    
    # print u"振込" + str(num)
    # print u"振込" + str(point)
    for j in range(0, _numHeroines):
        # print u"ヒロイン:" + str(j)

        value = 0
        if j == num:
            value = int(_heroines[j].myRealLove) + point
        else:
            value = int(_heroines[j].myRealLove)
        
        # 休日考慮なし
        # 最下位のとき
        # print value
        # print min(_heroines[j].revealedLove)
        # print max(_heroines[j].revealedLove)
        if min(_heroines[j].revealedLove) >= value:
            minNum = _heroines[j].revealedLove.count(value)
            if minNum > 1:
                estimation = float(estimation + (-1 * enthusiasm[j])) / minNum
            else: 
                estimation = float(estimation + (-1 * enthusiasm[j]))
            # print u"最下位" + float(estimation + (-1 * enthusiasm[j]))
        # 自分が一位のとき
        elif max(_heroines[j].revealedLove) <= value:
            maxNum = _heroines[j].revealedLove.count(value)
            # 追いつかれそうなときは追加したい
            if maxNum > 1:
                estimation = float(estimation + enthusiasm[j]) / maxNum
            else:
                estimation = float(estimation + enthusiasm[j])
        # それ以外
        else:
            pass

        # 休日考慮あり
        # 最下位のとき
        # print float(min(_heroines[j].revealedLove) + dated[j])
        # print float(max(_heroines[j].revealedLove) + dated[j])
        # estimationWithHolidayDate = 0.0
        if float(min(_heroines[j].revealedLove)) + dated[j] >= value:
            minNum = _heroines[j].revealedLove.count(value)
            if minNum > 1:
                estimationWithHolidayDate += float((-1 * enthusiasm[j])) / minNum
            else: 
                estimationWithHolidayDate += float((-1 * enthusiasm[j]))
            # print u"最下位" + str(-1 * enthusiasm[j])
        # 自分が一位のとき
        elif float(max(_heroines[j].revealedLove)) + dated[j] <= value:
            maxNum = _heroines[j].revealedLove.count(value)
            # 追いつかれそうなときは追加したい
            if maxNum > 1:
                estimationWithHolidayDate += float(enthusiasm[j]) / maxNum
            else:
                estimationWithHolidayDate += float(enthusiasm[j])
            # print u"首位" + str(enthusiasm[j])
        # それ以外
        else:
            pass
            # estimation += 0
        # print u"累積" + str(estimationWithHolidayDate)
    # print u"休日なし" + str(estimation)
    # print u"休日あり" + str(estimationWithHolidayDate)

    return estimationWithHolidayDate

    

print('READY')
sys.stdout.flush()

stepNum = 2

totalTurns, numPlayers, numHeroines = readLine()
enthusiasm = readLine()
heroines = []
cnt = 0
datedEstimation = [0] * numHeroines

for i in range(numHeroines):
    heroines.append(Heroine(enthusiasm[i]))

for t in range(totalTurns):

    # ターン数と平日、休日の入力
    turn, day = raw_input().split()
    # ターンをintに変換
    turn = int(turn)
    # 出力
    output = []

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

    # デートの配列の配列
    otherDated = copy.deepcopy(dated)
    for i in range(0, len(datedEstimation)):
        if len(output) == 2:
            for j in range(0, len(output)):
                if otherDated[output[j]] == 1:
                    if otherDated.count(max(otherDated)) == numPlayers * 2:
                        otherDated[output[j]] == 0.0
                    else:
                        otherDated[output[j]] == 0.5

        datedEstimation[i] += float(otherDated[i] * numPlayers * 2) / otherDated.count(max(otherDated))

    # print "1の数"
    # print dated.count(max(dated))
    # print "期待値"
    # print float(numPlayers * 2) / dated.count(max(dated))

    command = []
    
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

    
    outputArray = []
    outputEstimationArray = []

    estimationMax = []
    voteArray = []
    # フリの回数
    # num = length
    for cnt2 in range(0, length):
        # print cnt
        num = length - cnt2
        # print num
        # 紐づいた振り込みかた
        maxEstimation = -100000

        tmpArray = []
        tmpArray = copy.deepcopy(heroines)
        # 投票する番号
        vote = -100
        # 期待値がマイナスの可能性もあるので
        maxVal = -10000
        for k in range(0, numHeroines):
            # 期待値を計算 振り込む数をポイントにかけて期待値計算
            # estimateArray[k] = getEstimation(tmpArray, numHeroines, enthusiasm, point * num, k)
            estimateArray[k] = getEstimationWithHolidayDate(tmpArray, numHeroines, datedEstimation, enthusiasm, point * num, k)
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

        output = [finalVote] * num
        # print output
        for input in range(0, len(output)):
            tmpArray[output[input]].myRealLove += point

        length1 = length - len(output)
        for cnt1 in range(0, length1):
            # 紐づいた振り込みかた
            maxEstimation = -100000

            # if (turn > 0):
            # tmpArray = heroines
            # for var in range(1, length):
            # 投票する番号
            vote = -100
            # 期待値がマイナスの可能性もあるので
            maxVal = -10000
            for k in range(0, numHeroines):
                # 期待値を計算 振り込む数をポイントにかけて期待値計算
                # estimateArray[k] = getEstimation(tmpArray, numHeroines, enthusiasm, point * length1, k)
                estimateArray[k] = getEstimationWithHolidayDate(tmpArray, numHeroines, datedEstimation, enthusiasm, point * length1, k)

                if estimateArray[k] > maxVal:
                    maxVal = estimateArray[k]
                    vote = k

            estimationMax.append(maxVal)
            voteArray.append(vote)

        estMax = -100000
        finalVote = -100
        for estNum in range(0,len(estimationMax)):
            # print estimationMax[estNum]
            if estimationMax[estNum] >= estMax:
                estMax = estimationMax[estNum]
                finalVote = voteArray[estNum]
        # print maxVal
        out2 = [finalVote] * cnt2
        for l in range(0, len(out2)):
            output.append(out2[l])

        outputEstimationArray.append(estMax)
        outputArray.append(output)

    # 戦略の決定
    # print outputArray
    # print outputEstimationArray

    finalOutput = []
    maxOutputEstimation = -100000
    for m in range(0, len(outputEstimationArray)):
        if outputEstimationArray[m] > maxOutputEstimation:
            maxOutputEstimation = outputEstimationArray[m]
            finalOutput = outputArray[m]

    output = finalOutput
    
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
        # heroineNum = cnt % 8
        # cnt = cnt + 1
        # print output
        if (turn > 1):
            command.append(str(output[i]))
        else:
            command.append(str(random.randrange(numHeroines)))
        

    print(' '.join(command))
    sys.stdout.flush()
