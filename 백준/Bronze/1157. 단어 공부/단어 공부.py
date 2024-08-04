S = input().upper()

char_dict = {}

for char in S:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

max_cnt = max(char_dict.values())
max_char = [char for char, cnt in char_dict.items() if max_cnt == cnt]

if len(max_char) > 1:
    print('?')
else:
    print(max_char[0])
