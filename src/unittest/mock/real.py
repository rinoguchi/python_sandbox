def get_doubled_int(num: int) -> int:
    return num * 2


class KeyHolder:
    def get_first_key(self, prefix: str) -> str:
        return f'{prefix}_real_key'

    def get_second_key(self, prefix: str) -> str:
        return f'{prefix}_real_second_key'
