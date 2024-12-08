def parse_input(file_path):
    """Read and parse the input file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Check if XMAS exists starting at a position in a given direction
    def check_xmas(row, col, dx, dy):
        if (0 <= row + 3*dx < rows and 
            0 <= col + 3*dy < cols and
            grid[row][col] == 'X' and
            grid[row + dx][col + dy] == 'M' and
            grid[row + 2*dx][col + 2*dy] == 'A' and
            grid[row + 3*dx][col + 3*dy] == 'S'):
            return 1
        return 0

    # For each starting position
    for row in range(rows):
        for col in range(cols):
            # Check all 8 directions
            # Horizontal (right)
            count += check_xmas(row, col, 0, 1)
            # Horizontal (left)
            count += check_xmas(row, col, 0, -1)
            # Vertical (down)
            count += check_xmas(row, col, 1, 0)
            # Vertical (up)
            count += check_xmas(row, col, -1, 0)
            # Diagonal (down-right)
            count += check_xmas(row, col, 1, 1)
            # Diagonal (up-left)
            count += check_xmas(row, col, -1, -1)
            # Diagonal (down-left)
            count += check_xmas(row, col, 1, -1)
            # Diagonal (up-right)
            count += check_xmas(row, col, -1, 1)
    
    return count

def part1(data):
    return find_xmas(data)

def part2(data):
    pass

def main():
    # Change this to the path to your input file
    input_file = "day4/input.txt"
    
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
