#15-4. Modified Random Walks: In the class RandomWalk, x_step and y_step are generated from the same set of conditions. The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. Modify the values in these lists to see what happens to the overall shape of your walks. Try a longer list of choices for the distance, such as 0 through 8, or remove the –1 from the x or y direction list.

#15-5. Refactoring: The method fill_walk() is lengthy. Create a new method called get_step() to determine the direction and distance for each step, and then calculate the step. You should end up with two calls to get_step() in fill_walk():

# x_step = get_step()
# y_step = get_step()

# This refactoring should reduce the size of fill_walk() and make the method easier to read and understand.

from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance

        return step

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
           # Decide which direction to go and how far to go in that direction.
           
            x_step = self.get_step()
            y_step = self.get_step()

           # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

           # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

   
