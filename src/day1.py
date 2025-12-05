def part1():
    file = open("inputs/day1.txt")

    dial = 50
    count_zero = 0

    for line in file:
        dir = line[0]
        val = int(line[1:])

        print([dir, val])

        if dir == "L":
            dial -= val
        elif dir == "R":
            dial += val

        while (dial >= 100):
            dial -= 100

        while (dial < 0):
            dial += 100

        if dial == 0:
            count_zero += 1

        print(dial)

    return count_zero


def rotate_dial(dial, count_zero, dir, val):
    while (val > 0):
        if dir == "L":
            dial -= 1
        elif dir == "R":
            dial += 1

        if dial > 99:
            dial = 0
            print("99 max reached")
        elif dial < 0:
            dial = 99
            print("0 min reached")
        
        if dial == 0:
            count_zero += 1
            print("0 clicked")

        val -= 1

    return dial, count_zero


def part2():
    file = open("inputs/day1.txt")

    dial = 50
    count_zero = 0

    for line in file:
        print(f"dial: {dial}")
        print(f"count_zero: {count_zero}")

        dir = line[0]
        val = int(line[1:])

        print([dir, val])

        dial, count_zero = rotate_dial(dial, count_zero, dir, val)

        print(f"dial: {dial}")
        print(f"count_zero: {count_zero}")

        print("="*60)

    return count_zero


p1 = part1()
p2 = part2()
print("\n")
print(f"risultato parte 1: {p1}")
print(f"risultato parte 2: {p2}")
