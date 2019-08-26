def permutations(word):
    if len(word) == 1:
        return [word]
    else:
        result = []
        for p in permutations(word[1:]):
            print(p, word[1:])
            print("\n")
            for i in range(len(word)):
                print(i, "1" + p[:i], "2" + word[0:1], "3" + p[i:])
                current_p = p[:i] + word[0:1] + p[i:]
                result.append(current_p)

    return result


given_input = "bc"
print(permutations(given_input))
