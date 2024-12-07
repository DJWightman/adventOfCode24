def convertToInts(row):
    row[0] = int(row[0])
    temp = row[1].split(' ')
    temp.remove('')
    row[1] = [int(x) for x in temp]


def getOperatorSizes(row):
    return len(row[1])


def get2sSolution(row):
    nums = row[1]
    max = len(nums) - 1
    for ii in range(2**max):
        soln = nums[0]
        for bit in range(max):
            x = (ii >> bit) & 1
            if x == 0:
                soln += nums[1+bit]
            else:
                soln *= nums[1+bit]
        #print(s)
        if soln == row[0]:
            #print("Soln found")
            return row[0]

    return 0

def get3sSolution(row):
    max = len(row[1]) - 1
    for i in range(3**max):
        nums = row[1].copy()
        ops = []
        x = i
        for bit in range(max):
            ops.append(x % 3)
            x = int(x/3)
        
        soln = nums[0]
        for bit, op in enumerate(ops):
            if op == 0:
                soln += nums[1+bit]
            elif op == 1:
                soln *= nums[1+bit]
            else:
                soln = int(str(soln) + str(nums[1+bit]))
        if soln == row[0]:
            print(f"Found: {row[0]}, nums:{nums}")
            return row[0]
        
    return 0