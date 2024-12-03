def parse_input(file_path):
    """Read and parse the input file."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.split())) for line in file.readlines()]

def is_safe_report(levels, skip_index=-1):
    """Check if a report is safe, optionally skipping one index."""
    # Get valid numbers (excluding skipped index)
    nums = [n for i, n in enumerate(levels) if i != skip_index]
    
    if len(nums) < 2:
        return True
    
    # Determine if report is increasing or decreasing
    direction = 'increasing' if nums[1] > nums[0] else 'decreasing'
    
    # Check each adjacent pair
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        
        # Must maintain same direction
        if (direction == 'increasing' and diff <= 0) or (direction == 'decreasing' and diff >= 0):
            return False
        
        # Must differ by 1-3
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    
    return True

def part1(reports):
    """Count safe reports without Problem Dampener."""
    return sum([1 for report in reports if is_safe_report(report)])

def part2(reports):
    """Count safe reports with Problem Dampener."""
    safe_count = 0
    
    for report in reports:
        # Instantly check if report is safe without removing any level
        if is_safe_report(report):
            safe_count += 1
            continue
        
        # If its not safe, try removing each level one at a time until it returns true
        for i in range(len(report)):
            if is_safe_report(report, i):
                safe_count += 1
                break
    
    return safe_count

def main():
    input_file = "day2/input.txt"
    reports = parse_input(input_file)
    
    # Solve part 1
    result1 = part1(reports)
    print(f"Part 1: {result1}")
    
    # Solve part 2
    result2 = part2(reports)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
