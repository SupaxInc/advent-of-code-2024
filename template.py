def parse_input(file_path):
    """Read and parse the input file."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def part1(data):
    pass

def part2(data):
    pass

def main():
    # Change this to the path to your input file
    input_file = "inputs/day1.txt"
    
    # Parse input
    data = parse_input(input_file)
    
    # Solve part 1
    result1 = part1(data)
    print(f"Part 1: {result1}")
    
    # Solve part 2
    result2 = part2(data)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
