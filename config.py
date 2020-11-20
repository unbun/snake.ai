from hp import *
from constants import *
from minimax import searchAgent, greedyEvaluationFunction, smartCowardDfunc, survivorDfunc

window_size       = 40
agent             = "RL" # will be added to opponents
# agent             = "ES"
filename          = "rl-pg-linear-r6-1000-test"
# filename          = "rl-ql-linear-r6-1000"
# filename          = "es-linear-r6-50"
game_hp           = HP(grid_size = window_size, max_iter = 3000, discount = 0.9)
rl_hp             = RlHp(rl_type = "policy_gradients", radius = 6, filter_actions = False, lambda_ = None, q_type = "linear")
# rl_hp             = RlHp(rl_type = "qlearning", radius = 6, filter_actions = False, lambda_ = None, q_type = "linear")
es_hp             = EsHp(radius = 6)
depth             = lambda s,a : survivorDfunc(s, a , 2, 0.5)
evalFn            = greedyEvaluationFunction
num_trials        = 1000
opponents         = [SmartGreedyAgent] #should see 2 players against each other
# opponents         = [SmartGreedyAgent, OpportunistAgent, searchAgent("alphabeta", depth, evalFn)]
comment           = ""
