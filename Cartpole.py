import numpy as np
import math

# Physics constants
gravity = 9.8  # Acceleration due to gravity
cart_mass = 1.0  # Mass of the cart
pole_mass = 0.1  # Mass of the pole
total_mass = cart_mass + pole_mass  # Total mass
pole_length = 0.5  # Length of the pole (half-length used)
pole_mass_length = pole_mass * pole_length
force_magnitude = 10.0  # Magnitude of the force applied to the cart
time_step = 0.02  # Time between updates in seconds
angle_threshold = 12 * 2 * math.pi / 360  # Angle threshold for falling
position_threshold = 2.4  # Position threshold for falling off

# State variables: [cart position, cart velocity, pole angle, pole angular velocity]
state = np.random.uniform(low=-0.05, high=0.05, size=(4,))
steps_after_done = None

def reset():
    global state, steps_after_done
    # Reset the environment to a random initial state
    state = np.random.uniform(low=-0.05, high=0.05, size=(4,))
    steps_after_done = None
    return np.array(state)

def step(action):
    global state, steps_after_done
    # Update the environment based on the action taken
    cart_position, cart_velocity, pole_angle, pole_angular_velocity = state

    # Determine the force applied based on the action (0 = left, 1 = right)
    force = force_magnitude if action == 1 else -force_magnitude

    # Calculate physics
    cos_angle = math.cos(pole_angle)
    sin_angle = math.sin(pole_angle)

    temp = (force + pole_mass_length * pole_angular_velocity ** 2 * sin_angle) / total_mass
    pole_acceleration = (gravity * sin_angle - cos_angle * temp) / (
        pole_length * (4.0 / 3.0 - pole_mass * cos_angle ** 2 / total_mass))
    cart_acceleration = temp - pole_mass_length * pole_acceleration * cos_angle / total_mass

    # Update state with new values
    cart_position += time_step * cart_velocity
    cart_velocity += time_step * cart_acceleration
    pole_angle += time_step * pole_angular_velocity
    pole_angular_velocity += time_step * pole_acceleration
    state = (cart_position, cart_velocity, pole_angle, pole_angular_velocity)

    # Check if the episode is done (i.e., the pole fell or the cart went out of bounds)
    done = (cart_position < -position_threshold or cart_position > position_threshold or
            pole_angle < -angle_threshold or pole_angle > angle_threshold)
    done = bool(done)

    # Assign rewards
    if not done:
        reward = 1.0  # Continue to balance the pole
    elif steps_after_done is None:
        # The pole just fell
        steps_after_done = 0
        reward = 1.0  # Still reward for the last step
    else:
        if steps_after_done == 0:
            print("The pole has fallen!")
        steps_after_done += 1
        reward = 0.0  # No reward after the episode is done

    return np.array(state), reward, done, {}

def render():
    # Print the current state in a human-readable format
    print(f"Current State: Position: {state[0]:.2f}, Velocity: {state[1]:.2f}, "
          f"Angle: {state[2]:.2f}, Angular Velocity: {state[3]:.2f}")

# Basic simulation loop to step through the environment
def simulate():
    global state
    episodes = 2  # Number of episodes to run

    for episode in range(episodes):
        state = reset()  # Reset the environment for a new episode
        done = False  # Flag to check if the episode is finished
        time_steps = 0  # Count of time steps taken

        while not done:
            render()  # Show the current state
            action = np.random.choice(2)  # Choose a random action: 0 (left) or 1 (right)
            next_state, reward, done, _ = step(action)  # Take a step in the environment
            time_steps += 1

            if done:
                print(f"Episode finished after {time_steps} time steps.")
                break

# Run the simulation
simulate()
