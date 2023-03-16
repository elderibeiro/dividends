import pandas as pd
import io
import requests
import urllib3
import json
import datetime

#suppress ssl certificate check
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#bybass algotrading restrictions
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

#define the list of stocks to loop through
#stocks = ["AAPL", "MSFT", "XOM", "NVDA", "PBR", "META", "CCJ", "BDORY", "RSX", "QQQ"]
response = requests.get("https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=demo", headers=headers, verify=False)

#convert response from csv to pandas datagrame
stocks_df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))

#get the dataframe column 'symbol', convert every item to a string and format as a list
stocks = stocks_df['symbol'].astype(str).to_list()

#split the list in batches to avoid too many API calls
stocks_batch = []
for x in range(0,len(stocks),1000):
    stocks_batch.append(stocks[x:x+1000])

#define an empty list to hold the dataframes
dfs = []

#loop through the batch
#batch = [["AAPL", "MSFT", "XOM"], ["NVDA", "PBR", "META"], ["CCJ", "BDORY", "RSX"]]
for batch in stocks_batch:
    query_params = {"symbols": ",".join(batch)}

    #get quote for the batch
    response = requests.get("https://query1.finance.yahoo.com/v7/finance/quote", params=query_params, headers=headers, verify=False)
    json_response = json.loads(response.text)

    #create a dataframe for each stock of the batch and append to a list of dataframes
    for i in range(len(json_response["quoteResponse"]["result"])):
        symbol = json_response["quoteResponse"]["result"][i]["symbol"]
        if "shortName" in json_response["quoteResponse"]["result"][i]:
            shortName = json_response["quoteResponse"]["result"][i]["shortName"]
        else:
            shortName = None
        if "fullExchangeName" in json_response["quoteResponse"]["result"][i]:
            fullExchangeName = json_response["quoteResponse"]["result"][i]["fullExchangeName"]
        else:
            fullExchangeName = None
        if "dividendDate" in json_response["quoteResponse"]["result"][i]:
            dividendDate = datetime.datetime.fromtimestamp(json_response["quoteResponse"]["result"][i]["dividendDate"])
        else:
            dividendDate = None
        if "trailingAnnualDividendRate" in json_response["quoteResponse"]["result"][i]:
            trailingAnnualDividendRate = json_response["quoteResponse"]["result"][i]["trailingAnnualDividendRate"]
        else:
            trailingAnnualDividendRate = None
        if "trailingAnnualDividendYield" in json_response["quoteResponse"]["result"][i]:
            trailingAnnualDividendYield = json_response["quoteResponse"]["result"][i]["trailingAnnualDividendYield"]
        else:
            trailingAnnualDividendYield = None
        if "averageAnalystRating" in json_response["quoteResponse"]["result"][i]:
            averageAnalystRating = json_response["quoteResponse"]["result"][i]["averageAnalystRating"]
        else:
            averageAnalystRating = None
        data = {
            "shortName": [shortName],
            "symbol": [symbol],
            "fullExchangeName": [fullExchangeName],
            "dividendDate": [dividendDate],
            "trailingAnnualDividendRate": [trailingAnnualDividendRate],
            "trailingAnnualDividendYield": [trailingAnnualDividendYield],
            "averageAnalystRating": [averageAnalystRating]
        }
        df = pd.DataFrame(data)
        dfs.append(df)

#concatenate all the dataframes in the list into a single dataframe
concat_df = pd.concat(dfs, ignore_index=True)

# Convert the 'date' column to a datetime format
concat_df['dividendDate'] = pd.to_datetime(concat_df['dividendDate'], errors='coerce')

# Filter out records that are older than 2022 or have an empty date
final_df = concat_df[(concat_df['dividendDate'].notnull()) & (concat_df['dividendDate'].dt.year >= 2022)]

#print the resulting dataframe info
print(final_df.info())

#print top 50 items of the dataframe sorted by trailingAnnualDividendYield
print(final_df.sort_values(by=['trailingAnnualDividendYield'], ascending=False).head(50))

#print top 50 items of the dataframe sorted by trailingAnnualDividendYield
with open('dividends.md', 'w') as f:
    f.write(final_df.sort_values(by=['trailingAnnualDividendYield'], ascending=False).head(50).to_markdown(index=False))

#save the dataframe to a csv file
final_df.to_csv('dividends.csv', index=False)