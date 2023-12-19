# ROS2 mypkg
[![test](https://github.com/daitotomita/robosys2023/actions/workflows/test.yml/badge.svg)](https://github.com/daitotomita/robosys2023/actions/workflows/test.yml)
  * ロボットシステム学2023の練習リポジトリ
##  talker & listener
### ノードの説明
 * talker
	* countupを通じて16ビットの符号付き整数のメッセージを送信する
 * listener
	* countupからメッセージをもらって表示する
 
### 入力
端末を2つ用意する
  * 端末1
```
$ ros2 run mypkg talker
```
  * 端末2
```
$ ros2 run mypkg listener
```
### 実行結果
  * 端末2
```
$ ros2 run mypkg listener
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

## launchファイル
### ノードの説明
  * 複数のノードを一度に立ち上げるもの
### 入力
```
$ ros2 launch mypkg talk_listen.launch.py
```
### 実行結果
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/benzen0829/.ros/log/2023-12-19-21-45-08-600047-benzen-315
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [317]
[INFO] [listener-2]: process started with pid [319]
[listener-2] [INFO] [1702989909.522447086] [listener]: Listen: 0
[listener-2] [INFO] [1702989910.013168361] [listener]: Listen: 1
[listener-2] [INFO] [1702989910.512465711] [listener]: Listen: 2
[listener-2] [INFO] [1702989911.012568964] [listener]: Listen: 3
[listener-2] [INFO] [1702989911.512992526] [listener]: Listen: 4
[listener-2] [INFO] [1702989912.012918013] [listener]: Listen: 5
[listener-2] [INFO] [1702989912.513078479] [listener]: Listen: 6
[listener-2] [INFO] [1702989913.012894008] [listener]: Listen: 7
[listener-2] [INFO] [1702989913.513031761] [listener]: Listen: 8
[listener-2] [INFO] [1702989914.012862938] [listener]: Listen: 9
[listener-2] [INFO] [1702989914.512864601] [listener]: Listen: 10
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
