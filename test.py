alphabet = 'abcdefghijklmnopqrstuvwxyz'


def edits1(word):
    n = len(word)
    print([word[0:i] + c + word[i:] for i in range(n + 1) for c in alphabet])
    # result = set([word[0:i] + word[i + 1:] for i in range(n)] +  # deletion
    #              [word[0:i] + word[i + 1] + word[i] + word[i + 2:] for i in range(n - 1)] +  # transposition
    #              [word[0:i] + c + word[i + 1:] for i in range(n) for c in alphabet] +  # alteration
    #              [word[0:i] + c + word[i:] for i in range(n + 1) for c in alphabet])  # insertion
    # return result


edits1("learn")
