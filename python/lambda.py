# 関数型プログラミング
#   関数が他の変数と同じように値として扱われる
#     ラムダ関数
#       単一の小さい関数を作ればよく、完全に別個の関数を作成するほどではない場合に使う関数の簡略版

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#def f(person):
#    return person["name"]
# sortメソッドが内部的にリストpeopleの各要素をfに渡すのでfの引数を指定しなくても大丈夫
#people.sort(key=f)

# def f(person)を以下のようにlambdaで1行にできる。
people.sort(key=lambda person: person["name"])

print(people)
