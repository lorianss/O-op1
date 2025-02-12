import math


class Vector3D:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        """
        Инициализация объекта Vector3D.
        :param x: координата x (float).
        :param y: координата y (float).
        :param z: координата z (float).
        """
        if not all(isinstance(coord, (int, float)) for coord in [x, y, z]):
            raise ValueError("Координаты вектора должны быть числами.")

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def read(self):
        """
        Ввод значений координат вектора с клавиатуры.
        """
        try:
            self.x = float(input("Введите координату x: "))
            self.y = float(input("Введите координату y: "))
            self.z = float(input("Введите координату z: "))
        except ValueError:
            print("Ошибка ввода. Проверьте, что введены корректные значения.")
            raise

    def display(self):
        """
        Вывод координат вектора на экран.
        """
        print(f"Vector3D(x={self.x}, y={self.y}, z={self.z})")

    def __add__(self, other):
        """
        Сложение двух векторов.
        :param other: другой вектор (Vector3D).
        :return: новый вектор (Vector3D).
        """
        if not isinstance(other, Vector3D):
            raise TypeError("Операнд должен быть объектом класса Vector3D.")
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        Вычитание двух векторов.
        :param other: другой вектор (Vector3D).
        :return: новый вектор (Vector3D).
        """
        if not isinstance(other, Vector3D):
            raise TypeError("Операнд должен быть объектом класса Vector3D.")
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot_product(self, other):
        """
        Скалярное произведение двух векторов.
        :param other: другой вектор (Vector3D).
        :return: скалярное произведение (float).
        """
        if not isinstance(other, Vector3D):
            raise TypeError("Операнд должен быть объектом класса Vector3D.")
        return self.x * other.x + self.y * other.y + self.z * other.z

    def multiply_by_scalar(self, scalar: float):
        """
        Умножение вектора на скаляр.
        :param scalar: скаляр (float).
        :return: новый вектор (Vector3D).
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Скаляр должен быть числом.")
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def length(self):
        """
        Вычисление длины вектора.
        :return: длина вектора (float).
        """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __eq__(self, other):
        """
        Сравнение двух векторов на равенство.
        :param other: другой вектор (Vector3D).
        :return: True, если векторы равны, иначе False.
        """
        if not isinstance(other, Vector3D):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def compare_length(self, other):
        """
        Сравнение длин двух векторов.
        :param other: другой вектор (Vector3D).
        :return: 1, если длина текущего вектора больше; -1, если меньше; 0, если равны.
        """
        if not isinstance(other, Vector3D):
            raise TypeError("Операнд должен быть объектом класса Vector3D.")
        len_self = self.length()
        len_other = other.length()
        if len_self > len_other:
            return 1
        elif len_self < len_other:
            return -1
        else:
            return 0


if __name__ == '__main__':
    # Демонстрация работы класса Vector3D
    print("Создание двух векторов:")
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    v1.display()
    v2.display()

    print("\nСложение векторов:")
    v_sum = v1 + v2
    v_sum.display()

    print("\nВычитание векторов:")
    v_diff = v1 - v2
    v_diff.display()

    print("\nСкалярное произведение векторов:")
    dot = v1.dot_product(v2)
    print(f"Скалярное произведение: {dot}")

    print("\nУмножение вектора на скаляр:")
    scalar = 2
    v_scaled = v1.multiply_by_scalar(scalar)
    v_scaled.display()

    print("\nДлина вектора:")
    print(f"Длина v1: {v1.length()}")
    print(f"Длина v2: {v2.length()}")

    print("\nСравнение векторов:")
    print(f"v1 == v2: {v1 == v2}")

    print("\nСравнение длин векторов:")
    comparison = v1.compare_length(v2)
    if comparison == 1:
        print("Длина v1 больше длины v2")
    elif comparison == -1:
        print("Длина v1 меньше длины v2")
    else:
        print("Длины векторов равны")

    print("\nВвод вектора с клавиатуры:")
    v3 = Vector3D()
    try:
        v3.read()
        v3.display()
    except ValueError:
        print("Ошибка при вводе данных.")