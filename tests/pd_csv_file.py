import pandas as pd
import datetime
import os.path
from pandas.io.data import Options

today = datetime.datetime.now().date().isoformat().replace('-', '')


symbol = 'SPY'
filename = 'options.'+symbol+"."+today+".csv"

print "checking for csv file:"+ filename

all_options = None

if os.path.isfile(filename) == False:
    print "file does not exit, get remotely from yahoo, and write to file"
    options = Options(symbol, 'yahoo')
    all_options = options.get_all_data()
    all_options.to_csv(filename)
    all_options.reset_index(inplace=True)
else:
    print "file exists, read from data"
    # read from csv Strike,Expiry,Type,Symbol are treated as index
    all_options = pd.DataFrame.from_csv(filename, index_col=False)


# all_options will be the same value whether file exists
print all_options
