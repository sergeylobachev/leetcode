def solution(nums, target):
    if sum(nums) < target:
        return -1

    tbin = [0] * 35
    nbin = [0] * 35

    operations = 0

    for i in range(35):
        if (target & 1 << i) > 0:
            tbin[i] = 1

    for num in nums:
        counter = 0
        while num > 1:
            num //= 2
            counter += 1
        nbin[counter] += 1

    for i in range(34):
        if tbin[i] == 0:
            nbin[i+1] += nbin[i] // 2
            nbin[i] = nbin[i] % 2
        elif tbin[i] == 1:
            if nbin[i] > 0:
                tbin[i] = 0
                nbin[i] -= 1
                nbin[i+1] += nbin[i] // 2
                nbin[i] = nbin[i] % 2
            elif nbin[i] == 0:
                j = i
                while nbin[j] == 0:
                    j += 1
                operations += (j - i)
                while j > i:
                    nbin[j] -= 1
                    nbin[j-1] += 2
                    j -= 1

    print("tbin=", tbin)
    print("nbin=", nbin)
    print("operations", operations)

    return operations


nums = [1,2,8]
target = 7

# nums = [1,32,1,2]
# target = 12

# nums = [16,16,4]
# target = 3

print(solution(nums, target))


