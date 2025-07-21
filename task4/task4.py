import sys

def read_numbers(path):
    with open(path) as f:
        return sorted([int(line.strip()) for line in f])

def min_moves(nums):
    median = nums[len(nums) // 2]
    return sum(abs(x - median) for x in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py <input_file>")
        sys.exit(1)

    numbers = read_numbers(sys.argv[1])
    print(min_moves(numbers))
