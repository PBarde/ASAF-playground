'''An example to show how to set up an pommerman game programmatically'''
import pommerman
from pommerman import agents
import numpy as np

PORTS = [1001, 1002, 1003, 1004]


# pom_battle --agents=test::agents.SimpleAgent,docker::multiagentlearning/navocado,player::arrows,docker::multiagentlearning/eisenach --config=PommeTeamCompetition-v0 --render


def main(type_of_games="one_vs_frozen", n_games=1, recording_folder="", render=True):
    '''Simple function to bootstrap a game.

       Use this as an example to set up your training env.
    '''
    # Print all possible environments in the Pommerman registry
    # print(pommerman.REGISTRY)

    if type_of_games == "one_vs_frozen":
        n_simulated = 1
        pool_of_agents = {
            # "simple_agent": {"builder": agents.SimpleAgent, "args": []},
            # "random_agent": {"builder": agents.RandomAgent, "args": []},
            # "dypm.1": {"builder": agents.DockerAgent,
            #            "args": ["multiagentlearning/dypm.1"]},
            # "dypm.2": {"builder": agents.DockerAgent,
            #            "args": ["multiagentlearning/dypm.2"]},
            "mcts" : {"builder": agents.DockerAgent, "args": ["pommerman/agent47agent"]}
        }
    else:
        pool_of_agents = {
            # "simple_agent": {"builder": agents.SimpleAgent, "args": []},
            #   "random_agent": {"builder": agents.RandomAgent, "args": []},
            #   "hakozakijuncitons": {"builder": agents.DockerAgent,
            #                         "args": ["multiagentlearning/hakozakijunctions"]},
            #   "eisenach": {"builder": agents.DockerAgent,
            #                "args": ["multiagentlearning/eisenach"]},
            # "frozen_agent": {"builder": agents.FreezeAgent, "args": []},
            # "dypm.1": {"builder": agents.DockerAgent,
            #            "args": ["multiagentlearning/dypm.1"]},
            # "dypm.2": {"builder": agents.DockerAgent,
            #            "args": ["multiagentlearning/dypm.2"]},
            # "navocado": {"builder": agents.DockerAgent,
            #              "args": ["multiagentlearning/navocado"]},
            # "skynet955": {"builder": agents.DockerAgent,
            #               "args": ["multiagentlearning/skynet955"]}
        }
        raise NotImplementedError

    agents_types = list(pool_of_agents.keys())

    for g in range(n_games):
        available_ports = PORTS.copy()
        # Create a set of agents ()
        random_indexes = np.random.randint(len(list(pool_of_agents.keys())), size=n_simulated)
        agent_list = []
        running_agents = []
        for id in random_indexes:
            running_agents.append(agents_types[id])
            agent_t = pool_of_agents[agents_types[id]]
            builder = agent_t["builder"]
            args = agent_t["args"]
            if args:
                agent_list.append(builder(args[0], available_ports.pop()))
            else:
                agent_list.append(builder())

        if type_of_games == "one_vs_frozen":
            # agent_list.append(agents.FreezeAgent())
            agent_list.append(agents.SimpleAgent())
            running_agents.append("frozen_agent")
            # env = pommerman.make('PommeTest-v0', agent_list)
            env = pommerman.make('OneVsOne-v0', agent_list)

        # Make the "Free-For-All" environment using the agent list
        # env = pommerman.make('PommeTeamCompetitionFast-v0', agent_list)

        transitions = []
        # Run the episodes just like OpenAI Gym
        for i_episode in range(n_games):
            state = env.reset()
            done = False
            while not done:
                if render:
                    env.render()
                action = env.act(state)
                next_state, reward, done, info = env.step(action)
                transitions.append({"states": state.copy(), "action": action.copy(), "reward": reward.copy(),
                                    "next_state": next_state.copy(),
                                    "done": done, "info": info.copy()})
                state = next_state
            print('Episode {} finished'.format(i_episode))
            print(info)
            summary = {'agents': running_agents, 'result':info['result'], 'winners':info['winners'],
                       'transitions': transitions}
            # file_name =
        env.close()


if __name__ == '__main__':
    main()
