'''import csv
with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['sn','name'])
    writer.writerow([1,'mpv'])
'''

with open(s + '.json', 'a+') as outfile:
    output = '{"date": "' + str(bar.date) + '","open":' + str(bar.open) + ',"high":' + str(
        bar.high) + ',"low":' + str(bar.low) + '' \
                                               ',"close":' + str(bar.close) + '},\n'
    outfile.write(output)