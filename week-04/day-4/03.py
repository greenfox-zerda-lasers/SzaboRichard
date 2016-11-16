# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
def omg_brutal_rec(n):
    if n <= 1:
        return 1
    else:
        return n % 10 + omg_brutal_rec(n // 10)


print(omg_brutal_rec(12612))
