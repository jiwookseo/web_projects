import csv

def load_csv(csvfile):
    with open(csvfile, 'r', newline='',encoding="utf-8") as f:
        result=list(csv.reader(f))
    result.pop(0)
    return result       

def save_csv(csvfile,result):
    with open(csvfile, 'a', newline='',encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',')
        for temp in result:
            writer.writerow(temp)