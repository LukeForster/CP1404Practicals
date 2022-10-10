numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]              # Output = 3     - Correct
numbers[-1]             # Output = 2     - Correct
numbers[3]              # # Output = 1   - Correct
numbers[:-1]            # Output = 3     - Incorrect, Ans:  [3, 1, 4, 1, 5, 9]
numbers[3:4]            # Output = 1     - Incorrect, Ans: [1]
5 in numbers            # Output = 2     - Incorrect, Ans: True
7 in numbers            # Output = N/A   - Incorrect, Ans: False
"3" in numbers          # Output = pos[0]- Incorrect, Ans: False
numbers + [6, 5, 3]     # Output = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] - Correct