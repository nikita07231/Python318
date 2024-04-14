class Auto:
    def __init__(self, md, god, pro, mos, color, many):
        self.md = md
        self.god = god
        self.pro = pro
        self.mos = mos
        self.color = color
        self.many = many

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.md}\nГод выпуска: {self.god}\nПроизводитель: {self.pro}\n"
              f"Мощность двигателя: {self.mos}\nЦвет машины: {self.color}\nЦена: {self.many}")
        print("=" * 40)

    def set_name(self, md):
        self.md = md

    def get_name(self):
        return self.md


a = Auto("X7 M50i", 2021, "BMW", "530 л. с.", "white", 10790000)
a.print_info()