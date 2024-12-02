from collections import Counter


def parse_input(file_path):
    """Read and parse the input file."""
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def part1(locations1, locations2):
    total = 0
    locations1.sort()
    locations2.sort()

    for loc1, loc2 in list(zip(locations1, locations2)):
        total += abs(loc1 - loc2)
    return total

def part2(locations1, locations2):
    similarityScore = 0
    locations2Freq = Counter(locations2)

    for loc in locations1:
        similarityScore += loc * locations2Freq.get(loc, 0)
    
    return similarityScore

def main():
    input_file = "day1/input.txt"
    
    # Parse input
    data = parse_input(input_file)
    locations1 = []
    locations2 = []

    for line in data:
        locations = line.split("   ") 
        locations1.append(int(locations[0]))
        locations2.append(int(locations[1]))

    # Solve part 1
    result1 = part1(locations1, locations2)
    print(f"Part 1: {result1}")
    
    # Solve part 2
    result2 = part2(locations1, locations2)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
