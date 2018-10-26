class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = s.strip()

        if len(s) == 0:
            return ""

        word = None
        word_list = []
        for idx,l in enumerate(s):
            if not l == " " and not word:
                word= l

            elif not l == " ":
               word =  word + l

            elif l == " ":
                if word:
                    word_list.append(word)
                word = None

            if idx == len(s)-1:
                word_list.append(word)

        return self.joinWithSpace(self.reverseList(word_list))
    
    def reverseList(self,l):

        length = len(l)
        new_list = [None] * length

        new_idx = length - 1
        for i in l:
           new_list[new_idx]  = i
           new_idx -= 1
        return new_list

    def joinWithSpace(self,l):

        s = ""
        first = True
        for i in l:
            if first:
                s = s + str(i)
                first = False
            else:
                s = s + " " + str(i)
        return s
            


s = Solution()
test = "A man, a plan, a canal: Panama"
test2 = "a"
print(s.reverseWords(test2))
