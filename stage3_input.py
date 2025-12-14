file = open("data.txt", "r")
a, b, c, x = map(float, file.readline().split())
file.close()

y = a*x*x + b*x + c
print("Weather value:", y)

