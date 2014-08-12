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

print('READY')
sys.stdout.flush()

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
	for i in range({'W': 5, 'H': 2}[day]):
		# ここでロジック
		# 自分のプレイヤーナンバーは?
		# 期待値計算したい マイナスとプラス
		# 最も期待値が高いところに
		# command.append(str(random.randrange(numHeroines)))
		
		# ここでヒロインのIDを指定して出力
		heroineNum = cnt % 8
		cnt = cnt + 1
		command.append(str(heroineNum))
		

	print(' '.join(command))
	sys.stdout.flush()
