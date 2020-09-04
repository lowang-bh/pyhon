#!/usr/bin/env python

import unittest
"""
Given an array of strings arr.
String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""


class Solution(object):
    def maxLengthAndStr(self, arr):
        """
        :type arr: List[str]
        :rtype: int, str
        """
        if not arr:
            return 0, ""

        if len(arr) == 1:
            return len(arr[0]), arr[0]
        elif len(arr) == 2:
            if self.NoDuplicateChar(arr[0], arr[1]):
                return len(arr[0]) + len(arr[1]), arr[0]+arr[1]
            else:
                #return len(arr[0]) if len(arr[0]) >= len(arr[1]) else len(arr[1])
                if len(arr[0]) >= len(arr[1]):
                    return len(arr[0]), arr[0]
                else:
                    return len(arr[1]), arr[1]

        maxlen, maxstr = len(arr[0]), arr[0]
        for index in xrange(0, len(arr)):
            str = arr[index]
            
            sub_max, sub_max_str  = self.maxLengthAndStr(arr[:index] + arr[index+1:])
            if self.NoDuplicateChar(str, sub_max_str):
                if len(str) + sub_max > maxlen :
                    maxlen, maxstr = len(str) + sub_max, sub_max_str+str
            else:
                if max(len(str), sub_max) > maxlen:
                    if len(str) > sub_max:
                        maxlen, maxstr = len(str), str
                    else:
                        maxlen, maxstr = sub_max, sub_max_str

        return maxlen, maxstr

    def generate_bits(self, arr):
        bits = {}
        for word in arr:
            bit = 0
            for ch in word:
                mask = (1 << (ord(ch) - ord('a')))
                if (bit & mask) != 0:
                    break
                else:
                    bit |= mask
            else:
                bits[word] = bit
        return bits

    def maxLength(self, arr):
        # arr[i] will not be in bits if it contains duplicate characters
        bits = self.generate_bits(arr)
        l = 0
        n = len(arr)
        # generate all subsets
        for i in xrange(2**n):
            cur_len = 0
            cur_bits = 0
            for j in range(n):
                if (i&(1<<j)) != 0:
                    # check that there's no overlap
                    if arr[j] not in bits or (cur_bits & bits[arr[j]]) != 0:
                        break
                    cur_bits |= bits[arr[j]]
                    cur_len += len(arr[j])
            else:
                l = max(l, cur_len)
        return l
    def NoDuplicateChar(self, s1, s2):
        return len(s1) + len(s2) == len(set("".join([s1,s2])))

    def maxLength2(self, arr):
        return self.maxLengthAndStr(arr)[0]

class SolutionMaxLenthTestCase(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def test_case_null(self):
        self.assertEqual(self.s.maxLength([]), 0)
        self.assertEqual(self.s.maxLength([""]), 0)

    def test_case_one(self):
        self.assertEqual(self.s.maxLength(["a"]), 1)
        self.assertEqual(self.s.maxLength(["a","a"]), 1)
        self.assertEqual(self.s.maxLength(["a","a", "a"]), 1)
        self.assertEqual(self.s.maxLength(["abcdefghijklmnopqrstuvwxyz","a", "a"]), 26)

    def test_case_common(self):
        self.assertEqual(self.s.maxLength(["a", "b", "c"]), 3)
        self.assertEqual(self.s.maxLength(["ab", "cd", "ef"]), 6)
        self.assertEqual(self.s.maxLength(["ab", "bc", "def"]), 5)
        self.assertEqual(self.s.maxLength(["un", "iq", "ue"]), 4)
        self.assertEqual(self.s.maxLength(["abc", "bcd", "efg"]), 6)
        self.assertEqual(self.s.maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]),16)
        self.assertEqual(self.s.maxLength(["abcdefghijklm","bcdefghijklmn","cdefghijklmno","defghijklmnop",
                                          "efghijklmnopq","fghijklmnopqr","ghijklmnopqrs","hijklmnopqrst",
                                          "ijklmnopqrstu","jklmnopqrstuv","klmnopqrstuvw","lmnopqrstuvwx",
                                          "mnopqrstuvwxy","nopqrstuvwxyz","opqrstuvwxyza","pqrstuvwxyzab"]), 26)

if __name__ == "__main__":
    #unittest.main()
    s=Solution()
    print(s.maxLengthAndStr(["ab","bc","cd"]))
    #print(s.maxLengthAndStr(["a","b","c","d","e","f","g","h","i","j","k","l","m","n", "o","p"]))
    print(s.maxLengthAndStr(["abcdefghijklm","bcdefghijklmn","cdefghijklmno","defghijklmnop",
                       "efghijklmnopq","fghijklmnopqr","ghijklmnopqrs","hijklmnopqrst",
                       "ijklmnopqrstu","jklmnopqrstuv","klmnopqrstuvw","lmnopqrstuvwx",
                       "mnopqrstuvwxy","nopqrstuvwxyz","opqrstuvwxyza","pqrstuvwxyzab"]))
