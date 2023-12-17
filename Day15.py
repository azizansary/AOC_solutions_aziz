input_r = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

inputs = input_r.split(",")

#Part 1
sum = 0
for str in inputs:
    count = 0
    for char in str:
        count += ord(char)
        count = count*17
        count = count%256
    print(count)
    sum += count
print(sum)