# Model 1
grid = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['Y', ' ', ' ', ' ', 'Y', 'Y', ' '],
    ['R', ' ', ' ', 'Y', 'R', 'R', ' '],
    ['R', 'R', 'Y', 'R', 'Y', 'R', ' '],
    ['R', 'Y', 'R', 'Y', 'Y', 'Y', 'R'],
]

# Model 2
groceries = ["Apples", "Milk", "Flour", "Chips"]
for item in groceries:
    print("Don't forget the", item)
count = 0
for row in grid:  # outer loop
    print("row =", row)
    for cell in row:  # inner loop
        print("cell =", cell)
        if cell == ' ':
            count += 1
print(count, "spaces remaining")


lines = []
for i in range(6):
    for j in range(7):
        add = i, '+', j, '=', i + j
        lines.append(add)
print(len(lines))

count = 0
for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
        cell = row[j]
        if cell == ' ':
            count += 1
print(count)

for n in range(1, 21):
    fact = 1
    for x in range(1, n+1):
        fact *= x
    print("The factorial of", n, "is", fact)
