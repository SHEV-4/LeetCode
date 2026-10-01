# LeetCode Solutions

Мої розв'язки задач з [LeetCode](https://leetcode.com/) на Python. Для частини задач є кілька рішень, щоб порівняти підходи: наївний перебір, математичний спосіб, оптимізація. У коментарях на початку кожного рішення вказано дату, час виконання та використану пам'ять з LeetCode.

## Задачі

| # | Задача | Складність | Підхід | Складність алгоритму | Файл |
|---|---|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | хеш-таблиця: для кожного числа шукаємо `target - num` серед уже побачених | O(n) час, O(n) пам'ять | [two_sum](easy/0001_two_sum.py) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | 1) порівняння рядка з його розворотом; 2) математичний розворот числа без рядків | O(log x) час, у другому рішенні O(1) пам'ять | [palindrome_number](easy/0009_palindrome_number.py) |
| 3354 | [Make Array Elements Equal to Zero](https://leetcode.com/problems/make-array-elements-equal-to-zero/) | Easy | 1) повна симуляція для кожної стартової позиції; 2) префіксні суми: порівнюємо суму зліва й справа від кожного нуля | рішення 2: O(n) час, O(1) пам'ять | [make_array_elements_equal_to_zero](easy/3354_make_array_elements_equal_to_zero.py) |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | 1) додавання по розрядах з перенесенням; 2) перетворення списків у числа, додавання й побудова нового списку | рішення 1: O(max(m, n)) час | [add_two_numbers](medium/0002_add_two_numbers.py) |

## Приклад оптимізації

Задача **Make Array Elements Equal to Zero**: перше рішення симулює процес для кожної стартової позиції й виконується приблизно **5235 мс**. Друге рішення використовує префіксні суми й виконується приблизно за **54 мс**, тобто майже у 100 разів швидше. Час виконання залежить від навантаження серверів LeetCode, тому наведено значення на момент відправлення.

## Структура репозиторію

```
.
├── easy/
│   ├── 0001_two_sum.py
│   ├── 0009_palindrome_number.py
│   └── 3354_make_array_elements_equal_to_zero.py
├── medium/
│   └── 0002_add_two_numbers.py
└── README.md
```

Файли названо за схемою `<номер задачі>_<назва>.py`, папки відповідають складності.

## Як запускати рішення

Файли містять код у тому вигляді, в якому його приймає LeetCode, тобто лише клас `Solution`. Типи `List`, `Optional` і `ListNode` на сайті підставляються автоматично. Щоб запустити рішення локально, додай на початок файлу:

```python
from typing import List, Optional
```

Для задач зі зв'язаними списками (`Add Two Numbers`) потрібно також описати клас вузла:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Приклад перевірки:

```python
print(Solution().twoSum([2, 7, 11, 15], 9))   # [0, 1]
```

> Якщо у файлі кілька рішень, вони названі однаково (`Solution`), тому під час локального запуску діє лише останнє. Щоб перевірити окреме рішення, тимчасово закоментуй або перейменуй інші.

## Автор

[SHEV-4](https://github.com/SHEV-4)
