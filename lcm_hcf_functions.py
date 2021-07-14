def factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
        else:
            continue
    
    return factors

def prime(lists):
    primefac = []
    for i in lists:
        foff = []
        for l in range(1, i + 1):
            if i % l == 0:
                foff.append(l)
            else:
                continue
        if len(foff) <= 2:
            primefac.append(i)
        else:
            continue
    primefac.pop(0)
    return primefac

#list_of_prime_factors is the list of prime factors of the number
def primfactorisation(number, list_of_prime_factors):
    primefactoriationorder = []
    prime_index = 0
    while number != 1:
        if number % list_of_prime_factors[prime_index] == 0:
            number = number / list_of_prime_factors[prime_index]
            primefactoriationorder.append(list_of_prime_factors[prime_index])
            continue
        else:
            prime_index += 1
            continue
    
    return primefactoriationorder

#nos1_list is the prime factorisation list of number 1
#nos2_list is the prime factorisation list of number 2
def hcf_and_lcm(nos1_list, nos2_list):
    nos1_set = set(nos1_list)
    nos2_set = set(nos2_list)
    common_factors = nos1_set.intersection(nos2_set)
    hcf = max(common_factors)
    no1 = 1
    no2 = 1
    for i in nos1_list:
        no1 = no1 * i
    for l in nos2_list:
        no2 = no2 * l
    lcm = (no1 * no2) // hcf
    return hcf, lcm
