import requests
import csv

def make_csv():
    param_dict = {'key':'2ECEF0FA-03C3-33EA-8410-658A77DA3BA6','commodity_desc':'TURKEYS','year__GE':'1989','state_alpha':'VA','short_desc':'TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD','format':'csv'}
    r = requests.get("https://quickstats.nass.usda.gov/api/api_GET/?",params = param_dict)

    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        reader = csv.reader(r.text.splitlines())
        for row in reader:
            writer.writerow(row)

if __name__ == '__main__':
    make_csv()
