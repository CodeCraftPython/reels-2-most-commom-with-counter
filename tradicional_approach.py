from typing import List, Union, Any


def get_most_commom(data: Union[List[Any], str]):
    counter = {}
    for x in data:
        if x in counter:
            counter[x] += 1
        else:
            counter[x] = 1

    most_commom = max(counter, key=counter.get)
    return most_commom

if __name__ == '__main__':
    text = 'python is a programming language' \
           'used by junior and senior developers'

    fruits = ['apple', 'orange', 'pineapple', 'orange',
              'apple', 'apple']

    most_commom_char = get_most_commom(text)
    most_commom_fruit = get_most_commom(fruits)

    print(f"Most commom char: '{most_commom_char}'")
    print(f"Most commom fruit: '{most_commom_fruit}'")