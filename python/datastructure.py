# list(他の言語で言う配列)
# 値が変更可能な2つ以上の値をもつグループとしての用途が多い
print("!!!!!!!!!!!!!!list!!!!!!!!!!!!!!")

names = ["Harry", "Ron", "Hermione", "Ginny"]

print(names)
print(names[0])

names.append("Draco")
names.sort()
print(names)

# tuple
# 値が変わらない2つ以上の値をもつグループとしての用途が多い
print("!!!!!!!!!!!!!!tuple!!!!!!!!!!!!!!")
coordinate = (10.0, 20.0)
print(coordinate)
print(coordinate[1])

# set
# 同じ値が存在してはだめ
# 順序を気にせず1度しか出てこない場合に
print("!!!!!!!!!!!!!!set!!!!!!!!!!!!!!")

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) #これは表示されない。既に存在するので。
print(s)

s.remove(2)
print(s)
print(f"The set has {len(s)} elements.")


# dict
# キー/バリュー
print("!!!!!!!!!!!!!!dict!!!!!!!!!!!!!!")
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])
houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])


# listの中の各要素をdictにすることもできる
# listの中にlist,dictの中にlistなども可能
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]
