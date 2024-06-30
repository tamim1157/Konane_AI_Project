from A_Star import AStar
from Genetic import Genetic

heuristic_matrix = []
matrix_row = []
for i in range(9):
    ans = Genetic.main()
    matrix_row.append(ans)
    if(i+1)%3==0:
        heuristic_matrix.append(matrix_row)
        matrix_row = []

print(heuristic_matrix)
astar = AStar()
cost = astar.find_path_cost(heuristic_matrix)

if cost == -1:
    print("No path found!")
else:
    print(f"Total cost: {cost}")