"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""


class Rhombus(object):
    class_name = "Rhombus"

    def __init__(self, side_a, angle_a=None, angle_b=None):
        self.side_a = side_a
        if angle_a is not None and angle_b is not None:
            if angle_a + angle_b != 180:
                raise ValueError("Сумма углов должна быть 180")
            self.angle_a = angle_a

        elif angle_a is not None:
            self.angle_a = angle_a
        elif angle_b is not None:
            self.angle_b = angle_b
        else:
            raise ValueError("Должен быть указан хотя бы один угол")

    def __setattr__(self, name, value):
        if name == "side_a":
            if not isinstance(value, (int, float)):
                raise TypeError("Сторона должна быть числом")
            if value <= 0:
                raise ValueError("Сторона должна быть больше 0")
            object.__setattr__(self, "side_a", float(value))
            return

        elif name == "angle_a":

            if not isinstance(value, (int, float)):
                raise TypeError("Угол должен быть числом")
            if not 0 < value < 180:
                raise ValueError("Угол должен быть в диапазоне (0, 180)")
            object.__setattr__(self, "angle_a", value)
            object.__setattr__(self, "angle_b", 180 - value)
            return

        elif name == "angle_b":

            if not isinstance(value, (int, float)):
                raise TypeError("Угол должен быть числом")
            if not 0 < value < 180:
                raise ValueError("Угол должен быть в диапазоне (0, 180)")
            object.__setattr__(self, "angle_b", value)
            object.__setattr__(self, "angle_a", 180 - value)
            return

        object.__setattr__(self, name, value)


