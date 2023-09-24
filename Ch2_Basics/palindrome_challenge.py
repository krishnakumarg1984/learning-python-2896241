import string

show_expected_result = False
show_hints = False


def is_palindrome(teststr: str) -> bool:
    chars_strip_table = str.maketrans("", "", string.punctuation + " ")
    cleaned_str = teststr.lower().translate(chars_strip_table)
    return cleaned_str == cleaned_str[::-1]


if __name__ == "__main__":
    # print(is_palindrome("Radar"))
    # print(is_palindrome("Race car!"))
    # print(is_palindrome("Madam, I'm Adam."))
    total = 0
    test_words = ["Hello World!", "Radar", "Mama?", "Madam, I'm Adam.", "Race car!"]
    for word in test_words:
        total += is_palindrome(word)
    print(total)
