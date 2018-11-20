class User():
    species = "영장류"
    def __init__(self, name, gender): #인스턴스 메서드의 경우 항상 self인자를 첫인자로
        self.name = name
        self.gender = gender

    def get_user_info(self): 
        return "이름 : " + self.name + "\n성별 : " + self.gender 
       

    @classmethod #해당 메서드가 클래스 메서드임을 표시, 클래스메서드는 cls가 항상 첫인자
    def get_species(cls):
        return "사람은 모두" + cls.species + "이다."



user = User("조아라", "여자")
print("====user.py====")
print(user.get_species())
print(user.get_user_info())