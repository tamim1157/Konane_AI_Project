import heapq

# Define a state class to represent each node in the grid
class State:
    def __init__(self, row, col, cost):
        self.row = row
        self.col = col
        self.cost = cost
    
    # Define a custom comparator for priority queue
    def __lt__(self, other):
        return self.cost < other.cost

# Define the AStar class
class AStar:
    def __init__(self):
        self.grid = [
            ['.', '.', 'x'],
            ['.', 'x', '.'],
            ['.', '.', '.']
        ]
        self.source = (0, 0)
        self.destination = (2, 2)
        self.n = len(self.grid)
    
    # Define a heuristic function to estimate the remaining cost (Manhattan distance)
    def heuristic(self, source, dest):
        return abs(dest[0] - source[0]) + abs(dest[1] - source[1])

    # A* search algorithm to find the total cost of the path
    def find_path_cost(self, heuristic_matrix):
        pq = []
        heapq.heappush(pq, State(self.source[0], self.source[1], 0))
        visited = set()

        while pq:
            current = heapq.heappop(pq)

            if (current.row, current.col) == self.destination:
                return current.cost
            
            if (current.row, current.col) in visited:
                continue
            visited.add((current.row, current.col))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = current.row + dr, current.col + dc

                if 0 <= new_row < self.n and 0 <= new_col < self.n and self.grid[new_row][new_col] != 'x':
                    new_cost = current.cost + heuristic_matrix[new_row][new_col]
                    heapq.heappush(pq, State(new_row, new_col, new_cost))

        return -1  # Return -1 if no path is found

# Example usage in another Python file
if __name__ == "__main__":
    heuristic_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    astar = AStar()
    cost = astar.find_path_cost(heuristic_matrix)

    if cost == -1:
        print("No path found!")
    else:
        print(f"Total cost: {cost}")
