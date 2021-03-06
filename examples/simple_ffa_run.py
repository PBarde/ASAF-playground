
'''An example to show how to set up an pommerman game programmatically'''
import pommerman
from pommerman import agents

def print_state(state):
    for key in state:
        print(f'{key} : {state[key]}\n')

def main():
    '''Simple function to bootstrap a game.
       
       Use this as an example to set up your training env.
    '''
    # Print all possible environments in the Pommerman registry
    # print(pommerman.REGISTRY)

    # Create a set of agents (exactly four)
    agent_list = [
        # agents.SimpleAgent(),
        agents.SimpleAgent(),
        agents.FrozenAgent(),
        # agents.SimpleAgent(),
        # agents.RandomAgent(),
        # agents.DockerAgent("multiagentlearning/hakozakijunctions", port=12345),
        # agents.DockerAgent("multiagentlearning/eisenach", port=1000),
        # agents.DockerAgent("multiagentlearning/eisenach", port=1002),
        # agents.StateAgentExploit(),
        # agents.StateAgentExploit(),
        # agents.DockerAgent("multiagentlearning/eisenach", port=48),
        # agents.DockerAgent("multiagentlearning/eisenach", port=15),
        # agents.DockerAgent("multiagentlearning/skynet955", port=12347),
    ]
    # Make the "Free-For-All" environment using the agent list
    env = pommerman.make('PommeFFACompetition-v0', agent_list)
    # env = pommerman.make('PommeTeamCompetition-v0', agent_list)
    # env = pommerman.make('OneVsOne-v0', agent_list)
    # Run the episodes just like OpenAI Gym
    for i_episode in range(1):
        state = env.reset()
        done = False
        while not done:
            env.render()
            actions = env.act(state)
            print(f'++++++++++++AGENT 0+++++++++++++++++\n')
            print_state(state[0])
            print(f'++++++++++++AGENT 1+++++++++++++++++\n')
            print_state(state[1])
            state, reward, done, info = env.step(actions)
        print('Episode {} finished'.format(i_episode))
        print(info)
    env.close()


if __name__ == '__main__':
    main()
