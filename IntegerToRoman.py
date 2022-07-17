class Solution(object):
    def intToRoman(self, num):
        rmap = {
                    1:"I", 
                    4: "IV",
                    5:"V",
                    9: "IX",
                    10:"X",
                    40:"XL",
                    50:"L",
                    90:"XC",
                    100:"C",
                    400:"CD",
                    500:"D",
                    900:"CM",
                    1000:"M"
                }
        seq = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        so_far, idx = [], 0
        while num > 0:
            if num >= seq[idx]:
                so_far.append(rmap[seq[idx]])
                num -= seq[idx]
            else:
                idx += 1
        return "".join(so_far)
        """
        :type num: int
        :rtype: str
        """
        