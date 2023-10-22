from robot import Robot

def setup_robot(grid_size):
    """ Initialise the robot name, ID, and initial position and direction.

    Args:
        grid_size (int): The size of the grid.

    Returns:
        str : Robot name
        int : Robot ID
        int : Robot's row coordinate
        int : Robot's column coordinate
        str : Robot's direction ("n", "s", "e", or "w")
    """
    name = None
    id = 0
    row = 0
    col = 0
    direction = "n"
    return (name, id, row, col, direction)


def print_robot_greeting(name, identifier):
    print(f"Hello. My name is {name}. My ID is {identifier}.")


def navigate(current_direction,
             current_row,
             current_col,
             target_row,
             target_col,
             grid_size):
    pass


def run_simulation(grid_size=10, target_row=9, target_col=9):
    """ Start robot navigation simulation.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
        target_row (int): The target row coordinate. Defaults to 9.
        target_col (int): The target column coordinate. Defaults to 9.
    """
    name, identifier, row, col, direction = setup_robot(grid_size)
    print_robot_greeting(name, identifier)
    navigate(direction, row, col, target_row, target_col, grid_size)


grid_size = 10
run_simulation(grid_size=grid_size)