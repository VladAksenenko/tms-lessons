import re


def is_date(number: str) -> bool:
    return re.fullmatch(r'\d+\.\d+', number) is not None


assert is_date("1.0")
assert not is_date("2.5")
assert is_date("22")