class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        result = ''
        for encodedStr in strs:
            result += str(len(encodedStr)) + '#' + encodedStr
        return result

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        res, wordBlockStart = [], 0

        while wordBlockStart < len(str):
            delimiterIndex = wordBlockStart
            while str[delimiterIndex] != "#":
                delimiterIndex += 1
            length = int(str[wordBlockStart:delimiterIndex])
            res.append(str[delimiterIndex + 1: delimiterIndex + 1 + length])
            wordBlockStart = delimiterIndex + 1 + lengthlo

        return res
