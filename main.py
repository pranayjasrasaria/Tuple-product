from functools import reduce
import operator

def safe_product(values):
    """
    Compute the product of all numbers in an iterable.
    Includes input validation and error handling.
    """
    # Validate that input is a tuple
    if not isinstance(values, tuple):
        raise TypeError("Input must be a tuple.")

    # Validate that all items are numbers
    for item in values:
        if not isinstance(item, (int, float)):
            raise ValueError("All elements in the tuple must be numbers.")

    # Handle empty tuple case
    if len(values) == 0:
        return 1  # Neutral element for multiplication

    # Compute product
    return reduce(operator.mul, values, 1)

# Given tuples
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 2, 3, 9)

try:
    product1 = safe_product(tup1)
    product2 = safe_product(tup2)

    print("Product of tup1:", product1)
    print("Product of tup2:", product2)

except (TypeError, ValueError) as e:
    print("Error:", e)