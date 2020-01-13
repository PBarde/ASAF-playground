import os
import sys
import numpy as np

from pommerman.agents import *
from pommerman.configs import *
from pommerman.envs.v0 import Pomme
from pommerman.characters import Bomber
from pommerman import utility


# Instantiate the environment
config = ffa_competition_env()
env = Pomme(**config["env_kwargs"])

# def build_docker_agent(docker_image):
#     return DockerAgent(docker_image)
#
# agent_pool = {}
# Add 3 random agents
agents = {}
for agent_id in range(3):
    agents[agent_id] = SimpleAgent(config["agent"](agent_id, config["game_type"]))

# Add human agent
agents[3] = DockerAgent("multiagentlearning/navocado", "12345")
# agents[3] = SimpleAgent(config["agent"](3, config["game_type"]))

env.set_agents(list(agents.values()))
env.set_init_game_state(None)


# Seed and reset the environment
obs = env.reset()

# Run the agents until we're done
done = False
while not done:
    env.render()
    actions = env.act(obs)
    obs, reward, done, info = env.step(actions)

env.render(close=True)
env.close()

# Print the result
print(info)