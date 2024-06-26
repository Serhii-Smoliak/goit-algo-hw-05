# goit-algo-hw-05

# Задача 1
- run task_1.py

# Задача 2
- run task_2.py

# Задача 3
- run task_3.py

# Висновки по задачі №3 щодо швидкостей алгоритмів пошуку підрядка

1.  ### Пошукова фраза на початку кожної статті:
        "Автори публікації"

     ### Результат роботи алгоритмів:

        Article 1
          - Реальний підрядок:
            - Rabin-Karp: 4.59e-05 с
            - Boyer-Moore: 1.45e-05 с
            - KMP: 2.03e-05 с
          - Вигаданий підрядок:
            - Rabin-Karp: 0.00380 с
            - Boyer-Moore: 0.00072 с
            - KMP: 0.00220 с
    
        Article 2
          - Реальний підрядок:
            - Rabin-Karp: 4.69e-05 с
            - Boyer-Moore: 1.52e-05 с
            - KMP: 2.43e-05 с
          - Вигаданий підрядок:
            - Rabin-Karp: 0.00560 с
            - Boyer-Moore: 0.00096 с
            - KMP: 0.00330 с

2. ### Пошукова фраза в середині:
       стаття №1: "Він корисний"
       стаття №2: "Час доступу"

     ### Результат роботи алгоритмів:

       ### Article 1
       - Реальний підрядок:
         - Rabin-Karp: 0.00182 с
         - Boyer-Moore: 0.00043 с
         - KMP: 0.00102 с
       - Вигаданий підрядок:
         - Rabin-Karp: 0.00377 с
         - Boyer-Moore: 0.00065 с
         - KMP: 0.00229 с

       ### Article 2
       - Реальний підрядок:
         - Rabin-Karp: 0.00040 с
         - Boyer-Moore: 0.00010 с
         - KMP: 0.00022 с
       - Вигаданий підрядок:
         - Rabin-Karp: 0.00563 с
         - Boyer-Moore: 0.00096 с
         - KMP: 0.00329 с

3. ### Пошукова фраза в кінці:
       стаття №1: "Жадібні алгоритми"
       стаття №2: "Искусство программирования"

     ### Результат роботи алгоритмів:

       ### Article 1
       - Реальний підрядок:
         - Rabin-Karp: 0.00270 с
         - Boyer-Moore: 0.00052 с
         - KMP: 0.00151 с
       - Вигаданий підрядок:
         - Rabin-Karp: 0.00377 с
         - Boyer-Moore: 0.00065 с
         - KMP: 0.00219 с

       ### Article 2
       - Реальний підрядок:
         - Rabin-Karp: 0.00562 с
         - Boyer-Moore: 0.00072 с
         - KMP: 0.00312 с
       - Вигаданий підрядок:
         - Rabin-Karp: 0.00561 с
         - Boyer-Moore: 0.00099 с
         - KMP: 0.00325 с

## Загальні висновки

- У загальному, алгоритм Боєра-Мура виявився найшвидшим для обох текстів та обох типів підрядків.
- Алгоритм Кнута-Морріса-Прата (KMP) показав хороші результати, але трохи повільніший, ніж Боєра-Мура.
- Алгоритм Рабіна-Карпа виявився найповільнішим серед трьох.
- Швидкість виконання алгоритмів може залежати від конкретного тексту та підрядка, тому рекомендується виконати додаткові тести на різних даних для отримання більш точних результатів.