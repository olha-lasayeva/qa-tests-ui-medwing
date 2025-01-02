import requests
import datetime
import os
from tests_ui.conftest import current_date_time


# Documentation: https://developers.google.com/speed/docs/insights/v5/get-started
# JSON paths: https://developers.google.com/speed/docs/insights/v4/reference/pagespeedapi/runpagespeed
# Populate 'pagespeed.txt' file with URLs to query against API.



def test_getpagespeedscore(targeturl, ntimes, device, apikey, outputfile, daterun):
    writeheaders = not (os.path.isfile(outputfile))
    # write headers if file does not exist, otherwise append
    if writeheaders:
        file = open(outputfile, 'w')
        columnTitleRow = "Date run, Device, Target URL, Final URL, Performance Score, First Contentful Paint (s), First Interactive (s)\n"
        file.write(columnTitleRow)
    else:
        file = open(outputfile, 'a')
    # This is the google pagespeed api url structure, using for loop to insert each url in .txt file
    for n in range(ntimes):
        # If no "strategy" parameter is included, the query by default returns desktop data.
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={targeturl}&strategy={device}&key={apikey}'
        # print(f'Requesting {x}...')
        print(f'Requesting {targeturl}: {n + 1}')
        r = requests.get(x)
        final = r.json()
        try:
            urlid = final['id']
            split = urlid.split('?')  # This splits the absolute url from the api key parameter
            urlid = split[0]  # This reassigns urlid to the absolute url
            ID = str(urlid)
            urlfcp = final['lighthouseResult']['audits']['first-contentful-paint']['displayValue']
            FCP = str(urlfcp).strip("  s")
            urlfi = final['lighthouseResult']['audits']['interactive']['displayValue']
            FI = str(urlfi).strip("  s")
            urlscore = final['lighthouseResult']['categories']['performance']['score']
            Score = str(urlscore * 100)
        except KeyError:
            print("Error")
            #print(f'<KeyError> One or more keys not found {line}.')
        try:
            row = f'"{daterun}","{device}","{targeturl}","{ID}",{Score},{FCP},{FI}\n'
            file.write(row)
        except NameError:
            print("Error")
            #print(f'<NameError> Failing because of KeyError {line}.')
            #file.write(f'<KeyError> & <NameError> Failing because of nonexistant Key ~ {line}.' + '\n')
    file.close()
    print(f'Finished')


############################################
targeturls = [

    # Homepage
    'https://medwing.com/DE/de/',
]

ntimes = 5
# TODO: Update 'desktop'/'mobile'
device = 'mobile'
apikey = 'AIzaSyDUiGQpOw4_ehvcu0xOR-9sRjAKd-9gajA'
# TODO: Update the file name for every new test
outputfile = 'resultsProd_' + current_date_time + '.csv'

daterun = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
for targeturl in targeturls:
    test_getpagespeedscore(targeturl, ntimes, device, apikey, outputfile, daterun)
