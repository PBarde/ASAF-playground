from . import BaseAgent


class LearnableAgent(BaseAgent):
    """This is a learnable agent, basically a placeholder for which you have to overwrite the action"""

    def __init__(self, *args, **kwargs):
        super(LearnableAgent, self).__init__(*args, **kwargs)

    def act(self, obs, action_space):
        return None
