"""
When to use list comp vs generator expression.
Shows: list supports multiple passes / indexing; generator is one-shot.
"""

# --- Same data, list vs generator ---
data = [1, 2, 3, 4, 5]
squares_list = [x * x for x in data]
squares_gen = (x * x for x in data)

# --- LIST: multiple passes work (sequence is stored in memory) ---
print("--- LIST (multiple passes) ---")
print("  First pass  sum(squares_list):", sum(squares_list))   # 55
print("  Second pass sum(squares_list):", sum(squares_list))   # 55 again
print("  Indexing    squares_list[0]:  ", squares_list[0])      # 1

# --- GENERATOR: only first pass has data; then it's exhausted ---
print("--- GENERATOR (one pass only) ---")
print("  First pass  sum(squares_gen): ", sum(squares_gen))    # 55
print("  Second pass sum(squares_gen): ", sum(squares_gen))    # 0 (already exhausted!)
# print(squares_gen[0])  # TypeError: 'generator' object is not subscriptable
print("  (no indexing; generator has no [0])")

# --- Use generator when you only need one pass ---
total_once = sum(x * x for x in data)  # one pass, no list in memory
print("--- Gen exp, single use: sum =", total_once)
