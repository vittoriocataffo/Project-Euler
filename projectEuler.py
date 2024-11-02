### Problem 1
def MultipleOf3Or5(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum
#print(MultipleOf3Or5(1000))

### Problem 2
def EvenFibonacciNumbers(n):
    fib = [1,2]
    while(1):
        if fib[-1]+fib[-2] <= n:
            fib.append(fib[-1]+fib[-2])
        else:
            break
    sum = 0
    for i in fib:
        if i%2 == 0:
            sum += i
    return sum
#print(EvenFibonacciNumbers(4000000))

def factorsOf(n):
    factors = []
    for i in range(1,int(n**0.5+1)):
        if n % i == 0:
            factors.append(i)
            if i != n//i:
                factors.append(n//i)
    return factors 
#print(factorsOf(600851475143))

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    end = int(n**0.5)+1
    for i in range(3,end,2):
        if n%i == 0:
            return False
    else:
        return True
#print(isPrime(4))

### Problem 3
def LargestPrimeFactor(n):
    factors = factorsOf(n)
    primeFactors = []
    for i in factors:
        if isPrime(i):
            primeFactors.append(i)
    return max(primeFactors)
#print(LargestPrimeFactor(600851475143))

### Problem 4
def LargestPalindromeProduct():
    largest = 1
    for j in range(1,1000):
        for k in range (1,1000):
            product = j*k
            if isPalindrome(product) and product > largest:
                largest = product
    return largest
#print(LargestPalindromeProduct())

### Problem 5
def SmallestMultiple(n):
    smallest = 1
    for i in range(1,n+1):
        if(isPrime(i) or i == 1):
            smallest = smallest*i
        else:
            if(smallest%i!=0):
                if(i%2==0):
                    smallest*=2
                else: smallest*=3
    return smallest
#print(SmallestMultiple(20))

### Problem 6
def SumSquareDifference(n):
    sumOfSquare = 0
    sum = 0
    for i in range(1,n+1):
        sumOfSquare += i**2
        sum += i
    squareOfSum = sum**2
    return squareOfSum - sumOfSquare
#print(SumSquareDifference(100))

### Problem 7
def NthPrimeNumber(n):
    if n == 1:
        return 2
    count = 1
    i = 3
    while(1):
        if isPrime(i):
            count += 1
            if count == n:
                return i
        i += 2
#print(NthPrimeNumber(10001))

### Problem 8
number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
def LargestProductInASeries(n,number):
    largest = 0
    number = str(number)
    for i in range(len(number)-n):
        product = 1
        for j in range(n):
            product = product*int(number[i+j])
        if product > largest:
            largest = product
    return largest
#print(LargestProductInASeries(13,number))

### Problem 9
def SpecialPythagoreanTriplet(n):
    for i in range(n//2):
        for j in range(i+1,n//2):
            c = (i**2 + j**2)**0.5
            if i + j + c == n:
                return int(i*j*c)
#print(SpecialPythagoreanTriplet(1000))

def isPalindrome(n):
    n = str(n)
    for i in range(1,len(n)//2+1):
        if n[i-1] != n[-i]:
            return False
    else:
        return True
#print(isPalindrome(9009))

### Problem 10
def SummationOfPrime(n):
    sum = 2
    prime = 3
    while(prime < n):
        if isPrime(prime):
            sum = sum + prime
        prime += 2
    return sum
#print(SummationOfPrime(2000000))

### Problem 11
grid = [[8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
def LargestProductInAGrid(grid,n):
    largest = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            #rows
            if(j < len(grid)-n-1):
                product = 1
                for k in range(n):
                    product = product*grid[i][j+k]
                largest = max(largest, product)
                #right diagonal
                if(i < len(grid)-n-1):
                    product = 1
                    for k in range(n):
                        product = product*grid[i+k][j+k]
                    largest = max(largest, product)
            #columns
            if(i < len(grid)-n-1):
                product = 1
                for k in range(n):
                    product = product*grid[i+k][j]
                largest = max(largest, product)
                #left diagonal
                if(j>=n-1):
                    product = 1
                    for k in range(n):
                        product = product*grid[i+k][j-k]
                    largest = max(largest, product) 
    return largest
#print(LargestProductInAGrid(grid,4))

### Problem 12
def HighlyDivisibleTriangularNumber(n):
    triangleNumbers = []
    numFactors = 1
    i = 1
    while(1):
        triangleNumber = sum(range(1,i+1))
        triangleNumbers.append(triangleNumber)
        factors = factorsOf(triangleNumber)
        numFactors = len(factors)
        if (numFactors>n):
            break
        i = i+1
    return triangleNumbers[-1]
#print(HighlyDivisibleTriangularNumber(500))

def LargeSum(n):
    pass

### Problem 14
def LongestCollatzSequence(n):
    chain = []
    lenLongestChain = 1
    iTarget = 1
    for i in range(2,n+1):
        chain.append(i)
        while(i != 1):
            if (i%2 == 0):
                i = i//2
                chain.append(i)
            else:
                i = 3*i + 1
                chain.append(i)
        #print(chain)
        if (len(chain) > lenLongestChain):
            lenLongestChain = len(chain)
            iTarget = chain[0]
        chain.clear()
    return iTarget
#print(LongestCollatzSequence(1000000))

def LatticePaths():
    pass