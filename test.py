class person():
    name = "姓名"
    age = "年龄"
    gender = "性别"
    weight = "体重"

    def __init__(self, name, age, gender, weight):
        print("初始化")
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    @classmethod
    def eat(self):
        print("喜欢吃")

    def drink(self):
        print("喜欢喝")

    def play(self):
        print("喜欢玩")


zs = person("张三", 65, "男", 190)
print(zs.name, zs.age, zs.gender, zs.weight)
zs.eat()
person.eat()

print(person.name)
person.name = "王五"
print(person.name)
print(zs.name)
zs.name = "李四"
print(zs.name)
