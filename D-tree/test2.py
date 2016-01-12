from  math import log

# height weight sex age
# go shit

# big 1 , small 0
persons = [\
        [1,0,1,1],\
        [0,0,1,0],\
        [0,1,0,1],\
        [0,1,1,1],\
        [1,0,0,1]
]
# if good then go, else then shit
sagim = ["go", "shit", "shit","shit","go"]

# entrophy("go") + entrophy("shit")


def calc_shannon_ent(data):
    num_entry = len(data)
    print num_entry
    label_count = {}
    for row in data:                    
        label_count[row] = label_count.get(row,0) + 1   #if exists in label_count then row, else then 0
    
    ent_result = 0.0
    for label in label_count:
        prob = float(label_count[label])/num_entry
        print prob
        ent = -1 *prob * log(prob,2)
        ent_result += ent
    print  ent_result
    return ent_result
    
print (calc_shannon_ent(sagim)) # 0.9709... --> enough 1bit 


