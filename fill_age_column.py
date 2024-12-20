from filehandling import CSV_read,CSV_write

col_index,dataset = CSV_read('train_dataset/1.csv')

rows_without_age = []
i = 0
len_of_dataset = len(dataset)
while i < len_of_dataset:
    if dataset[i][col_index["Age"]] == '':
        rows_without_age.append(dataset.pop(i))
        len_of_dataset-=1
    else:
        i+=1

print(len(rows_without_age))

def age_index(age=str()):
    age = float(age)
    if 0 <= age < 5:#baby
        return 0
    elif 5 <= age < 12:#child
        return 1
    elif 12 <= age < 20:#teenage
        return 2
    elif 20 <= age < 30:#young1
        return 3
    elif 30 <= age < 40:#young2
        return 4
    elif 40 <= age < 60:#mid-age
        return 5
    elif 60 <= age  : #old
        return 6
    
def closer_to_young1(x,y):
    if abs(x-3) < abs(y-3):
        return x
    else:
        return y
    
def farer_to_young1(x,y):
    if abs(x-3) > abs(y-3):
        return x
    else:
        return y

def guess(age_counter,survival_status):
    temp = 0
    temp_index = 0
    for i in range(len(age_counter)):
        if len(age_counter[i]) == temp:
            if survival_status == '1':
                temp_index = closer_to_young1(temp_index,i)
            else:
                temp_index = farer_to_young1(temp_index,i)
        if len(age_counter[i]) > temp:
            temp = len(age_counter[i])
            temp_index = i
    avg = sum(age_counter[temp_index])/1 if len(age_counter[temp_index])==0 else len(age_counter[temp_index])
    return str(avg)

    

for row in rows_without_age:
    age_counter = [[],[],[],[],[],[],[]]
    for record in dataset:
        similar = True
        i = 0
        while i < len(record):
            if i == col_index['Age']:
                i+=1
                continue
            if row[i] != record[i]:
                similar = False
                break
            i+=1
        if similar:
            age_counter[age_index(record[col_index['Age']])].append(float(record[col_index['Age']]))
    g = guess(age_counter,row[col_index['Survived']])
    row[col_index['Age']]=g

print(rows_without_age)
dataset.extend(rows_without_age)

CSV_write("train_dataset/2.csv",dataset,col_index)
        
      
