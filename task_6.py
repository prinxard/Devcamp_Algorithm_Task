import itertools
integer_array = [2, 8, 4, 7, 9, 5, 1]
target = 14
for numbers in itertools.combinations(integer_array, 3):
    if sum(numbers) == target:
        print([integer_array.index(number) for number in numbers])
