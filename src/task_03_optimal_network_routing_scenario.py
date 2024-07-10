from heapq import heappush, heappop


def find_minimum_latency_path(graph, compression_nodes, source, target):

    to_visit = [(0, source, False)]

    # Track the best latency to each node
    visited = {(node, compression): float("inf") for node in graph for compression in [False, True]}
    visited[(source, False)] = 0

    while to_visit:
        current_time, node, compression_used = heappop(to_visit)

        # If we've reached the destinatoin, return the time it took
        if node == target:
            return current_time

        for neighbor, travel_time in graph[node]:
            time_to_neighbor = current_time + travel_time

            if time_to_neighbor < visited[(neighbor, compression_used)]:
                visited[(neighbor, compression_used)] = time_to_neighbor
                heappush(to_visit, (time_to_neighbor, neighbor, compression_used))

            if not compression_used and node in compression_nodes:
                compressed_time = current_time + travel_time // 2  # Apply compression

                if compressed_time < visited[(neighbor, True)]:
                    visited[(neighbor, True)] = compressed_time
                    heappush(to_visit, (compressed_time, neighbor, True))

    # Return considerng both times
    return min(visited[(target, False)], visited[(target, True)])


graph = {"A": [("B", 10), ("C", 20)], "B": [("D", 15)], "C": [("D", 30)], "D": []}
compression_nodes = ["B", "C"]
source = "A"
target = "D"

min_latency = find_minimum_latency_path(graph, compression_nodes, source, target)

print(f"Minimum total latency: {min_latency}")
