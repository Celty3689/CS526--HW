def simulate_pandemic(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            n = int(lines[0])
            infected_cells = []

            # Read the infection coordinates.
            for i in range(1, len(lines)):
                if lines[i]:
                    x, y = map(int, lines[i].split())
                    infected_cells.append((x, y))

            # Initialize the grid
            grid = [[0 for _ in range(n)] for _ in range(n)]

            # Mark the initially infected counties.
            for x, y in infected_cells:
                if 0 <= x < n and 0 <= y < n:
                    grid[x][y] = 1

            # Direction of infection: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            changed = True
            while changed:
                changed = False
                new_infections = []

                # Check all healthy counties.
                for i in range(n):
                    for j in range(n):
                        if grid[i][j] == 0:  # Healthy County
                            infected_neighbors = 0
                            # Calculate the number of infected neighbors (considering edge)
                            for dx, dy in directions:
                                ni, nj = i + dx, j + dy
                                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                                    infected_neighbors += 1

                            # If there are at least two infected neighbors, mark it
                            if infected_neighbors >= 2:
                                new_infections.append((i, j))
                                changed = True

                # New infection
                for x, y in new_infections:
                    grid[x][y] = 1

            # Check if there are any remaining healthy counties.
            healthy_count = 0
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 0:
                        healthy_count += 1

            return healthy_count > 0

    except Exception:
        return None

def check_all_pandemic_files():
    files = ['pandemic_input1.txt', 'pandemic_input2.txt']

    for filename in files:
        result = simulate_pandemic(filename)
        if result:
            print(f"{filename}: There are healthy counties left")
        else:
            print(f"{filename}: There are no healthy counties left")

if __name__ == "__main__":
    check_all_pandemic_files()