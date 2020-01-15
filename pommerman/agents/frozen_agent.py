from . import BaseAgent
from .. import constants


class FrozenAgent(BaseAgent):
    """This is a agent that just sits there."""

    def __init__(self, *args, **kwargs):
        super(FrozenAgent, self).__init__(*args, **kwargs)

    def act(self, obs, action_space):
        return constants.Action.Stop.value
