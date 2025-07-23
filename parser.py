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

def readfile(file) -> list:
 
    with open(file,'r') as file:
        return file.readlines()



def parse_apache_log_line(line):
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None


def extractLogs(data:list) -> list:
    
    parsed_logs = []
    for line in data:
        dt = parse_apache_log_line(line)
        parsed_logs.append(dt)
    return parsed_logs




