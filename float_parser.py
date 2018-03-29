# helpers
def get_absolute_str(value):
    is_negative = False
    stripped_value = value
    if value[0] == '-':
        is_negative = True
        stripped_value = value[1:]

    return is_negative, stripped_value


def get_exponent(value):
    finished_exponent = 0
    stripped_val = value

    for idx, char in enumerate(value):
        if char.lower() == 'e':
            exp_str = value[idx+1:]
            stripped_val = value[:idx]

            is_negative, absolute_exp = get_absolute_str(exp_str)
            exponent_digits = get_digits(absolute_exp)
            exponent_value = get_value_from_digits(exponent_digits)

            if is_negative:
                finished_exponent = -exponent_value
            else:
                finished_exponent = exponent_value

    return finished_exponent, stripped_val


def get_decimal_count(val):
    decimal_count = 0

    decimal_idx = val.find('.')
    if decimal_idx >= 0: # for case that val[0] == '.', e.g. val = '.34'
        decimal_count = len(val[decimal_idx + 1:])

    return decimal_count


def get_digits(val):
    integers = []
    for char in val:
        if char == '.':
            continue
        integers.append(parse_digit(char))

    return integers


def get_value_from_digits(digits):
    power = len(digits) - 1
    total = 0
    for digit in digits:
        total += (digit * 10 ** power)
        power -= 1

    return total


def parse_digit(digit):
    if digit == u"1":
        return 1
    if digit == u"2":
        return 2
    if digit == u"3":
        return 3
    if digit == u"4":
        return 4
    if digit == u"5":
        return 5
    if digit == u"6":
        return 6
    if digit == u"7":
        return 7
    if digit == u"8":
        return 8
    if digit == u"9":
        return 9
    if digit == u"0":
        return 0

# main
def parse_float(value):
    is_negative, absolute_value = get_absolute_str(value)
    exponent, value_sans_exponent = get_exponent(absolute_value)
    decimal_count = get_decimal_count(value_sans_exponent)
    digits = get_digits(value_sans_exponent)
    temp_total = get_value_from_digits(digits)

    if decimal_count:
        exponent -= decimal_count

    adjuster = 10 ** abs(exponent) * 1.0

    if exponent == 0:
        total = temp_total
    elif exponent < 0:
        total = temp_total / adjuster
    else:
        total = temp_total * adjuster

    if is_negative:
        return -total
    else:
        return total

# tests
assert parse_float("1") == 1
assert parse_float("123") == 123
assert parse_float("3502940") == 3502940
assert parse_float("01") == 1
assert parse_float("002703") == 2703
assert parse_float("-123") == -123
assert parse_float("-003920") == -3920
assert parse_float("0.34") == 0.34
assert parse_float("3.0012") == 3.0012
assert parse_float("1503.2001") == 1503.2001
assert parse_float("-250.0") == -250
assert parse_float("-355.4920") == -355.492
assert parse_float("3748e-123") == 3.748e-120
assert parse_float("-000.23E-20") == -2.3e-21