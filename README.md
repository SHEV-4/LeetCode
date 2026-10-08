# LeetCode Solutions

My solutions to [LeetCode](https://leetcode.com/) problems in Python. For some problems there are several solutions so that the approaches can be compared: brute force, a mathematical method, optimization. The comment at the start of each solution gives the date, runtime, and memory usage reported by LeetCode.

## Problems

| # | Problem | Difficulty | Approach | Algorithm complexity | File |
|---|---|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | hash table: for each number, look for `target - num` among the numbers already seen | O(n) time, O(n) space | [two_sum](easy/0001_two_sum.py) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | 1) compare the string with its reverse; 2) mathematical reversal of the number without strings | O(log x) time, O(1) space in the second solution | [palindrome_number](easy/0009_palindrome_number.py) |
| 3354 | [Make Array Elements Equal to Zero](https://leetcode.com/problems/make-array-elements-equal-to-zero/) | Easy | 1) full simulation for each starting position; 2) prefix sums: compare the sum to the left and to the right of each zero | solution 2: O(n) time, O(1) space | [make_array_elements_equal_to_zero](easy/3354_make_array_elements_equal_to_zero.py) |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | 1) digit-by-digit addition with carry; 2) convert the lists to numbers, add them, and build a new list | solution 1: O(max(m, n)) time | [add_two_numbers](medium/0002_add_two_numbers.py) |

## Optimization Example

The problem **Make Array Elements Equal to Zero**: the first solution simulates the process for each starting position and runs in about **5235 ms**. The second solution uses prefix sums and runs in about **54 ms**, almost 100 times faster. Runtime depends on the load of the LeetCode servers, so the values at the time of submission are given.

## Repository Structure

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

Files are named using the pattern `<problem number>_<name>.py`, and the folders correspond to difficulty.

## How to Run the Solutions

The files contain code in the form that LeetCode accepts, that is, only the `Solution` class. The `List`, `Optional`, and `ListNode` types are supplied automatically on the site. To run a solution locally, add this at the top of the file:

```python
from typing import List, Optional
```

For linked list problems (`Add Two Numbers`), you also need to define the node class:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

Example check:

```python
print(Solution().twoSum([2, 7, 11, 15], 9))   # [0, 1]
```

> If a file contains several solutions, they are all named the same (`Solution`), so only the last one takes effect when running locally. To test a particular solution, temporarily comment out or rename the others.

## Author

[SHEV-4](https://github.com/SHEV-4)
