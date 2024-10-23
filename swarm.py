from swarm_member import SwarmMember
from paramsToPos import paramsToPos, posToParams
from random_params import get_random_params

MEMBER_COUNT = 10
SWARM = []
SCORES = []
LOOP = 50


def update_file(iter,mem):
        with open("tracker.md", 'w') as fp:
            out = f"<h1> Info: </h1>Iteration: {iter+1} / {LOOP}<br> Member {mem} out of {MEMBER_COUNT} members."
            out += f"<h2> Best Score: </h2>{str(swarm_best_score)} {best_info}<br>Mean move: {mean_move:.2f}"
            out += "<br>"
            out += "<h2> Parameters:</h2>"
            out += "<p>"
            for a, b in posToParams(swarm_best_pos).items():
                out += str(a)
                out += f": {b}, "
                # out += "<br>"
            out += "</p><h2> Scores:</h2>"
            for scr in SCORES:
                out += f"{scr}<br>"

            fp.write(out)

swarm_best_pos = paramsToPos(get_random_params())
swarm_best_score = -1
best_info = ""
mean_move = 0
update_file(-1,0)
for a in range(MEMBER_COUNT):
    with open("tracker.md", 'w') as fp:
        fp.write(f"Creating swarm: {a+1}/{MEMBER_COUNT}")
    member = SwarmMember(a)
    SWARM.append(member)





for iter in range(LOOP):
    update_file(iter,0)
    movements = []
    for dex, member in enumerate(SWARM):
        member: SwarmMember = member
        movements.append(member.move(swarm_best_pos))
        scr = member.getLatestScore()["score"]
        if scr > swarm_best_score:
            swarm_best_score = scr
            swarm_best_pos = member.getPos()
            best_info = f"Achieved by: member {dex} in iteration {iter + 1}"
        SCORES.append(scr)
        if dex % 1 == 0:
            update_file(iter,dex)
    mean_move = sum(movements)/len(movements)

# TODO use schedule library to update it every 5 seconds
# TODO bootstrap dataset