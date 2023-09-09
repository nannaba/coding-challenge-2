import sys
import numpy as np


def readInfo(filename):
    """
    Read information from a file.
    Returns the input radius, number of points, and points
    """
    try:
        with open(filename) as f:
            r, p = next(f).strip(), next(f).strip()
            # check if r and p are correct
            try:
                r = float(r)
                p = int(p)
            except ValueError:
                print('Error: Radius or number of points not properly specified')
                sys.exit(1)
        try:
            points = np.genfromtxt(filename, skip_header=2)
            # check if dimensions are correct
            if points.shape[1] != 3:
                print('Error: Points should be 3D, x y z')
                sys.exit(1)
            if points.shape[0] != p:
                print('Error: Number of points given does not equal specified number of points')
                sys.exit(1)
            return r, p, points
        except ValueError:
            print('Error: Points not properly formatted')
            sys.exit(1)
    except IOError:
        print("Error: Can't find file, please change file path on line 66")
        sys.exit(1)


def euclideanDistance(i, p, points):
    """
    Calculates the Euclidean distance between the points
    """
    dist = np.zeros(p)
    for j in range(p):
        # can be done using numpy.linalg.norm
        dist[j] = np.linalg.norm(points[i] - points[j])
    return dist


def nearestNeighbor(r, i, p, points):
    """
    Finds the nearest neighbors to a point.
    Returns a list of the indices of the neighbors.
    """
    # find the Euclidean distance between this point and all the others
    distance = euclideanDistance(i, p, points)
    neighbors = []
    for i in range(p):
        # if the distance is <= radius then it's a neighbor
        if distance[i] <= r and distance[i] != 0:
            neighbors.append(i)
    return neighbors


def main():
    # get information from input file
    filename = 'neighbors.txt'  # change file path here
    r, p, points = readInfo(filename)

    # find nearest neighbors for every point
    for i in range(p):
        neighbors = nearestNeighbor(r, i, p, points)
        n = ', '.join([str(m) for m in neighbors])
        print(str(i) + ': ' + n)


if __name__ == "__main__":
    main()
