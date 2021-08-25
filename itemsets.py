# The ideas of finding closed and maximal frequent itemsets are from the website: https://blog.csdn.net/u013007900/article/details/54743395.
from efficient_apriori import apriori
import time

# This is a helper function.
def is_overlap(List1, List2):
    answer = True
    for i in List1:
        if i not in List2:
            answer = False
    return answer

# This part is for Part A: Closed Itemsets.
def closed_itemsets(itemsets):
    all_itemsets = []
    close = []
    length = len(itemsets)
    indexes = list(range(length))

    for i in indexes:
        all_itemsets.extend(itemsets[i+1].keys())

    for item in all_itemsets:
        for temp in all_itemsets:
            item_length = len(item)
            temp_length = len(temp)
            condition = (is_overlap(item,temp)) and (temp != item) and (itemsets[item_length][item] != itemsets[temp_length][temp])
            if (condition):
                close.append(item)
    close = list(set(close))
    answer = {}

    for item in close:
        l = len(item)
        if l not in answer.keys():
            answer[l] = {}
        iteration = itemsets[l][item]
        add = {item:iteration}
        answer[l].update(add)

    return answer

# This part is for Part B: Maximal Itemsets.
def maximal_itemsets(itemsets):
    all_itemsets = []
    maximal = []
    length = len(itemsets)
    indexes = list(range(length))

    for i in indexes:
        all_itemsets.extend(itemsets[i+1].keys())

    for item in all_itemsets:
        count = 0
        for temp in all_itemsets:
            condition = (is_overlap(item,temp))
            if (condition):
                count = count + 1
        if (count < 2):
            maximal.append(item)

    answer = {}

    for item in maximal:
        l = len(item)
        if l not in answer.keys():
            answer[l] = {}
        iteration = itemsets[l][item]
        add = {item:iteration}
        answer[l].update(add)

    return answer
       

def main():
    # This part is for preprocessing.
    print('......Reading Data......\n')
    f = open('BMS2.txt','r')
    print('......Reading Completed......\n')
    print('......Preprocessing......\n')
    answer = []
    for line in f.readlines():
      answer.append([s for s in line.strip().split() if s != '-1' and s != '-2'])
    f.close()
    print('......Preprocessing Completed......\n')
    print('......Apriori Generating......\n')
    start = time.perf_counter()
    itemsets, rules = apriori(answer, min_support = 0.005, min_confidence = 0.7)
    elapsed = (time.perf_counter() - start)
    print ('Time used in seconds: %f.\n' % elapsed)
    print('......Apriori Generated......\n')
    print('......Analyzing......\n')

    # This part is for C.1: All frequent itemsets. 
    print('******Answer of Part C.1******\n')
    start = time.perf_counter()
    all_itemsets_counter = 0
    for record in itemsets.keys():
        all_itemsets_counter = all_itemsets_counter + len(itemsets[record])
    print('The number of ALL frequent itemsets is %d.' % all_itemsets_counter)
    for record in itemsets.keys():
        print('The number of ' + str(record) + '-itemsets is %d.' % len(itemsets[record]))
    elapsed = (time.perf_counter() - start)
    print ('Time used in seconds: %f.\n' % elapsed)

    # This part is for C.2: CLOSED frequent itemsets.
    print('******Answer of Part C.2******\n')
    start = time.perf_counter()
    closed_itemsets_counter = 0
    closed = closed_itemsets(itemsets)
    for record in closed.keys():
        closed_itemsets_counter = closed_itemsets_counter + len(closed[record])
    print("The number of CLOSED frequent itemsets is %d." % closed_itemsets_counter)
    for record in closed.keys():
        print('The number of '+ str(record)+ '-itemsets is %d.' % len(closed[record]))
    elapsed = (time.perf_counter() - start)
    print ('Time used in seconds: %f.\n' % elapsed)

    # This part is for C.3: MAXIMAL frequent itemsets.
    print('******Answer of Part C.3******\n')
    start = time.perf_counter()
    max_itemsets_counter = 0
    maximal = maximal_itemsets(itemsets)
    for record in maximal.keys():
        max_itemsets_counter = max_itemsets_counter + len(maximal[record])
    print("The number of MAXIMAL frequent itemsets is %d." % max_itemsets_counter)
    for record in maximal.keys():
        print('The number of '+ str(record)+ '-itemsets is %d.' % len(maximal[record]))
    elapsed = (time.perf_counter() - start)
    print ('Time used in seconds: %f.\n' % elapsed)

    # This part is for D: Insight.
    print('******Answer of Part D******\n')
    if (max_itemsets_counter > closed_itemsets_counter):
        print('The number of MAXIMAL frequent itemsets is LARGER THAN the number of CLOSED frequent itemsets.')
    elif (max_itemsets_counter == closed_itemsets_counter):
        print('The number of MAXIMAL frequent itemsets is EQUAL TO the number of CLOSED frequent itemsets.')
    else:
        print('The number of MAXIMAL frequent itemsets is SMALLER THAN the number of CLOSED frequent itemsets.')
    print('Further discussions are in the report.')
    print('Thank you!\n')

if __name__ == '__main__':
    print('......This Is The Beginning of Assignment 3......\n')
    main()
    print('......This Is The End of Assignment 3......\n')
