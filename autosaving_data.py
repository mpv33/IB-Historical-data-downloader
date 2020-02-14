import csv
#method-1
with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['sn','name'])   # list form each row 
    writer.writerow([1,'mpv'])
# method-2
with open(s + '.json', 'a+') as outfile:
    output = '{"date": "' + str(bar.date) + '","open":' + str(bar.open) + ',"high":' + str(
        bar.high) + ',"low":' + str(bar.low) + '' \
                                               ',"close":' + str(bar.close) + '},\n'
    outfile.write(output)
