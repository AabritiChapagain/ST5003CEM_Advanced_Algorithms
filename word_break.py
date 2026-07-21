def word_break(s, word_dict):
    """
    Determines if a string can be segmented into valid dictionary words
    using Dynamic Programming.
    """

    n = len(s)

    # dp[i] is True if s[:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]


if __name__ == "__main__":

    dictionary = {
        "apple",
        "pen",
        "cat",
        "cats",
        "and",
        "sand",
        "dog"
    }

    string1 = "applepenapple"
    string2 = "catsanddog"
    string3 = "applecatdog"
    string4 = "applecar"

    print(string1, ":", word_break(string1, dictionary))
    print(string2, ":", word_break(string2, dictionary))
    print(string3, ":", word_break(string3, dictionary))
    print(string4, ":", word_break(string4, dictionary))