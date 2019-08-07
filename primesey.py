#!/usr/bin/env python3

###
# Name: Evan A Walker, Kristaaaa, Ehsan
# Student ID: 01932978 , kristaIDHere, EhsanIDHere
# Email: walke208@mail.chapman.edu , kristaEmailHere , ehsanEmailHere
# Course: CS510 Fall 2017
# Assignment: Classwork 4
###


import sys


def eratosthenes(n):
    """
    this fxn is the Sieve of Eratosthenes. 
    this algorithm generates a list of positive integers up to a given input n,
    then removes all multiples of 2, then 3,then 4, and so on until only the numbers
    that are divisible by 1 and itself are left in the list. and therefore the list only
    consists of all the primes less than or equal to n
    Args:
        n (int): positive integer parameter. where n>1
    Returns:
        prime_list (list): a list of all prime numbers less than or equal to n
    """
    assert n>1                                       #asserting n be a positive integer
    prime_list = []
    for i in range(2,n+1):                             #fills prime_list with all integers  2 <= i <= n
        prime_list.append(i)
    multiple = 2                                     #set to 2 because if set to 1 it will remove all elements from the list
    while multiple <= n/multiple:
        count = 2                                    #set to 2 because if set to 1 it will remove the prime itself from the list
        while count <= n/multiple:
            if count*multiple in prime_list:         #checks if count*multiple is in list. needed because it could have already been removed
                prime_list.remove(count*multiple)    #removes count*multiple
            count = count + 1
        multiple = multiple + 1
    #print(prime_list)   #for testing only
    return prime_list







def gen_eratosthenes():
    """
    this fxn is a generator for genPrimes(int n). 
    yields n where n is the next prime.
    see also genPrimes(int n)
    Args:
        none
    Yields:
        n (int): where n is the next prime
    """
    n=3
    yield 2
    while True:
        count = 2               #set count to 2 because if count=1; all numbers are divisible by 1, so it is not a case we need to check
        this = True
        while count < n/2 + 1:  #set to n/2 + 1 so that the amount of times iterated is minimized.
            if n%count == 0:    #i.e. if n is divisble by count, then n is not prime
                count = n       #ends this loop; if n is not prime, there is no reason to continue the loop
                this = False
            count += 1
        if this == True:        #i.e. if this == True, then we know that the while loop was completely executed and n has no divisors except 1 and n
            yield n             #yield n since it went through the entire loop without finding divisors
        n += 1                  #increment n to see if n+1 is prime. will continue incrimenting until another prime is found and yields it

def genPrimes(n):
    """
    this fxn, utilizing gen_eratosthenes(), will create a list
    of all prime numbers less than an input n.
    see also eratosthenes(int n).
    Args:
        n (int): positive integer parameter. where n>1
    Returns:
        prime_list (list): a list of all prime numbers 
                           less than or equal to n utilizing a generating fxn
    """
    assert n>1
    p = gen_eratosthenes()
    prime_list = []
    prime_list.append(next(p))
    while n > prime_list[len(prime_list)-1]:        #while input is less than the last term in the prime list
        prime_list.append(next(p))                  #adds next term from generator
    if n < prime_list[len(prime_list)-1]:           #deletes last term
        del prime_list[len(prime_list)-1]
    #print(prime_list)  #for testing only
    return prime_list







#the next 5 fxns are experimenting with other ways to generate primes

def evansMod(x,n):
    """
    this fxn flips a modulus value from 0 to 1, or from any integer x to 0 where x != 0
    Args:
        n (int): positive integer parameter. where n>1
        x (int): positive integer parameter
    Returns:
        1 (int): if n divides x
        0 (int): if n does not divide x
    """
    if x%n == 0:
        return 1
    else:
        return 0


def evansPrimes(n):
    """
    made this fxn over summer trying to find a fxn that would return perfect 
    numbers and the kernel of the fxn would be the set of all primes,
    however, it was computationally extensive and not easy to evaluate. 
    might as well test its effieciency versus the other prime number generators
    in this fxn g(x), x is a perfect number if g(x) = x (idempotent),
    and prime if g(x) = 1 (kernel).
    which is why below sums == 1, then i is prime
    Args:
        n (int): positive integer parameter. where n>1
    Returns:
        prime (list): a list of all prime numbers less than or equal to n
    """
    assert n>1
    primes = []
    for i in range(1,n+1):
        sums = 0
        for j in range(1,i):
            sums += evansMod(i,j)*j
        if sums == 1:
            primes.append(i)
    #print(primes)  #for testing only
    return primes

def evansPerfectNumbers(n):
    """
    made this fxn over summer trying to find a fxn that would return perfect numbers
    and the kernel of the fxn would be the set of all primes,
    however, it was computationally extensive and not easy to evaluate.
    might as well test its effieciency versus the other prime number generators
    in this fxn g(x), x is a perfect number if g(x) = x (idempotent), 
    and prime if g(x) = 1 (kernel). 
    which is why below sums == i, then i is perfect
    perfect numbers are numbers where the sum of the divsors is equal to the number,
    i.e 6=1+2+3, 1|6 & 2|6 & 3|6
    Args:
        n (int): positive integer parameter. where n>1
    Returns:
        perfect (list): a list of all perfect numbers less than or equal to n
    """
    assert n>1
    perfect = []
    for i in range(1,n+1):
        sums = 0
        for j in range(1,i):
            sums += evansMod(i,j)*j
        if sums == i:
            perfect.append(i)
    #print(perfect)  #for testing only
    return perfect





def gen_evanPrimes():
    """
    Args:
        none
    Yields:
        n (int): where n is the next prime
    """
    n=1
    while True:
        sums = 0
        for j in range(1,n):
                sums += evansMod(n,j)*j
        if sums == 1:
            yield n
        n+=1

def genevanPrimes(n):
    """
    Args:
        n (int): positive integer parameter. where n>1
    Returns:
        prime_list (list): a list of all prime numbers 
                           less than or equal to n utilizing a generating fxn
    """
    assert n>1
    p = gen_evanPrimes()
    prime_list = []
    prime_list.append(next(p))
    while n > prime_list[len(prime_list)-1]:        #while input is less than the last term in the prime list
        prime_list.append(next(p))                  #adds next term from generator
    if n < prime_list[len(prime_list)-1]:           #deletes last term
        del prime_list[len(prime_list)-1]
    #print(prime_list)  #for testing only
    return prime_list


if __name__ == "__main__":
    import sys
    #eratosthenes(int(sys.argv[1]))
    #genPrimes(int(sys.argv[1]))
    #evansPrimes(int(sys.argv[1]))
    #genevanPrimes(int(sys.argv[1]))