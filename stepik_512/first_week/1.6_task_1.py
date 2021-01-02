# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
#
# Или эквивалентно записи:
# class Class1(Class2, Class3 ... ClassK):
#     pass
#
# Класс A является прямым предком класса B, если B отнаследован от A:
# class B(A):
#     pass
#
# Класс A является предком класса B, если
#     A = B;
#     A - прямой предок B
#     существует такой класс C, что C - прямой предок B и A - предок C
#
# Например:
# class B(A):
#     pass
# class C(B):
#     pass
# # A -- предок С
#
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
#
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
#
#
# Формат входных данных:
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов
# наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется,
# что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного
# класса более одного раза.
#
# В следующей строке содержится число q - количество запросов.
#
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
#
# Формат выходных данных:
# Для каждого запроса выведите в отдельной строке слово "Yes", если
# класс 1 является предком класса 2, и "No", если не является.
#
# Sample Input:
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A
#
# Sample Output:
# Yes
# Yes
# Yes
# No


classes = {}


def fill_classes(str):
    # Заполняет словарь classes входными данными
    # {Название класса : [Прямые родители]}
    if len(str) == 1:
        classes[str[0]] = 'Object'
    else:
        values = []
        for i in range(2, len(str)):
            values.append(str[i])
        classes[str[0]] = values


def get_parent(parent, child):
    # Yes если parent предок child
   # print(f"{parent}, {child}")

    if child not in classes:
        return False

    if (child == parent) or (parent in classes[child]):
        return True

    if classes[child] == 'Object':
        return False

    for i in classes[child]:
        if get_parent(parent, i):
            return True
    return False


n = int(input())
for _ in range(n):
    str = input().split()
    fill_classes(str)

#print(classes)

q = int(input())
for _ in range(q):
    str = input().split()
    if get_parent(str[0], str[1]):
        print('Yes')
    else:
        print('No')