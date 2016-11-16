# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def other_rec_hc(base, power):
    if power <= 1 :
        return base
    else:
        # temp =
        return base * other_rec_hc(base,power-1)

print(other_rec_hc(3,3))
