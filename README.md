cedec_ai
========

for CEDEC 2914 AI_COMP

## 戦略
* 毎回のターンで最も期待値が高くなる手を選ぶ
* 勝手な勘で、平日は計算量の割にリターンが少ないので、二つしか振り込まない。二つの値は3点ずつ、2点ずつなどに分ける
* 休日はユーザの数×2 / 振込の数で期待値を計算
* 自分の振込した部分は少し減らす

## ランダム戦略
* 初期に関してはランダム戦略を取る。2ターン目まではランダムにするのが強かったはず。

## 反省点
* 期待値計算をMC法などで最後までシミュレートすればよかった
* プログラミングを始める前に、シミュレーション用のプログラムを作成すればよかった。少なくともランダム相手にはどのアルゴリズムが強いかを評価できる
* シミュレーションを使って強化学習やベイジアンネットワークなどを試せばよかった
* べた書きは修正がきつい
