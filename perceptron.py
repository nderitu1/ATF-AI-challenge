import numpy as np


def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-x))


def perceptron(inputs, weights, bias):
    """
    Simple perceptron implementation.

    Args:
        inputs: Array of input values
        weights: Array of weights
        bias: Bias term

    Returns:
        float: Output after activation
    """

    # Calculate weighted sum
    weighted_sum = np.dot(inputs, weights) + bias

    # Apply activation function
    output = sigmoid(weighted_sum)

    return output


# Predicting whether I will study Python today
# Features:
# [hours_of_sleep, free_time_hours, energy_level]

person_features = np.array([8, 2, 0.8])

# Weights
weights = np.array([0.3, 0.5, 0.7])

# Bias
bias = -0.5


# Make prediction
prediction = perceptron(person_features, weights, bias)


# Display result
print(f"Probability of studying Python: {prediction:.2%}")

print(
    f"Prediction: "
    f"{'Will study Python' if prediction > 0.5 else 'Will not study Python'}"
)