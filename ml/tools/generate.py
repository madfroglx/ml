import numpy as np
from numpy import random


def generate_data(num_samples=70, num_features=2):
    features = np.random.randint(0, 100, (num_samples, num_features))
    labels = np.random.randint(0, 2, num_samples)
    return features, labels


def generate_basorexia_data(num_entries):
    list_entries = []
    for entry_count in range(num_entries):
        new_entry = {}
        new_entry['age'] = random.randint(20, 100)
        new_entry['sex'] = random.choice(['M', 'F'])
        new_entry['BP'] = random.choice(['low', 'high', 'normal'])
        new_entry['cholestrol'] = random.choice(['low', 'high', 'normal'])
        new_entry['Na'] = random.random()
        new_entry['K'] = random.random()
        new_entry['drug'] = random.choice(['A', 'B', 'C', 'D'])
        list_entries.append(new_entry)
    return list_entries
