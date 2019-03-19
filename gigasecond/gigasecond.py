from datetime import datetime
def add_gigasecond(moment):
    gig = moment.timestamp()
    gig = gig + 10**9
    return datetime.fromtimestamp(gig)
