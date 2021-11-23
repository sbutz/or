#!/usr/bin/env python3

import math


def main():
    c = loadGraph('./Blatt_06_bier127.tsp')
    print(c)

def loadGraph(filename):
    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    content = content[content.index('NODE_COORD_SECTION')+1 : -1]

    points = []
    for line in content:
        parts = line.split()
        points.append({
            'x': float(parts[1]),
            'y': float(parts[2]),
        })

    c = [[None for j in points] for i in points]
    for i, a in enumerate(points):
        for j, b in enumerate(points):
            c[i][j] = distance(a,b)
    return c


def distance(a, b):
    return math.sqrt((a['x']-b['x'])**2 + (a['y']-b['y'])**2)


if __name__ == "__main__":
    main()
