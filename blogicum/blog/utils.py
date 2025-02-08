from .constants import STR_LIMIT


def truncate_string(value: str, limit: int = STR_LIMIT) -> str:
    return value[:limit] + ('...' if len(value) > limit else '')
