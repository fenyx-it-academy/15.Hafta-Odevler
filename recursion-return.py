def list_recursion(number):
    numbers = []
    if number > 0:
        numbers.append(number)
        return numbers + list_recursion(number - 1)
    else:
        return []

print(list_recursion(5))

list_recursion(5)

[5] + list_recursion(4)

[5] + ([4] + list_recursion(3))

[5] + ([4] + ([3] + list_recursion(2)))


[5] + ([4] + ([3] + ([2] + list_recursion(1))))


[5] + ([4] + ([3] + ([2] + ([1] + list_recursion(0)))))


[5] + ([4] + ([3] + ([2] + ([1] + []))))

[5] + ([4] + ([3] + ([2] + ([1]))))


[5] + ([4] + ([3] + ([2, 1])))


[5] + ([4] + ([3, 2, 1]))


[5] + ([4, 3, 2, 1])

[5, 4, 3, 2, 1]

