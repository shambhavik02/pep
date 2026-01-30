t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    last = 1000
    possible = True
    while cubes:
        if cubes[0] >= cubes[-1]:
            pick = cubes.pop(0)
        else:
            pick = cubes.pop()

        if pick > last:
            possible = False

        last = pick

    print("Yes" if possible else "No")
