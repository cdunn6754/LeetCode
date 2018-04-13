class Solution:
    def checkIfDuplicate(self, s, main_char):
        """
        Check if character main_char is duplicated within string
        s. 

        Returns: 
        If it occurs more than once return true
        otherwise return false.
        """
        counter = 0
        for char in s:
            if char == main_char:
                counter += 1
            if counter > 1:
                return True

        return False

    def getCharIdxs(self,s,main_char):
        return [idx for (idx,char) in enumerate(s) if main_char == char]

    def getPostLength(self,charIdxs):
        """
        For each occurence of main_char in s find the sub-string that follows it
        and includes only a single instance of main_char. Returns the length
        of the longest substring found. The length of the substring
        does not include the instance of the main_char itself
        """
        if len(charIdxs) <= 1:
            return len(s)
            
        max_length = 0
        for (idx_idx,idx) in enumerate(charIdxs[0:-1]):

            if idx_idx == len(charIdxs) - 2:
                length = len(s) - idx - 1
            else: 
                length = (charIdxs[idx_idx + 2] - idx) - 1
            if length > max_length:
                max_length = length

        return max_length

    def getPreLength(self,charIdxs)

            
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        unique_chars = list(set(s))

        if (len(s) == len(unique_chars)):
            return len(s)
        
        # Loop through, find the longest substring for each char
        # the shortest of those is the answer (of the chars)
        # this only catches the ss delimited by two chars (internal)
        maximum_internal_length = len(s)
        for char in unique_chars:
            new_length = self.longestInternalSubString(s, char)
            
            if new_length < maximum_internal_length:
                maximum_internal_length = new_length

        # Check to see if there is a good long string in the 
        # beginning or end (external)
        maximum_beg_length = self.longestBeginSubString(s)
        maximum_end_length = self.longestBeginSubString(s[::-1])

        return max(maximum_internal_length, maximum_beg_length, maximum_end_length)
            


        



### TESTING

s1 = Solution()

# print(s1.lengthOfLongestSubstring("asjrgapa"))
# print(s1.maxMiddleSubString("asjrgapa","a"))
s1.getPostLength("asargapdterga","a")
#print(s1.longestInternalSubString("abcb","b"))
#print(s1.longestBeginSubString("abcb"))

