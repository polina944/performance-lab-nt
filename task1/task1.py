import sys

def circular_path(n, m):
    path = []
    index = 0
    for _ in range(n):
        path.append((index % n) + 1)
        index = (index + m) % n
        if index == 0:
            break
    return ''.join(map(str, path))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task1.py <n> <m>")
        sys.exit(1)
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print(circular_path(n, m))
