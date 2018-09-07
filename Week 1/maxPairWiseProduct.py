# Uses python3

class maxPairWiseProduct:
    def find_max_pair_wise(numList):
        p1 = 0
        p2 = 0
        for num in numList:
            if num >= p1:
                p2 = p1
                p1 = num
            elif num > p2:
                p2 = num

        return p1 * p2

