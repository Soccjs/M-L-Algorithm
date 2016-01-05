from math import log

print "hello soccjs"
print "calc shannon entropy"

def calc_shannon_ent(label):
    num_entry = len(label)
    print num_entry

    label_count = {}
    for item in label:
        if item not in label_count.keys():
            label_count[item]=0
        label_count[item] += 1;

    print label_count

    shannon_ent = 0.0
    for key in label_count:
        prob = float(label_count[key])/num_entry
        shannon_ent -= prob * log(prob,2)   # P*logP

    return shannon_ent


label1 = ["shine", "rain", "shine", "rain","cloud","cloud"] 
label2 = ["shine", "shine","rain","rain","rain","shine"]    #label2's entropy less than label1's thing
            
c1 = calc_shannon_ent(label1)       #1.5~~
c2 = calc_shannon_ent(label2)       #1.0

print(c1)
print(c2)

assert c1>c2   #assert : if true then pass,false then  error



