
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s.replace(" ", "")
        t.replace(" ", "")

        if not len(t) == len(s):
            return False

        s_dict = {}

        for letter in s:
            if letter in s_dict.keys():
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        t_dict = {}
        for letter in t:
            if letter in t_dict.keys():
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1


        if t_dict == s_dict:
            return True
            
        return False
