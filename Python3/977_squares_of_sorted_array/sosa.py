class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        pos_pointer = len(A)
        squares = []
        
        for idx, num in enumerate(A):
            if num >= 0:
                pos_pointer = idx
                break
                
        neg_pointer = pos_pointer - 1
        
        while neg_pointer >= 0 and pos_pointer < len(A):
            print(neg_pointer)
            neg_num = A[neg_pointer]**2
            pos_num = A[pos_pointer]**2
            
            if pos_num < neg_num:
                squares.append(pos_num)
                pos_pointer += 1
            if neg_num <= pos_num:
                squares.append(neg_num)
                neg_pointer -= 1
                
        for neg_pointer in range(neg_pointer, -1, -1):
            neg_num = A[neg_pointer]**2
            squares.append(neg_num)
            
        for pos_pointer in range(pos_pointer, len(A)):
            pos_num = A[pos_pointer]**2
            squares.append(pos_num)
            
        return squares
