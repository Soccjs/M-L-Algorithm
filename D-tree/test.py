from math import log

print "hello soccjs"
print "calc shannon entropy"

def calc_shannon_ent(label):
    num_entry = len(label)
    # print num_entry

    label_count = {}
    for item in label:
        if item not in label_count.keys():
            label_count[item]=0
        label_count[item] += 1;

    # print label_count

    shannon_ent = 0.0
    for key in label_count:
        prob = float(label_count[key])/num_entry
        shannon_ent -= prob * log(prob,2)   # P*logP

    return shannon_ent

def major_label_count(label_data):
    label_count = {}
    max_label=''
    max_count=0
    for label in label_data:
        label_count[label] = label_count.get(label,0)+1 
        if max_count < label_count[label]:
            max_label=label
            max_count=label_count[label]
#     return sorted_label_count[0][0]
    return max_label

def split_data(mat_data, label_data, col, uniq):
    ret_mat =[]
    ret_label = []
    for index, row in enumerate(mat_data):
        if row[col] == uniq:
            temp = row[:col]
            temp.extend(row[col+1:])
            ret_mat.append(temp)
            ret_label.append(label_data[index])
    return ret_mat, ret_label
            

def create_tree(mat_data, label_data):
    if label_data.count(label_data[0]) == len(label_data): 
        return label_data[0]
    if len(mat_data[0]) == 0 or (len(mat_data[0])==1 and len(set([row[0] for row in mat_data]))==1):
        return major_label_count(label_data)
    

    num_cols=len(mat_data[0])
    lowest_ent = 9999
    best_col = -1
    
    for i in range(num_cols):
        col = [row[i] for row in mat_data]
        uniq_col = set(col)
        branch_ent=0.0
        for uniq in uniq_col:
            split_mat, split_label = split_data(mat_data, label_data, i, uniq)
            probability = len(split_label)/float(len(label_data))
            branch_ent += probability*calc_shannon_ent(split_label)
        if lowest_ent > branch_ent:
            lowest_ent = branch_ent
            best_col = i

    tree = { best_col : {
            # 0:sub_tree, 1:sub_tree, 2:sub_tree
        }}
    
    best_col_val = [row[best_col] for row in mat_data]
    uniq_val = set(best_col_val) 
    
    for val in uniq_val:
        split_mat, split_label = split_data(mat_data, label_data, best_col, val)
        tree[best_col][val]=create_tree(split_mat, split_label)
    print tree    
    return tree

    
    
# label : shine, rain, cloud
# mat : (wind, sun, fog, temp, wet) -> 0,1,2
mat_data = [\
            [1,2,0,2,0],\
            [2,0,2,1,2],\
            [2,2,1,2,0],\
            [2,1,2,0,2],\
            [1,0,0,1,1],\
            [2,0,1,1,1]\
           ]

label1 = ["shine", "rain", "shine", "rain","cloud","cloud"] 

print "start"
create_tree(mat_data,label1)