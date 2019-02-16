class Solution:

    def all_same(self, tup):
        for idx,_ in enumerate(tup):
            if tup[idx-1] != tup[idx]:
                return False
        return True
            
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        z_itr = zip(*strs)

        common_list = []
        for tup in z_itr:
            if not self.all_same(tup):
                break
            common_list.append(tup[0])

        return ''.join(common_list)
        


sol = Solution()

# same_tests = [
#     (1,1,1),
#     (1,2,3),
#     (3,1),
#     (2,2)
# ]

# for test in same_tests:
#     print(sol.all_same(test))


tests = [
    ["apple", "appble"],
    ["", "asdf"],
    ["asdf", ""],
    ["abc", "abc", "abd"]
]

for test in tests:
    print(sol.longestCommonPrefix(test))
