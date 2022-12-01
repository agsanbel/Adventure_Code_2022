# ADVENTURE CODE 1
f = open("input_1.txt", "r")
print(f.read())

dictionary = {}
suma = 0
n = 1

for line in open("input_1.txt"):
    
    if line.strip() == '':
        dictionary[n] = suma
        n = n+1
        suma = 0
        print('Number:',n)
        
    else:
        suma = suma + int(line)

# Max value
max(dictionary.values())

# Key of max value
max(dictionary, key=dictionary.get)

sort_dict_values = sorted(dictionary.values(), reverse=True)

# Sum of 3 top highest values
sum(sort_dict_values[0:3])
