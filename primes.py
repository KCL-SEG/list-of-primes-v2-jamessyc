def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError()
    list = [2]
    i = 3
    while i and len(list) < number_of_primes:
        if is_prime(i):
            list.append(i)
        i += 1        
    return list

def is_prime(num):
    for i in range(1, num):
        if num % i == 0 and i != num and i != 1:
            return False
    return True