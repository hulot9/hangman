# 自作
"""
def hangman(answer):
    hangman = ["",
               "--------        ",
               "        |       ",
               "        |       ",
               "        O       ",
               "       /|\      ",
               "       / \      ",
               "                ",
               ]
    count = 0
    word_list = list(word)
    blinds = ["_"] * len(word)
    while count < 8:
        if "_" not in blinds:
            print("あなたの勝ち!", "正解は \"{}\" .".format(word))
            break

        challenge = input("アルファベットを1文字、入力してください: ")
        for index, char in enumerate(word_list):
            if char == challenge:
               blinds[index] = challenge
               word_list[index] = "*"
               break
        else:
            count += 1

        print("\n", "".join(blinds))
        print("\n".join(hangman[:wrong+1]))
    if wrong >= 8:
        print("あなたの負け!", "正解は \"{}\" .".format(word))

word = input("好きな単語をアルファベットで入力してください: ")
hangman(word)
"""


# 解答
import random

def hangman():
    ans_list = ["Python", "Java", "PHP", "Perl", "Ruby"]
    word = random.choice(ans_list)
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|       |       ",
              "|       O       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "
              ]
    rletters = list(word.lower())
    board = ["_"]*len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages)-1:
      print("\n")
      msg = "1文字を予想してね: "
      char = input(msg)
      if char in rletters:
          cind = rletters.index(char)
          board[cind] = char
          rletters[cind] = "$"
      else:
          wrong += 1
      print(" ".join(board))
      e = wrong + 1
      print("\n".join(stages[0:e]))
      if "_" not in board:
          print("\n")
          print("あなたの勝ち！")
          print(word)
          win = True
          break
    if not win:
        print("\n")
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {} 。".format(word))

hangman()


# チャレンジ
"""
import random

ans_list = ["Python", "Charo", "TangeSazen", "Okuwamura", "Swagtail"]
answer = random.choice(ans_list)
hangman(answer)
"""
