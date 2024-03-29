Delivery Truck Dispatch System

**Algorithm Identification**
The program uses the Nearest Neighbor algorithm for package delivery. The algorithm looks for the nearest delivery address, moves to it, and repeats. It is self-adjusting, updating the delivery order as new packages are added.

**Overview**
The program reads package and distance data from CSV files and stores them in hash tables and 2D arrays. Packages are split into 3 lists, determining which truck they are assigned to. Each truck accesses its own packages in the hash table using a filtered list. The nearest neighbor algorithm is used to order the delivery addresses, determining the delivery route for each truck. A Truck object is created with a reference to the main hash table and its delivery route, as well as a start time (converted to timedelta). The truck delivers all its packages and keeps track of total distance.

The user interface allows the user to view all packages at a specific time, view a specific package at a specific time, and see the total distance for each truck and the sum of all truck distances.

The current implementation has a time complexity of O(n^3) and a space complexity of O(n^2). As the number of packages increases, the performance of the program will degrade. The chaining hash table implementation will scale well with more packages, however, the nearest neighbor algorithm will not scale as well and will become the bottleneck in terms of performance. To improve the scalability, the nearest neighbor algorithm could be replaced with a more efficient algorithm such as k-d trees or a divide-and-conquer algorithm. The program would also benefit from optimization and parallelization of computations where possible.

The program uses a chaining hash-table as its data structure. It takes the unique package ID as a parameter and returns the package object with the matching package ID. The program implements the nearest neighbor algorithm to deliver packages in the most efficient way. The strengths of the nearest neighbor algorithm are its intuitiveness and ability to be changed on the fly, while the weaknesses are that it may not always produce the shortest list and could be more complex than other algorithms such as Dijkstra's algorithm and farthest insertion algorithm. The program meets all requirements by delivering all packages within the required 140 miles and on time, and requires only two drivers to drive three trucks.
