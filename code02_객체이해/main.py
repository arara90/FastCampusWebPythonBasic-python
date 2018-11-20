class Cat():
    species = "russian blue"

    def __init__(self, name): #()가 붙은 method 선언할 때 사용
        self.name = name      #인스턴스 객체의 속성 name에 인자로 넘어온 name할당
        print("생성자호출!")

cat1 = Cat("냥1") # 객체가 생성될 때 init 생성자 자동으로 호출
cat2 = Cat("냥2") 

print(cat1.species)
print(cat2.species)

print(cat1.name)
print(cat2.name)
