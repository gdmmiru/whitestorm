from pandas.io.data import Options


import datetime
import sys

def print_header():
    print "======================================================================"
    print "======================================================================"
    print

symbol = 'AXP'

# create an Options object which we can use to retrieve data(empty datasource)
options = Options(symbol, "yahoo")

# tell the object to gather all options data for today
options.get_all_data()


# save the front month puts
front_month_puts = options.get_put_data()

# get all expirys
expiries = options.expiry_dates

# save the second month puts
back_month_puts = options.get_put_data(expiry=expiries[1])

# print sample of front month option puts
print "================ front month puts (head)===================="
print front_month_puts.head()

print_header()

print "================ back month puts (head)===================="
print back_month_puts.head()


# convenience variables
fm = front_month_puts

print_header()

# filter out options by their Vol (Vol is a value in the row)
min_vol = 10
min_oi = 50

active_fm_puts = fm[fm.Vol > min_vol]
print "FM PUTS WITH A MINIMUM OF AT LEAST VOLUME 10"
print "count:", len(active_fm_puts)
print active_fm_puts.head()


print_header()
active_fm_puts_with_oi = fm[(fm.Vol > min_vol) & (fm.Open_Int > min_oi)]
print "FM PUTS WITH A MINIMUM OF AT LEAST VOLUME 10 AND OI > 50"
print "count:", len(active_fm_puts_with_oi)
print active_fm_puts_with_oi.head()


print_header()
active_fm_puts_or_oi = = fm[(fm.Vol > min_vol) | (fm.Open_Int > min_oi)]
print "FM PUTS WITH A MINIMUM OF AT LEAST VOLUME 10 OR OI > 50"
print "count:", len(active_fm_puts_or_oi)
print active_fm_puts_or_oi.head()


print_header()
# the index is a multilevel field, which we can access through levels
# Strike is the first index of the levels
itm_fm_puts = fm[fm.index.levels[0] > options.underlying_price]
print "itm front month puts"





