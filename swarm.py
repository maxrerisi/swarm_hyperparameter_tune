from swarm_member import SwarmMember
from paramsToPos import paramsToPos, posToParams
from random_params import get_random_params
import schedule
import time
from parameter_file import NUMBER_OF_ROUNDS, MEMBER_COUNT
from ascii_loading_bar import ascii_loading_bar
from trainFunction import train_xgboost
from aToBLLength import euclidean_distance

SWARM = []
SCORES = []
LOOP = NUMBER_OF_ROUNDS
start = time.time()

def check_jobs():
    schedule.run_pending()

def write_interim(iter, mem):
    with open("interim_text.txt", 'w') as fp:
        fp.write(f"{iter},{mem}")

def read_interim():
    with open("interim_text.txt", 'r') as fp:
        out = fp.read().split(',')
        return (int(out[0]), int(out[1]))


swarm_best_pos = paramsToPos(get_random_params())
swarm_best_score = train_xgboost(posToParams(swarm_best_pos))
best_info = ""
mean_move = 0
swarm_bests = [(swarm_best_pos, swarm_best_score, 0,0)]

def update_file():
        iter, mem = read_interim()
        with open("tracker.md", 'w') as fp:
            out = f"<h1> Info: </h1>Iteration: {iter+1} / {LOOP} {ascii_loading_bar(iter+1, LOOP)}<br> Member {mem} out of {MEMBER_COUNT} members. {ascii_loading_bar(mem, MEMBER_COUNT)}<br>Time: {time.time()-start:.2f} seconds"
            out += f"<h2> Best Score: </h2>{str(swarm_best_score)} {best_info}<br>Mean move: {mean_move:.2f} <h3>Move History</h3>"
            for dex, (a, b, c, d) in enumerate(swarm_bests):
                out += f"{dex}: {tuple(round(z) for z in a)} \t {b:.6f} \t {c:.6f} \t {d:.6f}<br>"
            out += "<br>"
            out += "<h2> Parameters:</h2>"
            out += "<p>"
            for a, b in posToParams(swarm_best_pos).items():
                out += str(a)
                out += f": {b}, "
                # out += "<br>"
            # out += "</p><h2> Scores:</h2>"
            # for scr in SCORES:
            #     out += f"{scr}<br>"

            fp.write(out)

schedule.every(5).seconds.do(update_file)



write_interim(-1,0)
for a in range(MEMBER_COUNT):
    with open("tracker.md", 'w') as fp:
        fp.write(f"Creating swarm: {a+1}/{MEMBER_COUNT}<br>{ascii_loading_bar(a+1, MEMBER_COUNT)}")
    member = SwarmMember(a)
    SWARM.append(member)


for iter in range(LOOP):
    write_interim(iter,0)
    check_jobs()
    movements = []
    for dex, member in enumerate(SWARM):
        member: SwarmMember = member
        movements.append(member.move(swarm_best_pos))
        scr = member.getLatestScore()["score"]
        if scr >= swarm_best_score:
            swarm_bests.append((member.getPos(), scr, euclidean_distance(swarm_best_pos, member.getPos()), euclidean_distance(member.getPos(), tuple(0 for _ in range(len(swarm_best_pos))))))
            swarm_best_score = scr
            swarm_best_pos = member.getPos()
            best_info = f"Achieved by: member {dex} in iteration {iter + 1}"
        SCORES.append(scr)
        if dex % 1 == 0:
            write_interim(iter,dex)
            check_jobs()
    mean_move = sum(movements)/len(movements)


