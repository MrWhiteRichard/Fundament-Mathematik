# ---------------------------------------------------------------- #

import random
from collections import defaultdict

# ---------------------------------------------------------------- #

def argsmax(A):

    if type(A) == dict or type(A) == defaultdict:
        maximum = max(A.values())
        return [i for i, a in A.items() if a == maximum]

    elif type(A) == list:
        maximum = max(A)
        return [i for i, a in enumerate(A) if a == maximum]

    else:
        raise NotImplementedError

# ---------------------------------------------------------------- #

class Policy(object):

    def __init__(self, action_space, data=None, epsilon=1, Q=None):

        assert 0 <= epsilon <= 1

        self.action_space = action_space

        self.epsilon = epsilon
        self.Q = Q

        self.data = data

    def set_data(self, data=None):

        if data is None:
            self.reset()
        else:
            self.__data = data

    def get_data(self):
        return self.__data

    data = property(get_data, set_data)

    def reset(self):

        # with probability epsilon, choose uniformally from all actions
        self.data = defaultdict(
            lambda: {
                str(action): self.epsilon / self.action_space.size
                for action in self.action_space
            }
        )

        # check if policy should be at least a little bit greedy ...
        if self.epsilon < 1:

            # ... w.r.t. Q, which should not be None
            assert self.Q is not None

            # only reset the specified states
            for str_state in self.Q.keys():

                # get actions that share the privilege of being selected from with remaining probability 1 - epsilon
                str_actions_max = argsmax(self.Q[str_state])

                # there should be at least 1 maximising action (otherwise, self.Q[str_state] was an empty dict)
                assert len(str_actions_max) > 0

                # actually increase probability of maximising actions being selected
                for action_max in str_actions_max:
                    self.data[str_state][str(action_max)] += (1 - self.epsilon) / len(str_actions_max)

    def __getitem__(self, key):

        if type(key) is not tuple:
            state = key
            return self.data[str(state)]
        else:
            state, action = key
            return self.data[str(state)][str(action)]

    def __setitem__(self, key, value):

        if type(key) is not tuple:
            state = key
            self.data[str(state)] = value
        else:
            state, action = key
            self.data[str(state)][str(action)] = value

    def get_action(self, state):

        str_actions, probabilities = zip(*self[state].items())
        str_action = random.choices(population=str_actions, weights=probabilities)[0]

        for action in self.action_space:
            if str(action) == str_action:
                return action

    def __str__(self):
        return str(self.data)

# ---------------------------------------------------------------- #
