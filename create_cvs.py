import sys
import os.path

# Usage : python create_cvs.py "path"

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Usage : python create_cvs.py <path>"
        sys.exit(1)

    PATH=sys.argv[1]
    SEP=";"

    label = 0
    for dirname, dirnames, filenames in os.walk(PATH):
        for subdirname in dirnames:
            subjectPath = os.path.join(dirname, subdirname)
            for filename in os.listdir(subjectPath):
                absPath = "%s/%s" % (subjectPath, filename)
                print "%s%s%d" % (absPath, SEP, label)
            label = label + 1
