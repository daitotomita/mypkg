# ROS2 mypkg
[![test](https://github.com/daitotomita/robosys2023/actions/workflows/test.yml/badge.svg)](https://github.com/daitotomita/robosys2023/actions/workflows/test.yml)
  * ロボットシステム学2023の練習リポジトリ
##  talker & listener 
### 入力と実行結果
端末を2つ用意する
  * 端末1
```
$ ros2 run mypkg talker
```
  * 端末2
```
$ ros2 run mypkg listener
```
実行結果は以下の通りである
  * 端末2
```
[INFO] [1702987769.430848671] [listener]: Listen: 50
[INFO] [1702987769.864603575] [listener]: Listen: 51
[INFO] [1702987770.364476238] [listener]: Listen: 52
[INFO] [1702987770.864535967] [listener]: Listen: 53
[INFO] [1702987771.364151243] [listener]: Listen: 54
[INFO] [1702987771.864009347] [listener]: Listen: 55
[INFO] [1702987772.364514492] [listener]: Listen: 56
[INFO] [1702987772.864555855] [listener]: Listen: 57
[INFO] [1702987773.364942846] [listener]: Listen: 58
[INFO] [1702987773.864064285] [listener]: Listen: 59
[INFO] [1702987774.364653107] [listener]: Listen: 60
・・・
```

## 必要なソフトウェア
  * ROS2
  * Python
	* テスト済み: 3.7～3.10

## テスト環境
  * Ubuntu 20.04

## 著作権とライセンス
  *  このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
  *  このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
      * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
© 2023 Daito Tomita
