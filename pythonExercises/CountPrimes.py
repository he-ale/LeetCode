class Solution:
    def countPrimes(self, n: int) -> int:
        if (n <= 2):
            return 0
        
        counter= 0
        i= 2
        xs= [-1]*(n+1)
        while (i*i<n):
            if(xs[i] != -1):
                i+=1
                continue
            xs[i]= i
            counter+=1
            k= i*i
            while(k<n):
                xs[k]= k
                k+=i
            i+=1
        while i<n:
            if(xs[i] == -1):
                counter+=1
            i+=1

        return counter