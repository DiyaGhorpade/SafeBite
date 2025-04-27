
from faker import Faker
import random
import pandas as pd

fake = Faker()

# Define custom values
food_types = ['Milk', 'Wheat', 'Honey', 'Chili Powder', 'Turmeric']
adulterants = {
    'Milk': ['Water', 'Detergent', 'Starch', 'Urea'],
    'Wheat': ['Soapstone', 'Chalk Powder'],
    'Honey': ['Sugar Syrup', 'Jaggery Syrup'],
    'Chili Powder': ['Brick Powder', 'Salt Powder'],
    'Turmeric': ['Metanil Yellow', 'Chalk Powder']
}

def generate_food_sample(sample_id):
    food = random.choice(food_types)
    adulterated = random.choices([True, False], weights=[0.55, 0.45])[0]  # tilt slightly towards adulterated

    # Add label noise to 5% of samples
    if random.random() < 0.05:
        adulterated = not adulterated

    if adulterated:
        adulterant = random.choice(adulterants[food])
        level = round(random.uniform(0.05, 5.0), 2)
    else:
        adulterant = 'None'
        level = round(random.uniform(0.0, 0.2), 2)  # not always 0!

    return {
        'sample_id': sample_id,
        'food_type': food,
        'adulterant': adulterant,
        'adulteration_level': level,
        'is_adulterated': adulterated
    }

# Generate a DataFrame
data = [generate_food_sample(i) for i in range(1, 501)]
df = pd.DataFrame(data)

print(df)

# Save to CSV
df.to_csv('food_adulteration_samples1.csv', index=False)