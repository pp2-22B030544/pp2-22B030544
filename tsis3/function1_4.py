vetor = [2,3,4,5,11,15,23]
list = []

def filter_prime():                     
    div = 0
    i = 0
    for i in range(1, vetor[i+1]):
        if i % i == 0:
            div = div + 1
            list.append(div)
        if div == 2:
            print('The number {} is prime'(vetor[i]))
        else:
            print('The number {} is not prime'.format(vetor[i]))

print(filter_prime())