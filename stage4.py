file = open("data.txt", "r")

for line in file:
    a, b, c, x = map(float, line.split())
    y = a*x*x + b*x + c
    print("Weather value:", y)

file.close()
