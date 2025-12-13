def mergesort(arr, start, end):
            if end - start + 1 <= 1:
                return arr
            middle = (end+start)//2
            mergesort(arr, start, middle)
            mergesort(arr, middle+1, end)
            merge(arr, start, middle, end)
            return arr
def merge(arr, start, middle, end):
            L = arr[start:middle+1]
            R = arr[middle+1: end+1]
            i = 0
            j = 0
            k = start
            while i<len(L) and j < len(R):
                if L[i]<=R[j]:
                    arr[k]=L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1
            while i < len(L):
                arr[k]=L[i]
                i+=1
                k+=1
            while j < len(R):
                arr[k] = R[j]
                j+=1
                k+=1