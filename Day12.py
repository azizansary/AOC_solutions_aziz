from itertools import product
input_raw = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

strs= []
instances = []
for input in input_raw.splitlines():
    strs.append(input.split(" ")[0])
    instances.append(input.split(" ")[1].split(','))

def replace_strings (str):
    results = []
    reps = ['#','.']
    index = [i for i, char in enumerate(str) if char =='?']
    for item in product(reps, repeat = len(index)):
        new_str = list(str)
        for ind, rep in zip(index, item):
            new_str[ind] = rep
        results.append(''.join(new_str))
    return results
def check_occurrence(str, occurences : list):
    results = []
    current_index = 0
    current_occurence = int(occurences[current_index])
    for index, char in enumerate(str):
        if char =='#':
            current_occurence = int(current_occurence)
            current_occurence -= 1
            if current_occurence ==0:
                current_index += 1
                if index+1<len(str):
                    if str[index+1] != '.':
                        return False
                if current_index < len(occurences):
                    current_occurence = occurences[current_index]
                elif index + 1 < len(str):
                    if '#' not in str[index+1:]:
                        return True
                else:
                    return True
            elif current_occurence > 0:
                if index+1<len(str):
                    if str[index+1] == '.':
                        return False
            elif current_occurence <0:
                return False
        elif char =='.':
            continue
    return False

count = 0
for index, string in enumerate(strs):
    list_strings = replace_strings(string)
    for str in list_strings:

        if check_occurrence(str, instances[index]):
            print(str, instances[index])
            count += 1

print(count)
count = 0
#Part 2 yet to be added
# for index, string in enumerate(strs):
#     list_strings = replace_strings('?'.join([string]*5))
#     for str in list_strings:
#
#         if check_occurrence(str, instances[index]*5):
#             print(str, instances[index])
#             count += 1
#
# print(count)



