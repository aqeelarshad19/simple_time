import datetime, pytz
from time import gmtime, strftime

def get_nyc_time():
    utc = pytz.utc
    utc_dt = datetime.datetime.now(pytz.timezone('US/Eastern'))
    eastern = pytz.timezone('US/Eastern')
    loc_dt = utc_dt.astimezone(eastern)
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    loc_dt.strftime(fmt)
    return loc_dt

if __name__ == "__main__":
    local_time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print("Local Time: {}".format(local_time))
    print("Time in Newyork: {}".format(get_nyc_time()))

