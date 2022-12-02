# TASK1

result = 0
dic_opp = {'A':'Rock','B':'Paper','C':'Scissors'}
dic_mine = {'X':'Rock','Y':'Paper','Z':'Scissors'}

for line in open("input_2.txt"):
    line = line.strip('\n')
   
    oppo,mine = line.split(' ')
    
    if dic_opp[oppo] == dic_mine[mine]:
        value_1 = 3
    if dic_opp[oppo] == 'Rock' and dic_mine[mine] == 'Paper' :
        value_1 = 6
    if dic_opp[oppo] == 'Rock' and dic_mine[mine] == 'Scissors' :
        value_1 = 0
    if dic_opp[oppo] == 'Paper' and dic_mine[mine] == 'Rock' :
        value_1 = 0
    if dic_opp[oppo] == 'Paper' and dic_mine[mine] == 'Scissors' :
        value_1 = 6
    if dic_opp[oppo] == 'Scissors' and dic_mine[mine] == 'Rock' :
        value_1 = 6
    if dic_opp[oppo] == 'Scissors' and dic_mine[mine] == 'Paper' :
        value_1 = 0
    
    if dic_mine[mine] == 'Paper' :
        value_2 = 2
    if dic_mine[mine] == 'Rock' :
        value_2 = 1
    if dic_mine[mine] == 'Scissors' :
        value_2 = 3
        
    value_sum = value_1 + value_2
    result = result + value_sum
print(result)

# TASK2

result = 0
dic_opp = {'A':'Rock','B':'Paper','C':'Scissors'}
dic_res = {'X':0,'Y':3,'Z':6}
value_mine = {'Rock':1,'Paper':2,'Scissors':3}

for line in open("input_2.txt"):
    line = line.strip('\n')
   
    oppo,res = line.split(' ')
    
    if res == 'X':
        if dic_opp[oppo] == 'Rock':
            mine = 'Scissors'
        if dic_opp[oppo] == 'Paper':
            mine = 'Rock'
        if dic_opp[oppo] == 'Scissors':
            mine = 'Paper'
    
    if res == 'Z':
        if dic_opp[oppo] == 'Rock':
            mine = 'Paper'
        if dic_opp[oppo] == 'Paper':
            mine = 'Scissors'
        if dic_opp[oppo] == 'Scissors':
            mine = 'Rock'
            
    if res == 'Y':
        mine = dic_opp[oppo]
            
    value_1 = dic_res[res]
    value_2 = value_mine[mine]
    value_sum = value_1 + value_2
    result = result + value_sum
print(result)
