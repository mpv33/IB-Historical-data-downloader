import pandas as pd


'''
with open('ACC_2017-19_Historicaldata.csv') as f:
    data = list(csv.reader((f)))
    new_data = [a for i, a in enumerate(data) if a not in data[:i]]
    with open('ACC_updated_2017-19_Historicaldata.csv', 'w') as t:
        write = csv.writer(t)
        print('hi')
        write.writerows(new_data)
'''
df = pd.read_csv('file.csv')
df.drop_duplicates(inplace=True)
df.to_csv('updated_file.csv', index=False)

