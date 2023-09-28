from collections import Counter

if __name__ == '__main__':
    text = 'python is a programming language used by' \
           'junior and senior developers'

    fruits = ['orange', 'apple', 'pineapple', 'oange',
              'apple', 'apple']

    char_count = Counter(text)
    fruits_count = Counter(fruits)

    most_commom_char = char_count.most_common(1)[0]
    most_commom_fruit = fruits_count.most_common(1)[0]

    print(f"Most commom char is: '{most_commom_char}'")
    print(f"Most commom fruit is: '{most_commom_fruit}'")

    print(fruits_count.most_common())
