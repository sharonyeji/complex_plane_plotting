#!/usr/bin/env python3

def gen_ints():
    """Generator for the positive integers."""
    n = 2
    while True:
        yield n
        n += 1
        
def eratosthenes(n):
    #This function will take a positive integer ```n``` and return all prime numbers smaller than ```n```
    #First generate all positive sintegers less than n, starting from the number 2. Then remove all multiples of 2. 
    #Then remove all multiples of the next largest remaining (prime) number. Then repeat the last step until you reach the largest remaining number. Finally, return the set of remaining (prime) numbers. 
    
    
    listRM=[]

    g = gen_ints()
    [listRM.append(next(g)) for _ in range (1,n-2)]
  
    idxList = len(listRM)
    lenList = len(listRM) 
    largestNum = listRM[lenList-1]
   
    #remove all multiples of the next largest remaining (prime) number and repeat
    for _ in range(0, lenList-1):
        i = 0
        prime=True,
        while listRM[i] < largestNum:
            if largestNum % listRM[i] == 0:
                prime=False
                break
            else:
                prime=True        
            i += 1
            
        if prime == False:
            listRM.remove(largestNum)
            lenList -= 1
        
        idxList -= 1
        largestNum = listRM[idxList-1]

    return listRM

def prime_check(Num, primeList):
    """checking if Num is a prime by divided the element in previous primelist"""
    for primeNum in primeList:
        if Num % primeNum == 0:
            return False
        return True


def gen_eratosthenes():
    """
    generate prime number
    """
    primeList = []
    num = 2
    while True:
        primeList.append(num)
        yield num
        num = num + 1
        while prime_check(num, primeList) == False:
            num = num + 1


def main(local_argv):
    """
    local_argv is the argument list, progrom name is first arugment
    this function prints the fibonacci list calcuated by the command line argument n 
    
    """
   
    if len(local_argv) != 2:
        print("must add one and only one command argument, , exit ")
        return
        
    argument_n = int(local_argv[1]) #remember, this is the 2nd argument in command line
    
    if argument_n <= 0:
        print("please input an positive interger number, exit")
        return
    
    retList = []
    h = gen_eratosthenes()
    [retList.append(next(h)) for _ in range (0,argument_n)] #generates 1 new prime per iteration

    #retList =eratosthenes(argument_n)

    print(retList)
    return retList

# After the body of the module, you can optionally create a protected main 
# section to place executable scripting code.

if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv)
