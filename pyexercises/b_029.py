import re

inputs = (
    ['A', 'f', '.', 'Q', 2],
    ['.', '{', ' ^', '%', 'a'],
    [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
    ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
    list(range(1, 9)) + ['}'] + list('abcde'),  # noqa E230
    [2, '.', ',', '!']
)


def get_index_different_char(chars):
    all_alphas = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    alphas = []
    betas = []
    alpha_idx = 99
    betas_idx = 99
    for i in range(0, len(chars)):
        this_test = str(chars[i])
        if this_test in all_alphas:
            alphas += this_test
            alpha_idx = i
        else:
            betas += this_test
            betas_idx = i
    if len(alphas) < len(betas):
        return alpha_idx
    else:
        return betas_idx


# tests
def test_wrong_char():
    inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1,9)) + ['}'] + list('abcde'),  # noqa E230
        [2, '.', ',', '!']
    )
    expected = [2, 4, 1, 5, 8, 0]

    for arg, exp in zip(inputs, expected):
        err = f'get_index_different_char({arg}) should return index {exp}'
        assert get_index_different_char(arg) == exp, err

test_wrong_char()