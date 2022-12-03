# TASK 1

dict_ruck = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,
        'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
       'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,
        'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}

def compare(a, b):
    value = ''
    for x in a:
        if len(value) == 1:
            break
        for y in b:
            if len(value) == 1:
                break
            if x == y:
                value+=str(x)
      
    return value
  
  result = 0

  
for line in open("input_3.txt"):
    
    line = line.strip()
    num = int(len(line)/2)
    
    first_comp = line[0:num]
    second_comp = line[num:]
    
    char = compare(first_comp,second_comp)
    result += dict_ruck[char]

print(result)

# TASK 2

def compare(a,b,c):
    list_a = []
    for x in a:
        list_a.append(x)
    list_b = []
    for y in b:
        list_b.append(y)
    list_c = []
    for z in c:
        list_c.append(z)
    value = list(set(list_a) & set(list_b) & set(list_c))
    return value[0]

  
result = 0
n =0

for line in open("input_3.txt"):
  
    line = line.strip()
    if n % 3 == 0:
        first_comp = line
    if n % 3 == 1:
        sec_comp = line
    if n % 3 == 2:
        thi_comp = line 
        char = compare(first_comp,sec_comp,thi_comp)
        result += dict_ruck[char]
        
    n += 1

print(result)
