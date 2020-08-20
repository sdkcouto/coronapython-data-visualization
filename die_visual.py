#15-6. Automatic Labels: Modify die_visual.py and dice_visual.py by replacing the list we used to set the value of hist.x_labels with a loop to generate this list automatically. If you’re comfortable with list comprehensions, try replacing the other for loops in die_visual.py and dice_visual.py with comprehensions as well.


import pygal

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

print(frequencies)