from typing import Any, Hashable, Iterator

class Dictionary:
    def __init__(self):
        self._data: dict[Hashable, Any] = {}
        self._size: int = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def put(self, key: Hashable, value: Any) -> None:
        if key not in self._data:
            self._size += 1
        self._data[key] = value

    def get(self, key: Hashable) -> Any:
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found in the dictionary.")
        return self._data[key]

    def remove(self, key: Hashable) -> None:
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found in the dictionary.")
        del self._data[key]
        self._size -= 1

    def contains_key(self, key: Hashable) -> bool:
        return key in self._data

    def contains_value(self, value: Any) -> bool:
        return value in self._data.values()

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self) -> str:
        return f"Dictionary({self._data})"

    def __getitem__(self, key: Hashable) -> Any:
        return self.get(key)

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.put(key, value)

    def __delitem__(self, key: Hashable) -> None:
        self.remove(key)

    def __contains__(self, key: Hashable) -> bool:
        return self.contains_key(key)

    def keys(self) -> Iterator[Hashable]:
        return iter(self._data.keys())

    def values(self) -> Iterator[Any]:
        return iter(self._data.values())

    def items(self) -> Iterator[tuple[Hashable, Any]]:
        return iter(self._data.items())

    def clear(self) -> None:
        self._data.clear()
        self._size = 0

if __name__ == "__main__":
    my_dict = Dictionary()


    my_dict.put("something1", "loh")
    my_dict.put("something2", 6)
    print(f"key1 is {my_dict.get('something1')}, key2 is {my_dict.get('something2')}")
    my_dict.clear()
    print("\nafter clearing:")
    if my_dict.is_empty():
        print(f"  dictionary is empty. сannot get keys or values.")
    else:
        print(f" ??? ")
    my_dict.put("something3", "test")
    print(f"testing is {my_dict.get('something3')}")

    my_dict.put("venom", "venom")
    print(f"venom is {my_dict.get('venom')}")

    my_dict.remove("something3")
    if my_dict.contains_key("something3"):
        print("that's not right")
    else:
        print(f"venom is {my_dict.contains_key('venom')}")
