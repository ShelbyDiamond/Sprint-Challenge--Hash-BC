#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    print(f"Weights: {weights}")
    print(f"Length: {length}")
    print(f"Limit: {limit}")

    for index in range(length):
        weight_check = hash_table_retrieve(ht, limit - weights[index])  # checking for none
        if weight_check is None:
            hash_table_insert(ht, weights[index], index)
            print(f"weights index: {index} \t value there: {weights[index]}")
        else:
            tup = (index, weight_check)
            return tup


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
my_weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(my_weights, 5, 21))
