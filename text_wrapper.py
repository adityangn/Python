str = input()
n = int(input())

chunks = []

i = 0
while i < len(str):
    if i+n < len(str):
        chunks.append(str[i:i+n])
    else:
        chunks.append(str[i:len(str)])
    i += n
print('\n'.join(chunks))