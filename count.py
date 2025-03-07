def count_vowels(s):
    vowels = "aeiouAEIOU"  
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


input_string = input()


vowel_count = count_vowels(input_string)


if vowel_count > 0:
    print(f"Total number of vowels: {vowel_count}")
else:
    print("No vowels were found.")
