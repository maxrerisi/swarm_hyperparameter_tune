from random_params import get_random_params
from trainFunction import train_xgboost
from paramsToPos import paramsToPos, posToParams
from aToBLLength import move_towards, euclidean_distance
from parameter_file import RANDOM_MAGNITUDE, SELF_BEST_MAGNITUDE, SWARM_BEST_MAGNITUDE, INT_PARAMS


class SwarmMember():
    def __init__(self, swarmNumber) -> None:
        self.pos = paramsToPos(get_random_params())
        self.bestPos = self.pos
        self.bestScore = self.calculateScoreFromPos()
        self.scoreHistory = []
        self.swarmNumber = swarmNumber

    def calculateScoreFromPos(self):
        return train_xgboost(posToParams(self.pos))

    def getParamsFromPos(self):
        return posToParams(self.pos)
    
    def getLatestScore(self):
        return self.latest_log
    
    def getPos(self):
        return self.pos

    def move(self, swarm_best):
        curr_score = self.calculateScoreFromPos()
        self.latest_log = {"id": self.swarmNumber,
                                  "score": curr_score, "params": self.getParamsFromPos()}
        self.scoreHistory.append(self.latest_log)
        if curr_score > self.bestScore:
            self.bestScore = curr_score
            self.bestPos = self.pos
        
        rand_vect   =   move_towards(self.pos, paramsToPos(get_random_params()), RANDOM_MAGNITUDE)
        # print("\033[34m")
        # print(self.bestPos)
        # print("\033[0m")

        self_best   =   move_towards(self.pos, self.bestPos, SELF_BEST_MAGNITUDE)
        swarm_best  =   move_towards(self.pos, swarm_best, SWARM_BEST_MAGNITUDE)

        temp_pos = list(a+b+c+d for a, b, c, d in zip(rand_vect,self_best,swarm_best, self.pos))
        for a in range(len(temp_pos)):
            if temp_pos[a] < 0:
                temp_pos[a] = 0

        temp_pos = posToParams(temp_pos)
        for param in temp_pos:
            if param in INT_PARAMS:
                temp_pos[param] = round(temp_pos[param])

        temp_pos = paramsToPos(temp_pos)
        self.old_pos = self.pos
        self.pos = temp_pos
        return euclidean_distance(self.pos, self.old_pos)
        

