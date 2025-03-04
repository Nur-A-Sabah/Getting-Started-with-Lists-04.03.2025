emptylist = []
print(emptylist)
print(type(emptylist))

numbers = [1, 2, 3, 4, 5]
print(numbers[2])

numbers.append("Abir")
numbers.append("Maimuna")
numbers.append("Sabah")

print(numbers)
print(numbers[5])
print(numbers[6])
print(numbers[-1])

numbers.pop()
numbers.pop(5)
numbers.pop()
print(numbers)

triples = [1, 2, 3] * 4
print(triples)

aList = [100, 200, 300, 400, 500]
print(aList[::-1])