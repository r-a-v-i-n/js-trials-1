"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    pass  # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    pass  # TODO: replace this line with your code
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    pass  # TODO: replace this line with your code
    result = []

    for num in range(len(items)):
        if num % 2 != 0: 
        # it's if num % 2 == 0:
            return result.append(num)
            # result.append(items[num])
    # return result


def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code
    i = 1

    for item in items:
        print(f'{i}.{item}')

        i+=1



def get_range(start, stop):
    pass  # TODO: replace this line with your code
    nums = []

    for num = 0 AND num < stop:
    # for num in range(start, stop):
        num += 1
        # didn't need this? not in solution
        nums.append(num)

    # return nums


def censor_vowels(word):
    pass  # TODO: replace this line with your code

    chars = []

    for letter in word:
        if letter = 'aeiou':
        # if letter in 'aeiou':
            chars.append(letter)
            #chars.append('*')
    
    return chars.join('')
    # return ''.join(chars)


def snake_to_camel(string):
    pass  # TODO: replace this line with your code
    camel_case = []

    for word in string.split('_'):
        camel_case.append(word[0].upper, word[1:])
        # camel_case.append(f'{word[0].upper()}{word[1:]})
    
    return camel_case.join('')
    # return ''.join(camel_case)



def longest_word_length(words):
    pass  # TODO: replace this line with your code
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest


def truncate(string):
    pass  # TODO: replace this line with your code
    result = []

    for char in string:
        if 


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
