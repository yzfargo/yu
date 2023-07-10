def calculate_displacement(initial_velocity, acceleration, time):
    """Calculates the displacement using the SVT equation."""
    displacement = initial_velocity * time + 0.5 * acceleration * time**2
    return displacement

def calculate_final_velocity(initial_velocity, acceleration, time):
    """Calculates the final velocity using the SVT equation."""
    final_velocity = initial_velocity + acceleration * time
    return final_velocity

def calculate_time(initial_velocity, final_velocity, acceleration):
    """Calculates the time using the SVT equation."""
    time = (final_velocity - initial_velocity) / acceleration
    return time

# Example usage
initial_velocity = 10  # m/s
acceleration = 2  # m/s^2
time = 5  # s

displacement = calculate_displacement(initial_velocity, acceleration, time)
final_velocity = calculate_final_velocity(initial_velocity, acceleration, time)
calculated_time = calculate_time(initial_velocity, final_velocity, acceleration)

print("SVT Equations")
print(f"Initial Velocity: {initial_velocity} m/s")
print(f"Acceleration: {acceleration} m/s^2")
print(f"Time: {time} s")
print(f"Displacement: {displacement} m")
print(f"Final Velocity: {final_velocity} m/s")
print(f"Calculated Time: {calculated_time} s")
