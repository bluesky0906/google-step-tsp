# Google STEP 2020: Travelling Salesman Problem Challenges

Originally By: [Hayato Ito](https://github.com/hayatoito) (hayato@google.com)  
2020 Version By: [Hugh O'Cinneide](https://github.com/hkocinneide)
(hughoc@google.com)

Answered By: Sora Tagami

## How to run
```shell
python output_generator.py
```
- NN
- DNN
- NN_2opt
- DNN_2opt
- NN_comb1
- DNN_comb1
- NN_comb2

のうちから実行するファイルを選ぶ。
my_output/ 以下にoutputファイルができる。

## How to verify
```shell
python my_output_verifier.py
```
CHALLENGEごとのスコアが表示され、一番いいスコアのファイルがvisualizeされるようになる。

## 近似アルゴリズム
### 1. NN (NearestNeighbor) 法
sampleのgreedyと同じで

- 適当な都市を選び、出発点とする
- すべての都市を訪問するまで以下を繰り返す
  - まだ来訪間の都市で、現在いる都市から最も近い都市を選ぶ 
  - 視在いる都市と選んだ都市を接続し、選んだ都市に移動する
- 現在いる都市と出発点を接続する

### 2. DNN (DivisionNearestNeighbor) 法
参考文献1で改善法にかかりやすいと記述があったので採用した。
- 最も距離の離れた・2都市(Sl),(S2)を選択する
- (S1),(S2)を通る直線で都市群を2つのグループ【G1】,【G2】に分ける。ただし(S1), (S2)はどちらに も属さない
- (Sl)を開始都市として、【G1】に対してNN法を行う 
- グループ【G1】で最後に訪問した都市と(S2)を結ぶ
- (S2)を開始都市として、【G2】に対してNN法を行う 
- グループ【G2】で最後に訪問した都市と(S1)を結ぶ



## 改善アルゴリズム
### 1. 2-opt法
- 以下を経路が改善されなくなるまで繰り返す
  - 2つの辺AB, CDを考える
  - AB + CD よりも AC + BDの方が短ければ
  - BとCを入れ替える


### 2. or-opt法
- 以下を経路が改善されなくなるまで繰り返す
  - ある都市Aを考える
  - 他の辺BCに挿入したとき経路が改善されるならば
  - AをBCの間に挿入する

####注釈
- これの計算改善法として参考文献2にて記されていたので実装はしたが、どれほど計算速度があがるかは検証していない。

- 参考文献1にて1.5-opt法が提案されているが、これはor-opt法と「経路が改善された」ことの評価方法が異なるだけであったので、実装しなかった。



## 結果
- NN法は0~5までは全ての点をスタート地点にして一番短い経路を採用した。
- comb1は NN/DNN + 2-opt法の結果に対してor-opt法を適用した。
- comb2は、全てのスタート地点からのNN + 2-opt法の結果に対してor-opt法を適用し、一番短い経路を採用した。
- 空白の欄はまだ結果が出ていない。

|            |Challenge 0 |Challenge 1 |Challenge 2 |Challenge 3 |Challenge 4 |Challenge 5 |Challenge 6 |
|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
|NN          |3418.10     |3832.29     |5065.58     |9276.22     |12084.32    |24191.66    |47822.41    |
|DNN         |3858.81     |3942.55     |5106.22     |11066.65    |12323.86    |25856.02    |53335.42    |
|NN_2opt     |**3291.62** |3832.29     |4494.42     |8256.55     |10885.95    |20932.86    |**42176.22**|
|DNN_2opt    |**3291.62** |3832.29     |5069.50     |8990.86     |11089.48    |21598.66    |42874.53    |
|NN_comb1    |**3291.62** |**3778.72** |**4494.42** |**8164.16** |10693.81    |**20724.24**|            |
|DNN_comb1   |**3291.62** |**3778.72** |**4494.42** |8840.42     |10882.45    |21101.61    |            |
|NN_comb2    |**3291.62** |**3778.72** |**4494.42** |**8164.16** |**10680.10**|            |            |


## 考察
- NN_comb1とNN_comb2の結果がCHALLENGE4から違うということから、NN法で最適である経路を2-opt法とor-opt法で改善するよりも、NN法を適用した段階では長い経路になってしまっていた経路を改善した方が最終的に良い結果になることがあるとわかる。
- DNNはNNに比べ、スタート位置を変えない分高速であるが、CHALLENGE3からはスコアが落ちてしまう。
  - 参考文献1では改善法にかかりやすいとあり、そこで実装している改善法と2-opt法+or-opt法は似た実装であったが、必ずしも上がるわけではないということがわかる。


## 参考文献
#### 巡回セールスマン問題の近似アルゴリズムについて
https://mie-u.repo.nii.ac.jp/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=5071&item_no=1&page_id=13&block_id=21

#### 球面上における巡回セールスマン問題ソルバーの開発と評価
https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=161620&item_no=1&page_id=13&block_id=8