def bubble_up(heap, index):
    """Performs the bubble up operation to maintain the heap property.
    Moves the element at the given index up the heap until the heap property is restored."""
    parent_index = (index - 1) // 2

    if parent_index >= 0 and heap[parent_index][0] > heap[index][0]:
        heap[parent_index], heap[index] = heap[index], heap[parent_index]
        bubble_up(heap, parent_index)


def bubble_down(heap, index):
    """Performs the bubble down operation to maintain the heap property.
    Moves the element at the given index down the heap until the heap property is restored."""

    smallest = index  # Assume current index is the smallest
    left = 2 * index + 1  # Calculate left child index
    right = 2 * index + 2  # Calculate right child index

    if left < len(heap) and heap[left][0] < heap[smallest][0]:
        smallest = left

    if right < len(heap) and heap[right][0] < heap[smallest][0]:
        smallest = right

    # If the smallest is not the current index, swap and continue bubbling down
    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        bubble_down(heap, smallest)


def heappush(heap, item):
    """Adds a new item to the heap, maintaining the heap property."""
    heap.append(item)
    bubble_up(heap, len(heap) - 1)


def heappop(heap):
    """Removes and returns the smallest item from the heap, maintaining the heap property."""
    heap[0], heap[-1] = heap[-1], heap[0]
    item = heap.pop()

    if heap:
        bubble_down(heap, 0)

    return item


def distribute_fragments(data_center_risks: list, num_fragments: int) -> int:
    """Distributes a specified number of data fragments across a designated number of data centers,
    ensuring that the maximum risk associated with any set of fragments is minimized."""

    # Initialize a heap with each data center's initial risk, the number of fragments, and the base risk.
    heap = [(risk, 1, risk) for risk in data_center_risks]

    # Distribute fragments one at a time, recalculating and updating risks inside the the heap.
    for _ in range(num_fragments):
        current_risk, fragments, base_risk = heappop(heap)
        fragments += 1
        new_risk = base_risk**fragments
        heappush(heap, (new_risk, fragments, base_risk))

    # After distribution, get max risk.
    max_risk = max(heap)[0]
    return max_risk


data_centers = [10, 20, 30, 60, 22, 11, 110, 20, 50, 44, 1459]
fragments = 10

min_risk = distribute_fragments(data_center_risks=data_centers, num_fragments=fragments)

print(f"Minimized maximum risk: {min_risk}")
