def get_doubled_int(num: int) -> int:
    return num * 2


def wrapper__get_doubled_int(num: int) -> int:
    return __get_doubled_int(num)


def __get_doubled_int(num: int) -> int:
    return num * 2


class KeyHolder:
    def get_first_key(self, prefix: str) -> str:
        return f'{prefix}_real_key'

    def get_second_key(self, prefix: str) -> str:
        return f'{prefix}_real_second_key'

    def get_private_method(self) -> str:
        return self.__private_method()

    def __private_method(self) -> str:
        return '__private_method'
