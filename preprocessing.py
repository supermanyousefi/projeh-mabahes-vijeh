from filehandling import CSV_read,CSV_write
col_index,dataset = CSV_read('train_dataset/3.csv')

for row in dataset:
    for i in range(len(row)):
        try: 
            row[i]=int(row[i])
        except:
            row[i]=float(row[i])


#copy code from Machine_Learning_Code/S03/code-3/Preprocessing_Scale.ipynb

from sklearn.preprocessing import normalize

normal_dataset = normalize(dataset,'l1',axis=0)

normal_dataset = list(normal_dataset)
#saving
        

CSV_write('train_dataset/4.csv',normal_dataset,col_index)