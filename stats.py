def get_word_count(text: str) -> int:
    word_count = len(text.split())
    return word_count


def print_word_count(text: str):
    word_count = get_word_count(text)
    line = f"{word_count} words found in the document"
    print(line)


def get_char_count(text: str):
    counter: dict[str, int] = {}
    for c in text.lower():
        counter[c] = counter.get(c, 0) + 1
    return counter


def sort_char_count(counter: dict[str, int]) -> list[dict[str, int]]:
    def sort_key(dictionary):
        (v,) = dictionary.values()
        return v

    count_list = [{k: v} for k, v in counter.items()]
    count_list.sort(reverse=True, key=sort_key)
    return count_list


def print_char_count(text: str):
    counter = get_char_count(text)
    sorted_chars = sort_char_count(counter)
    for pair in sorted_chars:
        key, = pair.keys()
        if not key.isalpha():
            continue
        print(f'{key}: {pair[key]}')
