from collections import Counter

historical_activities = [
    0, 1, 2, 1, 3, 5, 4, 1, 3, 4,
    0, 1, 2, 1, 3, 5, 1, 4, 0
]

activity_names = {
    0: 'Sleep',
    1: 'TikTok',
    2: 'Exercise',
    3: 'Snack',
    4: 'Work',
    5: 'Read'
}


def calculate_probabilities(sequence):

    counts = Counter(sequence)
    total = len(sequence)

    probabilities = {
        activity: count / total
        for activity, count in counts.items()
    }

    return probabilities


# Calculate probabilities
probs = calculate_probabilities(historical_activities)


# Display ALL activities
print("Probability of All Activities:\n")

for activity in sorted(activity_names):
    
    probability = probs.get(activity, 0)

    print(
        f"{activity_names[activity]}: "
        f"{probability:.2%}"
    )