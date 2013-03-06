#!/usr/bin/envy python2.7
import random

POINTS_FILE = "sample.txt" # <Point, Name> pairs. See sample.txt for format
POINTS_FILE_PROCESSED = "sample.out.txt" # Results will be stored in this file
POINTS_DESC = True # Sort order

def points():
    """ sort a list of point name pairs """
    def compare_with_ties(a, b):
        diff = cmp(a, b)
        return diff if diff else random.choice([-1,1])
    with open(POINTS_FILE) as fh:
        lines = fh.readlines()
        out = []
        for line in lines:
            u = line.split(" ")
            out.append((float(u[0]), (" ".join(u[1:]).strip())))
        out = sorted(out, key=lambda x: x[0], cmp=compare_with_ties, reverse=POINTS_DESC)
        with open(POINTS_FILE_PROCESSED, 'w') as fh:
            for line in out:
                print(line)
                fh.write(" ".join([str(line[0]), line[1]])+'\n')
        return out

if __name__ == '__main__':
    points()
    print("results saved in %s" % POINTS_FILE_PROCESSED)
