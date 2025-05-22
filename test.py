def discriminant(a, b, c):
  '''Функция нахождения дискриминанта
   D= b**2 - 4ac'''
  return b**2-4*a*c
#print( discriminant(3, 6, 2))
def solution(a, b, c):
  ''' Поиск корней квадратного уравнения
  ax**2+b*x+c=0 => При D>0 : x1=(-b + sqrt(D))/2a , x2=(-b - sqrt(D))/2a
                    При D=0 : x=(-b )/2a
                    При D<0 :корней нет
  Вычисление квадратного корня:
  num = 25
  sqrt = num ** (0.5)'''
  discrim = discriminant(a, b, c)
  if discrim > 0 :
    result_1=((-b)+(discrim ** (0.5)))/(2*a)
    result_2=((-b)-(discrim ** (0.5)))/(2*a)
    print(result_1,result_2 )
  elif discrim == 0 :
    result = (-b) / (2 * a)
    print(result)
  else:
    print('корней нет')

def test_discriminant():
    # Тесты для функции discriminant(a, b, c)
    assert discriminant(1, 0, 0) == 0  # D = 0² - 4*1*0 = 0
    assert discriminant(1, 5, 6) == 1  # D = 5² - 4*1*6 = 25-24 = 1
    assert discriminant(2, 4, 2) == 0  # D = 4² - 4*2*2 = 16-16 = 0
    assert discriminant(1, 1, 1) == -3  # D = 1² - 4*1*1 = 1-4 = -3

    # Тесты для функции solution(a, b, c)
    # Проверка уравнения с двумя корнями (D > 0)
    solution(1, -5, 6)  # Должно вывести 3.0 и 2.0

    # Проверка уравнения с одним корнем (D = 0)
    solution(1, -4, 4)  # Должно вывести 2.0

    # Проверка уравнения без корней (D < 0)
    solution(1, 1, 1)  # Должно вывести "корней нет"

    print(f"\nВсе тесты функции {test_discriminant.__name__} прошли успешно!\n")

test_discriminant()

def vote(votes):
    # your code
   return max(set(votes), key=votes.count)


def test_vote():
    # Тест 1: Один победитель
    assert vote([1, 1, 2, 3]) == 1

    # Тест 2: Несколько одинаково частых элементов (возвращает первый из них)
    assert vote([1, 2, 1, 2, 3]) in [1, 2]  # Может вернуть 1 или 2

    # Тест 3: Все элементы уникальны (возвращает первый)
    assert vote([10, 20, 30]) == 10

    # Тест 4: Один элемент повторяется много раз
    assert vote(['a', 'a', 'a', 'b']) == 'a'

    # Тест 5: Строки и разные типы данных
    assert vote(['apple', 'banana', 'apple']) == 'apple'

    # Тест 6: Пустой список (вызовет исключение)
    try:
        vote([])
        assert False, "Функция должна вызывать исключение для пустого списка"
    except ValueError:
        pass

    print(f"\nВсе тесты функции {test_vote.__name__} прошли успешно!\n")


# Запуск тестов
test_vote()


def solve(boys: list, girls: list):
    result = ""  # в эту строку сохраните полученные пары или сообщение "Кто-то может остаться без пары!"
    solve = []
    if len(boys) == len(girls):  # проверьте, что длины списков одинаковы
        for boy, girl in zip(sorted(boys), sorted(girls)):  #
            result += f"{boy} и {girl}, "  # добавьте в результат пары
        result = result[:-2]
        return result

    else:
        result = "Кто-то может остаться без пары!"
        return result


def test_solve():
    # Тест 1: Одинаковое количество мальчиков и девочек
    assert solve(["Антон", "Вася"], ["Маша", "Катя"]) == "Антон и Катя, Вася и Маша"

    # Тест 2: Разное количество - должен быть вывод о нехватке
    assert solve(["Антон", "Вася", "Петя"], ["Маша", "Катя"]) == "Кто-то может остаться без пары!"

    # Тест 3: Пустые списки
    assert solve([], []) == ""

    # Тест 4: Один мальчик и одна девочка
    assert solve(["Дима"], ["Оля"]) == "Дима и Оля"

    # Тест 5: Проверка сортировки
    assert solve(["Борис", "Антон"], ["Яна", "Аня"]) == "Антон и Аня, Борис и Яна"

    # Тест 6: Несколько элементов с одинаковыми начальными буквами
    assert solve(["Алекс", "Андрей"], ["Алина", "Анна"]) == "Алекс и Алина, Андрей и Анна"

    # Тест 7: Числа вместо имен (если функция должна поддерживать)
    assert solve([1, 2], [3, 4]) == "1 и 3, 2 и 4"

    print("Все тесты пройдены успешно!")


test_solve()
