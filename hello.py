from datetime import datetime

s = input("お名前を入力してください")
y = int(input(f"こんにちは、{s}さん！年は何歳ですか？"))

# Pythonが誕生(1991)してからの年数を取得
py = datetime.now().year - 1991

if(y == py):
  print("へぇー、同い年ですね！")
elif(y < py):
  print("へぇー、若いですね！")
else:
  print("わたしより年上なんですね！")

input("何かキーを押すと終了します")