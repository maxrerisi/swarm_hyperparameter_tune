import math

def move_towards(a: tuple, b: tuple, L: float) -> tuple:
    if len(a) != len(b):
        raise SyntaxError("Tuples a and b should be the same length.")

    # Step 1: Calculate the vector from a to b
    vector = tuple(b_i - a_i for a_i, b_i in zip(a, b))
    
    # Step 2: Calculate the magnitude of the vector
    magnitude = math.sqrt(sum((b_i - a_i) ** 2 for a_i, b_i in zip(a, b)))
    
    # Step 3: Normalize the vector (if magnitude is non-zero)
    if magnitude == 0:
        unit_vector = tuple((b_i - a_i) for a_i, b_i in zip(a, b))
    else:
        unit_vector = tuple((b_i - a_i) / magnitude for a_i, b_i in zip(a, b))
        # raise ValueError("Points a and b are the same. No direction to move.")
    
    
    
    # Step 4: Scale the unit vector by L
    scaled_vector = tuple(L * u_i for u_i in unit_vector)
    
    # Step 5: Return the final position after moving L units
    return scaled_vector # returns the coords to move, not the new coords
    # result = tuple(a_i + s_i for a_i, s_i in zip(a, scaled_vector))
    
    # return result

# Example usage:
# a = (1, 2, 3)
# b = (4, 6, 8)
# L = 5

# result = move_towards(a, b, L)
# print(result)


def euclidean_distance(a: tuple, b: tuple) -> tuple:
    if len(a) != len(b):
        raise SyntaxError("Tuples a and b should be the same length.")
    

    vector = tuple(b_i - a_i for a_i, b_i in zip(a, b))
    magnitude = math.sqrt(sum((b_i - a_i) ** 2 for a_i, b_i in zip(a, b)))
    return magnitude