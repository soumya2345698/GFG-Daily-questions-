class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        col=len(matrix[0])
        row=len(matrix)
        count=0
        ans=[]
        startingRow=0
        endingRow=row-1
        startingCol=0
        endingCol=col-1

        count=0


        while count<row*col:
            #firstRowLeftToRight
            for i in range(startingCol, endingCol+1):
                ans.append(matrix[startingRow][i])
                count+=1
            startingRow+=1
            for j in range(startingRow, endingRow+1):
                ans.append(matrix[j][endingCol])
                count+=1
            endingCol-=1
            if startingRow <= endingRow:
                for k in range(endingCol,startingCol-1,-1 ):
                    ans.append(matrix[endingRow][k])
                    count+=1
                endingRow-=1
            if startingCol <= endingCol:
                for l in range(endingRow,startingRow-1,-1 ):
                    ans.append(matrix[l][startingCol])
                    count+=1
                startingCol+=1
        return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends