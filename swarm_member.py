from random_params import get_random_params
from trainFunction import train_xgboost
from paramsToPos import paramsToPos, posToParams
from aToBLLength import move_towards
from parameter_file import RANDOM_MAGNITUDE, SELF_BEST_MAGNITUDE, SWARM_BEST_MAGNITUDE


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

    def move(self, swarm_best):
        curr_score = self.calculateScoreFromPos()
        self.scoreHistory.append({"id": self.swarmNumber,
                                  "score": curr_score, "params": self.getParamsFromPos()})
        if curr_score > self.bestScore:
            self.bestScore = curr_score
            self.bestPos = self.pos
        
        rand_vect   =   move_towards(self.pos, paramsToPos(get_random_params()), RANDOM_MAGNITUDE)
        self_best   =   move_towards(self.pos, self.bestPos, SELF_BEST_MAGNITUDE)
        swarm_best  =   move_towards(self.pos, swarm_best, SWARM_BEST_MAGNITUDE)

        temp_pos = list(a+b+c+d for a, b, c, d in zip(rand_vect,self_best,swarm_best, self.pos))
        for a in range(len(temp_pos)):
            if temp_pos[a] < 0:
                temp_pos[a] = 0
        
        self.pos = temp_pos
        


        


member = SwarmMember(1)
print(member.pos)
print(member.bestScore)
member.move(paramsToPos(get_random_params()))
print(member.pos)
