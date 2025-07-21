import sys

def read_circle(file_path):
    with open(file_path) as f:
        x, y = map(float, f.readline().split())
        r = float(f.readline())
    return x, y, r

def read_points(file_path):
    with open(file_path) as f:
        return [tuple(map(float, line.split())) for line in f]

def classify_point(x, y, r, px, py):
    dist_squared = (px - x)**2 + (py - y)**2
    r_squared = r**2
    if abs(dist_squared - r_squared) < 1e-6:
        return 0
    elif dist_squared < r_squared:
        return 1
    else:
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py <circle_file> <points_file>")
        sys.exit(1)

    x, y, r = read_circle(sys.argv[1])
    points = read_points(sys.argv[2])

    for px, py in points:
        print(classify_point(x, y, r, px, py))
