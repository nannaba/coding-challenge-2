# coding-challenge-2

Nearest Neighbors Algorithm

Description
For this challenge, please write a program that takes as input:
1. A floating point radius 𝑟𝑟,
2. The number of points 𝑁𝑁,
3. A series of lines of 3D points with each coordinate separated by a space
The ID for each point is generated sequentially starting from 0 and incrementing by 1. Your program should print to the screen for each node the node id, followed by a colon, followed by a comma separated list the id of each neighbor to that node. A neighbor of a node 𝑛𝑛 is another node 𝑛𝑛𝑖𝑖 whose distance from 𝑛𝑛 is less than 𝑟𝑟. Formally, the neighbors of a node 𝑛𝑛 is the set of nodes {𝑛𝑛𝑖𝑖|‖𝑛𝑛−𝑛𝑛𝑖𝑖‖<𝑟𝑟}. See the example output below.
Please discuss the time and space complexity of your solution and any implementation decisions that you feel were important when writing your program.
Input Format
r (input radius)
N (number of points)
x1 y1 z1
…
xN yN zN
Output Format
0: 𝑛𝑛00,…,𝑛𝑛𝑚𝑚00 … N-1: 𝑛𝑛0𝑁𝑁−1,…,𝑛𝑛𝑚𝑚𝑁𝑁−1𝑁𝑁−1
Where 𝑛𝑛𝑗𝑗𝑖𝑖 denotes node 𝑖𝑖’s 𝑗𝑗th neighbor.
Constraints
• 1≤𝑛𝑛≤105, where 𝑛𝑛 is the number of nodes.
• {(𝑥𝑥,𝑦𝑦,𝑧𝑧) ∈ℝ3:−107≤𝑥𝑥,𝑦𝑦,𝑧𝑧≤ 107}
• The node IDs are enumerated from 1 to 𝑛𝑛.
• There are no other constraints on the input. You may format the input however you wish.
Example
We can consider the case where one corner is at (0, 0, 0) and the far corner is at (1, 1, 1). The input would then be:
1.0
9
0 0 0
1 0 0
0 1 0
0 0 1
1 1 0
0 1 1
1 0 1
1 1 1
0.5 0.5 0.5
The output should be:
0: 1, 2, 3, 8
1: 0, 4, 6, 8
2: 0, 4, 5, 8
3: 0, 5, 6, 8
4: 1, 2, 7, 8
5: 2, 3, 7, 8
6: 1, 3, 7, 8
7: 4, 5, 6, 8
8: 0, 1, 2, 3, 4, 5, 6, 7
