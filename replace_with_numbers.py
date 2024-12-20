from filehandling import CSV_read,CSV_write
col_index,dataset = CSV_read('train_dataset/2.csv')
for r in dataset:
    if r[col_index['Sex']] == 'male':
        r[col_index['Sex']] = '0'
    else:
        r[col_index['Sex']] = '1'

    if r[col_index['Embarked']] == 'C':
        r[col_index['Embarked']] = '0'
    elif r[col_index['Embarked']] == 'Q':
        r[col_index['Embarked']] = '1'
    elif r[col_index['Embarked']] == 'S':
        r[col_index['Embarked']] = '2'


CSV_write('train_dataset/3.csv',dataset,col_index)
    
    

    
    
