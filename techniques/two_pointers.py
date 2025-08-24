def is_palindrome(word: str) -> bool:
    if len(word) < 2:
        return True
    right_pointer = len(word) - 1
    left_pointer = 0
    while left_pointer < right_pointer:
        if word[right_pointer] != word[left_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    return True


def test_is_palindrome():
    arguments = [
        '',
        'a',
        'am'
        'madam',
        'rotator',
        'car',
        'engage'
    ]
    expected_results = [
        True,
        True,
        False,
        True,
        True,
        True,
        False,
    ]
    for arg, res in zip(arguments, expected_results):
        curr = is_palindrome(arg)
        assert curr == res, f'{curr} != {res}'
