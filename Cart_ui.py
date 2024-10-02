import gym

# Create the CartPole environment with render mode
env = gym.make("CartPole-v1", render_mode="human")

def Random_games():
    # Each of these episodes is its own game.
    for episode in range(10):
        state = env.reset()
        for t in range(500):
            env.render()  # Render the environment
            
            # Create a sample action
            action = env.action_space.sample()

            # Execute the action
            next_state, reward, terminated, truncated, info = env.step(action)
            
            # Print details
            print(t, next_state, reward, terminated, truncated, info, action)

            # Use 'terminated' to determine if the episode is done
            if terminated:
                break
                
# Run the random games function
Random_games()

# Close the environment
env.close()