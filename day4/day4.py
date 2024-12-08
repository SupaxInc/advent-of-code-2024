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

def find_xmas_part2(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def check_mas(row, col, dx, dy):
        # Check if SAM exists
        if (0 <= row + 2*dx < rows and 
            0 <= col + 2*dy < cols and
            grid[row][col] == 'M' and
            grid[row + dx][col + dy] == 'A' and
            grid[row + 2*dx][col + 2*dy] == 'S'):
            return True
        # Check for backwards MAS if SAM doesn't exist
        if (0 <= row + 2*dx < rows and 
            0 <= col + 2*dy < cols and
            grid[row][col] == 'S' and
            grid[row + dx][col + dy] == 'A' and
            grid[row + 2*dx][col + 2*dy] == 'M'):
            return True
        return False

    # For each center position (where the A would be)
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            # Check if current cell is not an A
            if grid[row][col] != 'A':
                continue
                
            # If it is an A check for X pattern, so check for both MAS and SAM in each direction
            # Begin from top-left with a direction of down-right
            # AND Begin top-right with a direction of down-left
            if (check_mas(row-1, col-1, 1, 1) and 
                check_mas(row-1, col+1, 1, -1)):
                count += 1
                
    return count

def part1(data):
    return find_xmas(data)

def part2(data):
    return find_xmas_part2(data)

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
