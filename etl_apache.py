# Entry-point CLI

from database import createTable, createConnection,insertData
from summarizer import saveTjson,saveTocsv
from parser import readfile, extractLogs




def main():
    try:
        logsfile = './data/logs/apache_logs'
        data = readfile(logsfile)
        parsed_logs = extractLogs(data)
        cur,conn = createConnection()
        table = createTable(cur)
        insertData(conn,cur,parsed_logs)
        saveTocsv(parsedLogs=parsed_logs)
        saveTjson(parsedLogs=parsed_logs)
    except BaseException as error:
        print(error)



if __name__ == '__main__':
    main()