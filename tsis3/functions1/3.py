def solve(numheads, numlegs):
    if numlegs % 2 == 1 or 4 * numheads < numlegs or numlegs < 2 * numheads:
        return "No solution"
    chickens = (4 * numheads - numlegs) // 2
    rabbits = (numlegs - 2 * numheads) // 2
    print((chickens, rabbits))


heads = int(input())
legs = int(input())

print(solve(heads, legs))