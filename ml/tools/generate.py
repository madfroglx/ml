import numpy as np


def generate_data(num_samples=70, num_features=2):
    features = np.random.randint(0, 100, (num_samples, num_features))
    labels = np.random.randint(0, 2, num_samples)
    return features, labels
