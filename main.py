print("Students")
class Students:
    group = "C2011"
    education = "IT_STEP"
    role = "student"
    def __init__(self, name, age, great):
        self.name = name
        self.age = age
        self.great = great


st = Students(name="Anna", age="13", great="8")
print(f"st= {st.name} {st.age} {st.great} {st.group}")

st1 = Students(name="Maxim", age="14", great="6")
print(f"st1= {st1.name} {st1.age} {st1.great} {st1.group}")

st2 = Students(name="Sasha", age="13", great="11")
print(f"st2= {st2.name} {st2.age} {st2.great} {st2.group}")

print("_____________________________")
print("Teachers")
class Teachers:
    education = "IT STEP"
    group = "C2011"
    пол = "мужской"

    def __init__(self, name, lesson, helpful):
        self.name = name
        self.lesson = lesson
        self.helpful = helpful

tchr = Teachers(name="Кеба Евгений", lesson="python", helpful="11/10")
print(f"tchr= {tchr.name} {tchr.group} {tchr.lesson} {tchr.helpful} {tchr.пол}")

tchr1 = Teachers(name="Русецкий Андрей", lesson="CupCut", helpful="9/10")
print(f"tchr1= {tchr1.name} {tchr1.group} {tchr1.lesson} {tchr1.helpful} {tchr1.пол}")

tchr2 = Teachers(name="Рыжов Константин", lesson="BBC Micro:bit", helpful="8.5/10")
print(f"tchr2= {tchr2.name} {tchr2.group} {tchr2.lesson} {tchr2.helpful} {tchr2.пол}")