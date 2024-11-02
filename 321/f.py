# 1
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
average = (num1 + num2) / 2
print(f"Среднее арифметическое: {average}")
# 2
x = int(input("Введите значение x: "))
y = (x**3) / (2 * (x + 5))
print(f"{x}:{y}")
# 3
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
dis= b**2 - 4 * a * c
if dis > 0:
  x1 = (-b + math.sqrt(dis)) / (2 * a)
  x2 = (-b - math.sqrt(dis)) / (2 * a)
  print(f"Корни уравнения:{x1};{x2}")
else:
  print("Дискриминант меньше или равен 0, корней нет.")
# 4
num = int(input("Введите трехзначное число: "))
hundreds = num // 100
tens = (num % 100) // 10
units = num % 10
print(f"Сотни: {hundreds}, Десятки: {tens}, Единицы: {units}")
# 5
a= int(input("Введите первый угол: "))
b = int(input("Введите второй угол: "))
if a + b < 180:
  print("Такой треугольник существует.")
  if a == 90 or b == 90 or a + b == 90:
    print("Треугольник прямоугольный.")
  else:
    print("Треугольник не прямоугольный.")
else:
  print("Такой треугольник не существует.")

#6
temp = float(input("Введите температуру: "))
if temp < 0:
  print("Вода в твердом состоянии (лед).")
elif temp >= 0 and temp < 100:
  print("Вода в жидком состоянии.")
else:
  print("Вода в газообразном состоянии (пар).")
# 7
num = int(input("Введите число: "))
if num % 2 == 0:
  print("Число четное.")
else:
  print("Число нечетное.")
# 8
print(5 + 3**2 - 18*4 + 120 / 5)
print(25.5 + 4.2**2 - 125 / 5)


# 9

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
result = num1 ** num2
result /= num1
ost = result % num1
print(f"Остаток от деления: {ost}")

# 10

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
division = num1 / num2
division_int= num1 // num2
print(f"Результат обычного деления: {division}")
print(f"Результат целочисленного деления: {division_int}")


# 11

float_num = float(input("Введите дробное число: "))
int_num = int(input("Введите целое число: "))
rem = float_num % int_num
print(f"Остаток от деления: {rem}")

