#Enhance your coding skills, start writing your code here!!
def SieveOfEratosthenes(num):
    prime = [True for _ in range(num + 1)]
    primes = []
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, num + 1):
        if prime[p]:
            primes.append(p)
    return primes

primes=SieveOfEratosthenes(10**4)
l=int(input())
m=int(input())
for i in primes:
  if i>=l and i<=m:
    print(i)
