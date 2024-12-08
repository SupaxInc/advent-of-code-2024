def parse_input(file_path):
    """Read and parse the input file."""
    with open(file_path, 'r') as file:
        return file.read()

def is_1_to_3_digit_number(s):
    return s.isdigit() and 1 <= len(s) <= 3

def begin_instructions(s, i):
    startPos = s.find('mul(', i)

    # If start position is false then return that it wasn't found with -1
    if startPos == -1:
        return 0, -1

    openPos = startPos+3
    endPos = s.find(')', openPos)

    if endPos != -1:
        # Grab what we need to multiply and remove the whitespaces. E.g. ( 1,  2 )
        multiples = s[openPos+1:endPos].strip()

        if len(multiples) < 8:
            commaPos = multiples.find(',')

            if commaPos != -1:
                # Split the numbers by the comma if the comma position was found
                # then ensure that there are only 3 numbers and they are a 1 to 3 digit number
                numbers = multiples.split(',')
                if len(numbers) == 2 and is_1_to_3_digit_number(numbers[0]) and is_1_to_3_digit_number(numbers[1]):
                    return int(numbers[0]) * int(numbers[1]), endPos

    return 0, i  # Return current index if invalid, not endPos


def part1(encodedString):
    s = encodedString
    i = 0
    total = 0

    while i < len(s):
        product, endPos = begin_instructions(s, i)

        if endPos == -1:
            break

        total += product

        # Skip to next segment of starting muls (if it was found, else it would just be the current i)
        i = endPos

        # Adds a 1 to begin outside of possible last closing bracket or to prevent infinite loops if no mul was ever found
        i += 1

    return total

    

def part2(encodedString):
    s = encodedString
    i = 0
    total = 0

    while i < len(s):
        doPos = s.find('do()', i)

        if doPos == -1:
            break

        product, endPos = begin_instructions(s, i)

        total += product

        # Skip to next segment of starting muls (if it was found, else it would just be the current i)
        i = endPos

        # Adds a 1 to begin outside of possible last closing bracket or to prevent infinite loops if no mul was ever found
        i += 1

    return total


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
