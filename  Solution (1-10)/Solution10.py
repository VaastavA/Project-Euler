MAX_SIZE = 2000009
isprime = [True] * MAX_SIZE  
prime = []  
SPF = [None] * (MAX_SIZE)  

def manipulated_seive(N):  

    isprime[0] = isprime[1] = False
  
    for i in range(2, N):  
        if isprime[i] == True:  
            prime.append(i)  
            SPF[i] = i  
        j = 0
        while (j < len(prime) and i * prime[j] < N and prime[j] <= SPF[i]): 
          
            isprime[i * prime[j]] = False
 
            SPF[i * prime[j]] = prime[j] 
              
            j += 1
manipulated_seive(2000000)
i = 0
s = 0
while i < len(prime) and prime[i] <= 2000000: 
  s += prime[i]
  i += 1
print(s)

