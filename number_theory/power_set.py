def power_set(initial_set):

    x = len(initial_set)
    pow_set = []
    for i in range(1 << x): # size of power set: 1 << x == 2^x
        # the bits of i tell us which elements to include
        seti = set()
        for index, elem in enumerate(initial_set):
            if i & (1 << index):
                seti.add(elem)
        pow_set.append(seti) # uses binary digits as index
    return pow_set

[print("{0:12} {1}".format(bin(i), e)) for i, e in enumerate(power_set({1,2,3}))]

# example
# initial_set = {1,2,3}
# each element in the initial_set is effectively indexed by 2^j
# therefore 1<<0 <--> initial_set[0], 1<<1 <--> initial_set[1], and 1<<2 <--> initial_set[2]
# e.g
# i = 5 --> 101 will be true for 1 << 0 --> 1 --> 001 and 1 << 2 --> 4 --> 100
# thus, elements initial_set[0] and initial_set[2] will be included in the subset computation
# dec  bin  elems
# 0    000  {}
# 1    001  {1}
# 2    010  {2}
# 3    011  {1,2}
# 4    100  {3} 1 << j(2) = 4
# 5    101  {1,3}
# 6    110  {2,3}
# 7    111  {1,2,3}
