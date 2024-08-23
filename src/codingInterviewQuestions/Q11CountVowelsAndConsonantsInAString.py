"""Count vowels and consonants in a String"""

s = list(input('Enter String:-'))


def counter(word: list):
    vcount = 0
    ccount = 0
    for ch in range(len(word)):
        if word[ch] == 'a' or word[ch] == 'e' or word[ch] == 'i' or word[ch] == 'o' or word[ch] == 'u':
            vcount = vcount + 1
        else:
            ccount = ccount + 1

    print(f" consonants count ={ccount} and Vowels count ={vcount} ")


counter(s)
