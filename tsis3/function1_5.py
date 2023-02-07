def permutations(word, permutation=''):
     
    if len(word) == 0:
        print(permutation)
 
    for i in range(len(word)):
 
        newpermu = permutation + word[i]
        newword = word[0:i] + word[i+1:]
 
        permutations(newword, newpermu)
 
 
if __name__ == '__main__':
 
    s = 'Zhanel'
    permutations(s)