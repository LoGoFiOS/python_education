Здесь я выкладываю материалы, которые накапливаются у меня в процессе изучения Python.

------------

## Директория stepik_512
Материалы по курсу [Python: основы и применение](https://stepik.org/course/512/ "Python: основы и применение"): конспект лекций, а так же ответы на задачи.

## Директория Instructions

Инструкции по настройке, работе с чем-либо.

------------

## 1. Дорожная карта

Мой путь становления Python разработчиком.

### 1.1 Курс "введение в Linux"

Период учёбы: 12.20 - 12.20, [ссылка](https://stepik.org/course/73/)

На мой взгляд материал подаётся достаточно, для начинающих, глубоко, а полученных знаний хватит, чтобы двигаться дальше. Затронуты такие полезные темы, как: **tmux, bash, vim, ssh**.

Конспектировал лекции (не оцифровано).

### 1.2 Курс "Python: основы и применение"

Период учёбы: 12.20 - 01.21, [ссылка](https://stepik.org/course/512/)

Объясняются (и очень хорошо!) фундаментальные вещи, без которых невозможно понять философию Python и, соответственно, писать эффективный код.

Во время обучения старался максимально использовать **GitHub, Vim и PyCharm** для получения опыта.

Начал решать задачи на [CodeWars](https://www.codewars.com/users/LoGoFiOS) и [LeetCode](https://leetcode.com/logofios/). Создал [страничку](https://logofios.github.io/) им. себя.

### 1.3 Разработка Telegram ботов <– you are here

Период обучения: 02.21 - 

Следующей темой выбрал создание ботов. Планирую разобраться с asyncio, декораторами, aiogram, БД, настройкой серверов, Docker. Создам пару ботов. Плюс периодическая практика – решение задач. 

Приобрёл курс [Разработка Telegram ботов на Python](https://www.udemy.com/course/aiogram-python/). 

***to be continued...***

## 2. Подборка книг

Подборка книг, которые я выбрал для себя и которые, кхм, рекомендую. Их не нужно читать от корки до корки, скорее открывать на тех темах тогда, когда хочется разобраться в чём-то.

- "Python. К вершинам мастерства" – Рамальо Лучано
- "Python. Книга Рецептов" – Кэвэна-Джонс Брайан, Бизли Дэвид М.
- "Чистый Python. Тонкости программирования для профи" – Бейдер Дэн
- "Чистый код. Создание анализ и рефакторинг" – Мартин Роберт К.
- "Паттерны объектно-ориентированного проектирования" – Гамма Эрих, Хелм Ричард
- "Классические задачи Computer Science на языке Python" – Копец Дэвид

## 3. Статьи

Сборник полезных статей, объединённых по группам. 

### 3.1 Roadmaps, общее про становление

- [Python-Roadmap: Дорожная карта по изучению Python](https://github.com/GnuriaN/Python-Roadmap)
- [Как не стать Python-разработчиком](https://habr.com/ru/post/350748/)
- [Что нужно знать, уметь и понимать, чтобы не иметь проблем с поиском работы питонистом](https://habr.com/ru/post/311642/)
- [Что надо знать Python веб-разработчику для успешного поиска работы?](https://www.youtube.com/watch?v=9kLI6R0heTQ)
- [Несколько полезных советов как практиковаться в Python](https://habr.com/ru/post/478900/)

### 3.2 Изучение Linux

- [Примеры *nix](http://najomi.org/_nix)
- [Bash-скрипты](https://habr.com/ru/company/ruvds/blog/325522/)

### 3.3 Изучение Vim

- [ Как пользоваться Vim](http://najomi.org/vim)

### 3.4 Про виртуальное окружение

- [Что это + настройка](https://python-scripts.com/virtualenv)

### 3.5 Изучение Git

- [Крутая и бесплатная онлайн книга](https://git-scm.com/book/ru/v2)
- [Бесплатный курс](https://githowto.com/ru)

### 3.6 Собеседование/Поиск работы

- [Что работодатели ждут от Junior Python-разработчика](https://tproger.ru/articles/what-junior-python-dev-should-know/)
- [Обширный обзор собеседований по Python. Советы и подсказки](https://habr.com/ru/post/439576/)
- [Как проходит собеседование начинающего разработчика на С++: что нужно знать и как подготовиться](https://habr.com/ru/company/yandex_praktikum/blog/533154/)
- [Как джуниор-разработчику найти работу ](https://vc.ru/flood/29126-kak-dzhunior-razrabotchiku-nayti-rabotu)
- [Детальный разбор интервью для Junior Python Developer](https://habr.com/ru/post/458746/)
- Тестовое [задание](https://www.notion.so/backend-14c451038c5541c9996095192db75fc6) Python, Django.

### 3.7 Изучение Docker

- [Изучаем Docker](https://habr.com/ru/company/ruvds/blog/438796/)

### 3.8 Разное про Python

- [Про scopes и namespace](https://realpython.com/python-scope-legb-rule/#using-enclosing-scopes-as-closures)
- [Как работает yield](https://habr.com/ru/post/132554/)
- Про декораторы [раз](https://tirinox.ru/python-decorators/) и [два](https://tirinox.ru/parametric-decorator/)
- Asyncio [раз](https://webdevblog.ru/obzor-async-io-v-python-3-7/), [два](https://realpython.com/python-concurrency/)

### 3.9   Алгоритмы

- [Число простое или нет](https://foxford.ru/wiki/informatika/proverka-chisla-na-prostotu-v-python)

  Здесь важно отметить, что у составного числа есть собственный делитель, не превосходящий квадратного корня из числа. Отсюда и **return d * d > n**.

- [Бинарное дерево](https://stephenagrice.medium.com/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533)

### 3.10 Регулярные выражения

* [Мета символы](https://www.debuggex.com/cheatsheet/regex/python) регулярных выражений
* [Статья](https://habr.com/ru/post/349860/) на habr.com
* Онлайн [редактор](https://regex101.com/#python)


## 4. Практика

Для практики подходит как решение задачек, так и создание личных проектов.

- Вопросы на [stackoverflow](https://ru.stackoverflow.com/questions/tagged/python)
- [CodeWars](https://www.codewars.com/)
- [Leetcode](https://leetcode.com/problemset/all/)
- [Sololearn](https://www.sololearn.com/)

## 5. Курсы

- Курсы от московского сообщества [Python](https://learn.python.ru/). Длительность 2 мес. (!), есть оффлайн вариант.
- [Практический курс парсинга сайтов на Python](https://www.patreon.com/posts/karta-kurs-na-30462246)
- [Разработка Telegram ботов на Python](https://www.udemy.com/course/aiogram-python/)
- [Полный курс по веб разработке с нуля на Python + Django ](https://www.udemy.com/course/python-pythondjango/)

## 6. Источники информации

- YouTube Блог [Диджитализируй!](https://www.youtube.com/channel/UC9MK8SybZcrHR3CUV4NMy2g)

  Архиполезный блог, очень рекомендую.

- [Лекции](https://youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0) по алгоритмам Тимофея Хирьянова.

  Преподавать здоровски подаёт материал, смотреть одно удовольствие. У него есть лекции и по языку Python, но, возможно, после тех курсов, что я советую, покажется малоинформативным. 

- YouTube канал [Хитрый Питон](https://www.youtube.com/channel/UC2-j4-hV33hboyK1FtukJ9w/videos)

  Небольшие ролики про тонкости Питона. 

## 7. Разное

- Пошаговый [визуализатор](http://www.pythontutor.com/) кода