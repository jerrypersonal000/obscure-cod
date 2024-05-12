import streamlit as st
from collections import deque

def shortest_path_to_range(A, B, C):
    queue = deque([(A, 0, [])])
    visited = set()
    operations = list(range(1, 10))
    max_limit = 30000  # Set a numeric upper limit
    max_queue_length = 10000  # Maximum queue length to prevent memory overflow

    lower_bound = min(B, C)
    upper_bound = max(B, C)

    while queue and len(queue) < max_queue_length:
        current, steps, path = queue.popleft()
        
        if lower_bound <= current <= upper_bound:
            return steps, path
        
        if abs(current) > max_limit:
            continue
        
        if steps > 100:  # Arbitrary step limit to prevent too long paths
            continue
        
        for op in operations:
            next_steps = [
                (current + op, f"{current} + {op} = {current + op}"),
                (current - op, f"{current} - {op} = {current - op}"),
                (current * op, f"{current} * {op} = {current * op}"),
                (current // op if op != 0 else None, f"{current} // {op} = {current // op}" if op != 0 else None)
            ]
            for result, desc in next_steps:
                if result is not None and result not in visited and abs(result) <= max_limit:
                    visited.add(result)
                    if len(queue) < max_queue_length:  # Check queue length before appending
                        queue.append((result, steps + 1, path + [desc]))
    
    return -1, []

A = st.number_input("Enter initial value A: ", step=1)
B = st.number_input("Enter one boundary of the range: ", step=1)
C = st.number_input("Enter the other boundary of the range: ", step=1)

steps, path = shortest_path_to_range(A, B, C)
if steps != -1:
    st.write(f"The shortest path from {A} to the range [{lower_bound}, {upper_bound}] requires {steps} steps")
    st.write("The operations are as follows:")
    for p in path:
        st.write(p)
else:
    st.write(f"No path found from {A} to the range [{lower_bound}, {upper_bound}].")
