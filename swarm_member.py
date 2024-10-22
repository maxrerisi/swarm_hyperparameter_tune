class SwarmMember():
    def __init__(self, swarmNumber) -> None:
        self.pos = None
        self.bestPos = self.pos
        self.bestScore = None
        self.scoreHistory = None
        self.swarmNumber = swarmNumber
