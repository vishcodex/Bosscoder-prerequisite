# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

# For each location indices[i], do both of the following:

# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        print("Testing matrix solutions!")
        count=0
        matrix = []
        for i in range(m):
            l = []
            print("i is:", i)
            for j in range(n):
                print("j is:", j)
                l.append(0)
            matrix.append(l)
        print("matrix value is :", matrix)
        for r,c in indices:
            for k in range(n):
                matrix[r][k]+=1
            for z in range(m):
                matrix[z][c]+=1
        print("matrix value after updated", matrix)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]%2!=0:
                    count+=1
        return count


# Main function stars here
if __name__ == '__main__':
    ob = Solution()
    result = ob.oddCells(m = 2, n = 3, indices = [[0,1],[1,1]])
    print(result)