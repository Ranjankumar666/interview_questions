class  DS:
    def __init__(self, vals):
        self.prefix = self.prefixProduct(vals)
        self.suffix = self.suffixProduct(vals)


    def prefixProduct(self, A):
        n = len(A)
        psum = [1]*(n)
        psum[0] = A[0]
        
        for i in range(1, n):
            psum[i] = A[i]  * psum[i-1]
        
        
        return psum



    def suffixProduct(self, A):
        n = len(A)
        ssum =[1]*(n)
        ssum[n-1] = A[n-1]
        
        for i in range(n-2, -1, -1):
            ssum[i] = ssum[i+1] * A[i]

        return ssum 

arr = [1, 2, 3, 4]
ds = DS(arr)
res = [1]*len(arr)

for i, val in enumerate(arr):
    if (i+1  != len(arr)):
         res[i] *= ds.suffix[i+1] 
    if i-1 >= 0:
        res[i] *= ds.prefix[i-1]
    
print(res)