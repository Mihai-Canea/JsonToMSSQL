import sys
import getopt
import getpass
import json


def PrintOutput(sqlQuery, QueryName):
    sqlFile = open("{}.sql".format(QueryName), "w")
    sqlFile.write(sqlQuery)
    sqlFile.close()


def SQLtable(TableName, JsonFile):
    queryContent = ""
    print("Table name:", TableName, "| JSON file:", JsonFile)
    with open('{}'.format(JsonFile)) as data_file:
        data = json.load(data_file)
    # print("Data:\n",json.dumps(data, indent=4))

    print("ROWS: ", len(data))
    print("COLUMNS: ", len(data[0]))

    for elements in data:
        sqlQuery = "INSERT INTO [dbo].[{}](\n".format(TableName)
        for num, items in enumerate(elements, start=1):
            if num == len(data[0]):
                sqlQuery += "\t{}".format(items)
            else:
                sqlQuery += "\t{},\n".format(items)
        break

    for rows, elements in enumerate(data, start=1):
        queryContent += "("
        for num, items in enumerate(elements, start=1):
            # Check if exist single quotation mark
            if elements[items].find("'") != -1:
                elements[items] = elements[items].replace("'", "''")
            if num == len(data[0]):
                queryContent += "'{}'".format(elements[items])
            else:
                queryContent += "'{}',".format(elements[items])
        queryContent += ");" if rows == len(data) else "),\n"

    sqlQuery += "\n)\nVALUES\n{}".format(queryContent)
    PrintOutput(sqlQuery, TableName)
    print("---\nFile created")

def ShowMenu():
    print("\nUsage\n")
    print("[-t] [<DB table name>]: insert JSON file name from scrapy output")
    print("[-o] [Name output file]: Export data")
    print("...")

#
# ──────────────────────────────────────────────── I ──────────
#   :::::: M A I N : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────
#

def SetTitle():
    return """
     _ ___  ___  _  _   _         __  __ ___ ___  ___  _    
  _ | / __|/ _ \| \| | | |_ ___  |  \/  / __/ __|/ _ \| |   
 | || \__ \ (_) | .` | |  _/ _ \ | |\/| \__ \__ \ (_) | |__ 
  \__/|___/\___/|_|\_|  \__\___/ |_|  |_|___/___/\__\_\____|       
    """

def main(argv):
    print(SetTitle())
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "t:o:", ["iTable=", "ofile="])
        # print("OPTS: ", opts, "ARGS ", args)
    except getopt.GetoptError:
        # print('main.py -t <DB table name> -o <Output.txt>')
        #print('main.py -t <DB table name>')
        ShowMenu()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-help':
            #print('main.py -t <DB table name>')
            ShowMenu()
            sys.exit()
        elif opt in ("-t", "--iTable"):
            # print("OPT ", opt, "ARG ", arg)
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            # print("OPT ", opt, "ARG ", arg)
            outputfile = arg

    SQLtable(inputfile.split('.')[0], inputfile)
    # print('Input file is "', inputfile)
    # print('Output file is "', outputfile)


if __name__ == "__main__":
    print(sys.argv[1:])
    main(sys.argv[1:])
