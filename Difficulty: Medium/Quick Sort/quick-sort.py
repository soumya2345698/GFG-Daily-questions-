#User function Template for python3

class Solution:
    def quickSort(self,arr,low,high):
        if(low<high):
            n = self.partition(arr,low,high)
            self.quickSort(arr, low, n-1)
            self.quickSort(arr, n+1, high)
    
    def partition(self,arr,low,high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if(arr[j] < pivot):
                i+=1
                arr[i], arr[j] = arr[j], arr[i]     
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

        print("~")
# } Driver Code Ends