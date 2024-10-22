from get_random_params import get_random_params
from trainFunction import train_xgboost
from paramsToPos import paramsToPos, posToParams


class SwarmMember():
    def __init__(self, swarmNumber) -> None:
        self.pos = posToParams(get_random_params())
        self.bestPos = self.pos
        self.bestScore = self.calculateScoreFromPos()
        self.scoreHistory = []
        self.swarmNumber = swarmNumber

    def calculateScoreFromPos(self):
        self.bestScore = train_xgboost(posToParams(self.pos))

    def getParamsFromPos(self):
        return paramsToPos(self.pos)

    def move(self):
        curr_score = self.calculateScoreFromPos()
        self.scoreHistory.append[{"id": self.swarmNumber,
                                  "score": curr_score, "params": self.getParamsFromPos()}]


member = SwarmMember(1)
print(member.pos)
print(member.bestScore)
