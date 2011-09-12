from sys import argv
from datetime import date
from itertools import permutations

def illegal(error):
    #Error processing params
    print '%s is illegal' % error 
    exit()

class bestbefore(object):
    def __init__(self, A, B, C):
        self.MIN = 0
        self.MAX = 2999
        self.MIN_YEAR = 2000
    
        self.A, self.B, self.C = (A, B, C)

    def compute(self):
        # Test all possible options
        all_dates = []
        if not self.A and not self.B and not self.C:
            return []
        for A, B, C in permutations([self.A, self.B, self.C]):
            try:
                d = date(A, B, C)
                # Check year in MIN_YEAR..MAX range
                if d.year < self.MIN_YEAR:
                    year = d.year + self.MIN_YEAR
                    if year > self.MAX:
                        # year not in range!
                        continue
                    d = date(year, d.month, d.day)
                all_dates.append(d.isoformat())
            except ValueError:
                continue
        return all_dates

if __name__ == "__main__":
    data = raw_input()
    try:
        A, B, C = map(int, data.split('/'))
    except:
        illegal(data)

    b = bestbefore(A, B, C)
    all_dates = b.compute()
    try:
        # Get earliest legal date
        print min(all_dates)
    except ValueError:
        illegal(data)
