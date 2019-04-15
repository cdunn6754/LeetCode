class Solution:
    def customSortString(self, S: str, T: str) -> str:
        order = collections.defaultdict(lambda : -1)
        
        for idx,char in enumerate(S):
            order[char] = idx
        
        T_list = list(T)
        get_order = lambda idx: order[T_list[idx]]
        
        for _ in range(0,len(T)):
            lo_idx = 0
            hi_idx = 1   
            
            while hi_idx < len(T):
                lo_order = get_order(lo_idx)
                hi_order = get_order(hi_idx)

                if lo_order > hi_order:
                    T_list[lo_idx], T_list[hi_idx] = T_list[hi_idx], T_list[lo_idx]

                lo_idx += 1
                hi_idx += 1
                
        return "".join(T_list)
