"""
A version of this was given to me during a triplebyte test. They suggested looking 
up the algorithm. That's what I did, I failed miserably during the test but decided 
to come back and try it out here. The w_* functions are not necessary for this
particular task but seemed like an easy design addition in case you want to use
different weight functions.
"""

class Solution:

    def w_del(self, c):
        return 1
    def w_ins(self, c):
        return 1
    def w_subs(self, c1, c2):
        return 1
    
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':

        self.d = [ [None for x in range(len(word1) + 1)] for x in range(len(word2) + 1)]
        self.word1 = word1
        self.word2=word2

        self.d[0][0] = 0
        for idx,_ in enumerate(word2):
            self.d[idx+1][0] = sum(map(self.w_del, word2[0:idx+1]))

        for idx,_ in enumerate(word1):
            self.d[0][idx+1] = sum(map(self.w_ins, word1[0:idx+1]))

        
        self.find_d(len(word2),len(word1))
        return self.d[len(word2)][len(word1)]

    def find_d(self, i, j):
        if self.d[i][j] != None:
            return self.d[i][j]
        
        a = self.word1[j-1]
        b = self.word2[i-1]

        if a == b:
            self.d[i][j] = self.find_d(i-1, j-1)
        else:
            self.d[i][j] = min(
                self.find_d(i-1,j) + self.w_del(b),
                self.find_d(i, j-1) + self.w_ins(a),
                self.find_d(i-1, j-1) + self.w_subs(a,b)
            )
        return self.d[i][j]    

def print_matrix(mat):
    for row in mat:
        print(row)
        
sol = Solution()


tests = [
    ("horse", "ros"),
]

for test in tests:
    print(sol.minDistance(*test))
