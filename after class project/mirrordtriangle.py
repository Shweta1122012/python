print(" print a mirrored right triangle pattern made by stars!")
rows =int(input("enter the number of rows:"))

print("right angle triangle made by stars:")
for i in range(rows):
    for j in range (i+1):
        print("*",end="")
    print()

print("mirrord right angle triangle made by stars:")

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (i + 1))