def parse_input(file_path):
    """Read and parse the input file."""
    with open(file_path, 'r') as file:
        return file.read()

def is_1_to_3_digit_number(s):
    return s.isdigit() and 1 <= len(s) <= 3

def part1(encodedString):
    s = encodedString
    i = 0
    total = 0

    while i < len(s):
        startPos = s.find('mul(', i)

        if startPos == -1:
            break; # No more mul instructions found

        openPos = startPos+3 # Open bracket ( position
        # Find closing bracket position beginning from open bracket
        endPos = s.find(')', openPos) 

        if endPos != -1:
            # Remove the white spaces to ensure we have valid length checking later
            multiples = s[openPos+1:endPos].strip() # E.g. 111,111

            if len(multiples) < 8:
                commaPos = multiples.find(',')

                if commaPos != -1:
                    numbers = multiples.split(',')
                    if len(numbers) == 2 and is_1_to_3_digit_number(numbers[0]) and is_1_to_3_digit_number(numbers[1]):
                        total += int(numbers[0]) * int(numbers[1])

                # Skip to next segment of starting muls
                i = endPos

        # Adds a 1 to begin outside of possible last closing bracket or to prevent infinite loops if no mul was ever found
        i += 1

    return total

def part2(encodedString):
    pass

def main():
    # Change this to the path to your input file
    input_file = "day3/input.txt"
    
    # Parse input
    encodedString = parse_input(input_file)
    
    # Solve part 1
    result1 = part1(encodedString)
    print(f"Part 1: {result1}")
    
    # Solve part 2
    result2 = part2(encodedString)
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
