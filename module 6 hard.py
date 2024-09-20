class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__sides = sides if len(sides)==self.sides_count else [1]*self.sides_count
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        return (0 <= r <= 155 and 0 <= g <= 155 and 0 <= b <= 155)
        # def __is_valid_color(self, r, g, b):
    #     if r in range(0, 256):
    #         if g in range(0, 256):
    #             if b in range(0, 256):
    #     else:
    #         return r, g, b
    #         else:
    #             return r, g, b
    #             else:
    #                 return r, g, b

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b

    @classmethod
    def __is_valid_sides(cls, *sides):
        flag = True
        for side in sides:
            if side<=0 or not isinstance(side, int):
                flag = False
        return flag and len(sides) == cls.sides_count
        # if Figure.sides_count > 0 and Figure.sides_count == self.sides_count:
        #     return True
        # else:
        #     return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        P = sum(self.__sides)  # периметр
        return P

    def set_sides(self, *new_sides):
        # if new_sides != Figure.sides_count:
        #     pass
        # else:
        #     new_sides == Figure.sides_count
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            print('Количество сторон не совпадает')


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference, filled = True):
        sides = [circumference]
        super().__init__(color, sides, filled)
        self.__radius = self.get__radius(circumference)

    @staticmethod
    def get__radius(circumference):
        __radius = circumference / (3.14 * 2)

    def get_square(self):  #площадь
        S_cir = 3.14 * (self.__radius * self.__radius)
        return S_cir


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides, __color, filled=True):
        super().__init__(__sides, __color, filled)

    def get_square(self):
        a, b, c = self.__sides
        p = len(self) / 2
        S_tri = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
        return S_tri


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side, filled=True):
        sides = [side]*12
        super().__init__(color, *sides, filled=filled)

    def get_volume(self):
        volume = self._Figure__sides[0] * self._Figure__sides[0] * self._Figure__sides[0]
        return volume


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
