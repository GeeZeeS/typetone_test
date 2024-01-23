from random import choice
from string import ascii_letters, digits


def validate_shortcode(shortcode: str) -> bool:
    if len(shortcode) != 6 or not all(c.isalnum() or c == "_" for c in shortcode):
        return False
    return True


def generate_shortcode() -> str:
    characters = ascii_letters + digits + "_"
    return "".join(choice(characters) for _ in range(6))
