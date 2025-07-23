# Log Parsing Logic
import re




log_pattern = re.compile(
    r'(?P<ip>\S+) '                  # IP address
    r'\S+ \S+ '                      # Identd and user (ignored)
    r'\[(?P<timestamp>.+?)\] '       # Timestamp
    r'"(?P<method>\S+) '             # HTTP Method
    r'(?P<url>\S+) '                 # URL
    r'(?P<protocol>[^"]+)" '         # Protocol
    r'(?P<status>\d{3}) '            # HTTP Status code
    r'(?P<size>\S+)'                 # Response size
)

def readfile(file):
    myfile = None
    with open(file,'r') as file:
        myfile = file.readlines()

    return myfile


def extractLogs(data:list):
    for line in data:
        dt = parse_apache_log_line(line)
        print(dt,'\n')

def parse_apache_log_line(line):
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None



        
logsfile = './data/logs/apache_logs'
data = readfile(logsfile)
extractLogs(data)