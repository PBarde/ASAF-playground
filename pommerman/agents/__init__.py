'''Entry point into the agents module set'''
from .base_agent import BaseAgent
from .docker_agent import DockerAgent
from .http_agent import HttpAgent
from .player_agent import PlayerAgent
from .player_agent_blocking import PlayerAgentBlocking
from .random_agent import RandomAgent
from .simple_agent import SimpleAgent
from .tensorforce_agent import TensorForceAgent
from .yichen_agent import YichenAgent
from .aggressive_agent import AggressiveAgent
from .mcts_agent import MCTSAgent
from .state_agent_exploit import StateAgentExploit
from .state_agent_explore import StateAgentExplore
from .state_agent_standard import StateAgentStandard
from .state_agent_bfs import StateAgentBFS
from .dummy_agent import DummyAgent
from .frozen_agent import FrozenAgent
from .learnable_agent import LearnableAgent
from .pacific_agents import RandomPacifist, SimplePacifist