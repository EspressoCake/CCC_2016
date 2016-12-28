import os
import re
import sys

def main():
    if len(sys.argv) != 2:
        print "Usage: python", sys.argv[0], '"FILE_STORAGE_DIRECTORY"'
        sys.exit()
    else:
        regex = re.compile("^33c3.\d+.eng.")
        for item in os.listdir(sys.argv[1]):
            if re.match(regex, item):
                new_Name = re.sub(regex, "33C3_", item)
                os.rename((os.path.join(sys.argv[1], item)), (os.path.join(sys.argv[1], new_Name)))            

main()
