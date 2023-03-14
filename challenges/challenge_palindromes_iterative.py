def is_palindrome_iterative(word):
    if not word:
        return False

    n = len(word) - 1

    for index in range(len(word) - 1):
        if word[index] != word[n]:
            return False

        if n < index:
            break

        n -= 1

    return True
