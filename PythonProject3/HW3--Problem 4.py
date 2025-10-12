import math
def do_lines_intersect_as_lines(p1, p2, p3, p4):
    """Check if two stright lines intersect"""
    #Calculate vectors of the two lines
    dir1 = (p2[0] - p1[0], p2[1] - p1[1])
    dir2 = (p4[0] - p3[0], p4[1] - p3[1])

    #Check if lines are parallel using cross product
    if dir1[0] * dir2[1] == dir1[1] * dir2[0]:
        if (p3[0] - p1[0]) * dir1[1] == (p3[1] - p1[1]) * dir1[0]:
            return True #Coincident lines are considered intersecting
        else:
            return False #Parallel but not coincident, no intersection
    else:
        return True


def check_no_crossing_lines(pairs):
    """Check if all ghostbuster-ghost lines have no intersections"""
    n = len(pairs)
    #Check all pairs of lines
    for i in range(n):
        for j in range(i + 1, n):
            b1, g1 = pairs[i]  #First pair
            b2, g2 = pairs[j]  #Second pair
            #If any two lines intersect, return False
            if do_lines_intersect_as_lines(b1, g1, b2, g2):
                return False
    return True  #All lines are non-intersecting


def main():
    #test all 9 files
    for i in range(9):
        filename = f"ghostbusters_input_{i}.txt"
        try:
            with open(filename, 'r') as f:
                #Read number of ghostbuster-ghost pairs
                n = int(f.readline().strip())
                pairs = []
                #Read each pair from the file
                for j in range(n):
                    parts = f.readline().strip().split()
                    #Parse ghostbuster and ghost coordinates
                    buster_coord = (float(parts[1]), float(parts[2]))
                    ghost_coord = (float(parts[4]), float(parts[5]))
                    pairs.append((buster_coord, ghost_coord))

            #Check if all lines are non-intersecting
            if check_no_crossing_lines(pairs):
                print("All Ghosts: were eliminated")
            else:
                print("All Ghosts: were not eliminated")

        except:
            #If file reading fails
            print("All Ghosts: were not eliminated")

if __name__ == "__main__":
    main()