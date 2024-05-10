n = int(input())
for i in range(1, n, 1):
    print(" " * (n - i - 1) + "*" if i == 1 else " " * (n - i - 1) + "o" * (2 * i - 1))
print(" " * (n - 3) + "| |")
