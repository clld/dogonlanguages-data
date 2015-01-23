# Given a directory with Dogon flora and fauna images extract metadata from filenames

import csv
import sys
from path import path

def process(path):
    md5 = path.read_md5()
    result = [md5]
    result.append(str(path.basename()))
    tokens = path.namebase.split("_")
    result.append(len(tokens))
    for i in tokens:
        result.append(i)
    return(result)

def main(dir):
    output = open("output.csv", "w")
    for f in path(dir).files():
        if not f.basename().startswith('.'):
            result = process(f)
            wr = csv.writer(output, quoting=csv.QUOTE_ALL)
            wr.writerow(result)
    output.close()

if __name__=="__main__":
    dir = sys.argv[1]
    main(dir)


