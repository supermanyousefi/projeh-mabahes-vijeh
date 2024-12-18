
# CSV_read is a function that receives a filename of csv file 
#file name must end with .csv, and its case sensetive
# it builds a list based dataset and returns a dictionary to handle that
#it must be used like this: col_index, dataset = CSV_read(filename)
# read comments below ...
def CSV_read(filename):
    if not filename.endswith(".csv"):
        raise Exception("only csv files allowed")
    with open(filename) as f:
        dataset = f.read()
    dataset = dataset.splitlines()
# to access value in dataset, use like this:
# dataset[row number][col_index["column name"]]
    for i in range(len(dataset)):
        s = dataset[i]
        s = s.split(',')
        dataset[i] = s
    
    first_row = dataset.pop(0)
    col_index = {col_name:first_row.index(col_name) for col_name in first_row}
    #print(dataset)
    return (col_index,dataset)


def CSV_write(newfilename,dataset,dictionary):
    if type(dataset) != type([]):
        return Exception("dataset crashed")
    file = open(newfilename,'x')


    for element in dictionary:
        file.write(str(element))
        if element != list(dictionary)[-1]:
            file.write(',')
    file.write('\n')
    
    for record in dataset:
        i = -1
        for value in record:
            i+=1
            file.write(str(value))
            if i != len(record)-1:
                file.write(',')
        file.write('\n')
    file.close()

