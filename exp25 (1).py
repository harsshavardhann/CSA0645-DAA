def stringMatching(words):
    result = []

    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break

    return result


# Example 1
words1 = ["mass", "as", "hero", "superhero"]
print(stringMatching(words1))

# Example 2
words2 = ["leetcode", "et", "code"]
print(stringMatching(words2))

# Example 3
words3 = ["blue", "green", "bu"]
print(stringMatching(words3))
