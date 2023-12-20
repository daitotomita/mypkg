# ROS2 mypkg
[![test](https://github.com/daitotomita/robosys2023/actions/workflows/test.yml/badge.svg)](https://github.com/daitotomita/robosys2023/actions/workflows/test.yml)
  * ロボットシステム学2023の練習用リポジトリ
##  talker & listener
### 説明
 * トピック
	* 今回は/countupというトピックを使用している
 * talker
	* 数字をカウントして/countupを通じてInt16という型のメッセージを送信するノード
 * listener
	* /countupからメッセージを受け取りその整数が素数であるかを判定するノード
 
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
[INFO] [listener]: Listen: 10 合成数
[INFO] [listener]: Listen: 11 素数
[INFO] [listener]: Listen: 12 合成数
[INFO] [listener]: Listen: 13 素数
[INFO] [listener]: Listen: 14 合成数
[INFO] [listener]: Listen: 15 合成数
[INFO] [listener]: Listen: 16 合成数
[INFO] [listener]: Listen: 17 素数
[INFO] [listener]: Listen: 18 合成数
[INFO] [listener]: Listen: 19 素数
[INFO] [listener]: Listen: 20 合成数
・・・
```

## launchファイル
### 説明
  * 複数のノードを一度に立ち上げるノード
### 入力
```
$ ros2 launch mypkg talk_listen.launch.py
```
### 実行結果
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/benzen0829/.ros/log/2023-12-21-00-10-12-347990-benzen-7229
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [7231]
[INFO] [listener-2]: process started with pid [7233]
[listener-2] [INFO] [listener]: Listen: 0 合成数
[listener-2] [INFO] [listener]: Listen: 1 合成数
[listener-2] [INFO] [listener]: Listen: 2 素数
[listener-2] [INFO] [listener]: Listen: 3 素数
[listener-2] [INFO] [listener]: Listen: 4 合成数
[listener-2] [INFO] [listener]: Listen: 5 素数
[listener-2] [INFO] [listener]: Listen: 6 合成数
[listener-2] [INFO] [listener]: Listen: 7 素数
[listener-2] [INFO] [listener]: Listen: 8 合成数
[listener-2] [INFO] [listener]: Listen: 9 合成数
[listener-2] [INFO] [listener]: Listen: 10 合成数
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
  *  このパッケージのコードは、下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）の一部のものを加筆し、本人の許可を得て自身の著作としたものです。
      * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

© 2023 Daito Tomita
