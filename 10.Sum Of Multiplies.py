# Time complexity O(n) | Space complexity O(n)
def sum_of_multiples(n):
    c = []
    for i in range(n+1):
        if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0) or (i % 15 == 0) or (i % 21 == 0) or (i % 35 == 0):
            c.append(i)
    return sum(c)

