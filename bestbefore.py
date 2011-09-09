from sys import argv, exit
from itertools import permutations
from datetime import date

def illegal(error):
    #Error processing params
    print '%s is illegal' % error 
    exit()

class bestbefore(object):
    def __init__(self, A, B, C):
        self.MIN = 0
        self.MAX = 2999
        self.YEAR = 2000
    
        self.A, self.B, self.C = (int(A), int(B), int(C))
        # Check input range
        if not ((self.MIN <= self.A and self.A <= self.MAX) and \
                (self.MIN <= self.B and self.B <= self.MAX) and \
                (self.MIN <= self.C and self.C <= self.MAX)):
            self.A = None
            self.B = None
            self.C = None

    def compute(self):
        # Test all possible options
        correct = []
        all_failed = True
        for A, B, C in permutations([self.A, self.B, self.C]):
            try:
                d = date(A, B, C)
                # Check year in MIN..MAX range
                if d.year < self.YEAR:
                    year = d.year + self.YEAR
                    if year > self.MAX:
                        # year not in MIN..MAX range!
                        continue
                    d = date(year, d.month, d.day)
                correct.append(d.isoformat())
                all_failed = False
            except ValueError:
                continue
        if all_failed:
            illegal('/'.join([A, B, C]))
        # Get earliest legal date
        return min(correct)

if __name__ == "__main__":
    A, B, C = [None, None, None]
    # Read from a file
    try:
        A, B, C = open(argv[1]).read().strip().split('/')
    except IOError:
        # If not found, then parse it as string
        try:
            A, B, C = argv[1].strip().split('/')
        except:
            illegal(argv[1])

    try:
        b = bestbefore(A, B, C)
        print b.compute()
    except:
        illegal('/'.join([A, B, C]))

