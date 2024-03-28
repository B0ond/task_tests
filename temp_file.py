import string


def password_strength(value: str) -> str:

    if len(value) < 8:
        return 'Too weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue

    if count==3:
        return 'Very Good'
    return 'Weak' if count == 1 else 'Good'


if __name__ == '__main__':
    assert password_strength('') == 'Too weak'
    assert password_strength('1234567') == 'Too weak'
    assert password_strength('qwdfbvc') == 'Too weak'
    assert password_strength('Q5FGd4d') == 'Too weak'
    assert password_strength('Q5FGd') == 'Too weak'
    assert password_strength('12345678') == 'Weak'
    assert password_strength('123456783453453') == 'Weak'
    assert password_strength('qwertyhu') == 'Weak'
    assert password_strength('qwertyhudfgdfgd') == 'Weak'
    assert password_strength('QWERTYUH') == 'Weak'
    assert password_strength('QWERTYUIOPKUHKGH') == 'Weak'
    assert password_strength('1234QWER') == 'Good'
    assert password_strength('1234qwer') == 'Good'
    assert password_strength('1234qwerttg') == 'Good'
    assert password_strength('1234QWERTIUYT') == 'Good'
    assert password_strength('UIPOqwer') == 'Good'
    assert password_strength('JIOUHFIUHqwer') == 'Good'
    assert password_strength('123qweJHG') == 'Very Good'
    assert password_strength('1234343gF') == 'Very Good'
    assert password_strength('1234qweE') == 'Very Good'
    assert password_strength('sdfsdfsdfF1') == 'Very Good'
    assert password_strength('KJHGUYGYGh4') == 'Very Good'
