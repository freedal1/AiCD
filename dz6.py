#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 25
class IntegerVector: #целочисленный вектор фиксированной размерности
    def __init__(self, dimension, coordinates):
        self.dimension = dimension #размерность вектора
        self.coordinates = coordinates #координаты вектора

    def compare(self, other_vector): #Метод compare сравнивает два вектора на равенство по координатам
        return self.coordinates == other_vector.coordinates #сравнение текущего вектора с другим

    def length(self):
        return sum(coord ** 2 for coord in self.coordinates) ** 0.5 #вычисляет длину вектора по евклидовой норме

# Пример использования
vector1 = IntegerVector(3, [1, 2, 3])
vector2 = IntegerVector(3, [1, 2, 4])

print(vector1.compare(vector2))  # True
print(vector1.length())  # Пример вычисления длины вектора
print(vector2.length())


# In[2]:


# 26
class Window:
    def __init__(self, x, y, width, height, title, visible):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.visible = visible

    def move_horizontal(self, distance):
        new_x = self.x + distance # перемещение по горизонтали
        if new_x >= 0:  # проверка на выход за левую границу экрана
            self.x = new_x
        else:
            print("Вышел за границу окна")
    def move_vertical(self, distance):
        new_y = self.y + distance # перемещение по вертикали
        if new_y >= 0:  # проверка на выход за верхнюю границу экрана
            self.y = new_y
        else:
            print("Вышел за границу окна")
    def change_width(self, new_width):
        if self.x + new_width <= screen_width:  # проверка на пересечение правой границы экрана
            self.width = new_width
        else:
            print("Вышел за границу окна")
    def change_height(self, new_height):
        if self.y + new_height <= screen_height:  # проверка на пересечение нижней границы экрана
            self.height = new_height
        else:
            print("Вышел за границу окна")
    @property
    def is_square(self):   #является ли окно квадратным
        return self.width == self.height

# Пример использования класса Window
screen_width = 1920
screen_height = 1080

window1 = Window(0, 0, 200, 150, "My Window", True)
print(window1.is_square)  # False

window1.change_width(150)
print(window1.is_square)  # True

window1.move_horizontal(50)
print(window1.x) 


# In[29]:


# 27
class Transport:
    def __init__(self, brand, marka, number, speed, capacity):
        self.brand = brand
        self.marka = marka
        self.number = number
        self.speed = speed
        self.capacity = capacity

    def display_info(self):
        print(f"\nBrand: {self.brand}")
        print(f"Marka: {self.marka}")
        print(f"Number: {self.number}")
        print(f"Speed: {self.speed}")
        print(f"Capacity: {self.capacity}")

    def check_capacity(self, required_capacity):
        return self.capacity >= required_capacity


class Car(Transport):
    def __init__(self, brand, marka, number, speed, capacity):
        super().__init__(brand, marka, number, speed, capacity)


class Motorcycle(Transport):
    def __init__(self, brand, marka, number, speed, capacity, has_sidecar):
        if not has_sidecar:
            capacity = 0
        super().__init__(brand, marka, number, speed, capacity)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has sidecar: {self.has_sidecar}")


class Truck(Transport):
    def __init__(self, brand, marka, number, speed, capacity, has_trailer):
        if has_trailer:
            capacity *= 2
        super().__init__(brand, marka, number, speed, capacity)
        self.has_trailer = has_trailer

    def display_info(self):
        super().display_info()
        print(f"Has trailer: {self.has_trailer}")



vehicles = []
vehicles.append(Car("Toyota", "Camry", "123", 120, 1500))
vehicles.append(Motorcycle( "Honda", "accord", "567", 80, 200, False))
vehicles.append(Truck("Volvo", "v60", "8910", 100, 3000, True))

print("All vehicles:")
for vehicle in vehicles:
    vehicle.display_info()

required_capacity = 1000
print(f"Vehicles with capacity >= {required_capacity}:")
for vehicle in vehicles:
    if vehicle.check_capacity(required_capacity) and vehicle.capacity >= 1000:
        vehicle.display_info()


# In[ ]:





# In[ ]:




