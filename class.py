class Solution:
    def __init__(self, s):
        self.rim = s

    def romanToInt(self):
        dict_of_rim = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(0, len(self.rim)):
            if i == 0 or dict_of_rim[self.rim[i]] <= dict_of_rim[self.rim[i - 1]]:
                result += dict_of_rim[self.rim[i]]
            else:
                result += dict_of_rim[self.rim[i]] - 2 * dict_of_rim[self.rim[i - 1]]
        return result


n = Solution('MMMCMXCIX')
print(n.romanToInt())
