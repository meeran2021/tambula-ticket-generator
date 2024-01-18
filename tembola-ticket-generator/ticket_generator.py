# ticket_generator.py
import numpy as np
import json

def generate_ticket():
    """
    Generates a single ticket based on the specified rules.
    """
    ticket_matrix = np.full(45, 1).reshape(9, 5)
    ticket_matrix[:6, :] *= 0
    [np.random.shuffle(ticket_matrix[:, col]) for col in range(5)]

    for row in range(9):
        numbers_in_column = np.arange(1, 11)
        np.random.shuffle(numbers_in_column)
        selected_numbers = np.sort(numbers_in_column[:5])
        ticket_matrix[row, :] *= (selected_numbers + row * 10)

    return ticket_matrix.T.tolist()

def generate_unique_tickets(num_tickets):
    """
    Generates a specified number of unique tickets.
    """
    unique_tickets_set = set()

    while len(unique_tickets_set) < num_tickets:
        ticket = generate_ticket()

        # Convert the ticket to a tuple and add it to the set
        ticket_tuple = tuple(map(tuple, ticket))
        unique_tickets_set.add(ticket_tuple)

    return list(map(list, unique_tickets_set))
