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

    def longestInternalSubString(self, s, main_char):
        """
        Given the string s and character of that string main_char, 
        find the length of the longest substring delimited
        by the character c. Length should be non-inclusive 
        so do not include second c in determination of length.

        If -1 is returned it means that main_char was not in 
        the sting s.
        """
        maximum_length = -1
        length_counter = 0
        for char in s:
            length_counter += 1
            if not char == main_char:
                continue

            elif char == main_char:
                if length_counter > maximum_length:
                    maximum_length = length_counter - 1
                length_counter = 1

        if length_counter > maximum_length:
            maximum_length = length_counter

        return maximum_length

    def longestBeginSubString(self,s):
        """
        From the beginning of the string count untill 
        an element is counted twice
        """
        length_count = 0
        previous_chars = []
        
        for char in s:
            length_count += 1
            if char in previous_chars:
                length_count -= 1
                break
            previous_chars.append(char)

        return length_count
            
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

print(s1.lengthOfLongestSubstring("asjrgapa"))
#print(s1.longestInternalSubString("abcb","b"))
#print(s1.longestBeginSubString("abcb"))

