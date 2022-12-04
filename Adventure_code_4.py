# TASK1

result = 0

for line in open('input_4.txt'):
    line = line.strip()
    pair_1, pair_2 = line.split(',')
    
    val1_pair1,val2_pair1 = pair_1.split('-')
    val1_pair2,val2_pair2 = pair_2.split('-')
     
    pair1_vec = set(range(int(val1_pair1),int(val2_pair1)+1))
    pair2_vec = set(range(int(val1_pair2),int(val2_pair2)+1))
    
    if pair1_vec.issubset(pair2_vec) or pair1_vec.issuperset(pair2_vec):
        result += 1
    
print(result)

# TASK2

result = 0

for line in open('input_4.txt'):
    line = line.strip()
    pair_1, pair_2 = line.split(',')
    
    val1_pair1,val2_pair1 = pair_1.split('-')
    val1_pair2,val2_pair2 = pair_2.split('-')
     
    pair1_vec = set(range(int(val1_pair1),int(val2_pair1)+1))
    pair2_vec = set(range(int(val1_pair2),int(val2_pair2)+1))
    
    if len(pair1_vec & pair2_vec) != 0:
        result += 1
    
print(result)
