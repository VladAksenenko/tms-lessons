import re


def is_date(number: str) -> bool:
    return re.fullmatch(r'\d\d-\d\d-\d\d\d\d', number) is not None


assert is_date("01-12-2022")
assert not is_date("12-12-2023")
assert is_date("01-12-20")

