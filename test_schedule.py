import schedule
import time


def task_1():
    print("Running task 1")

def task_2():
    print("Running task 2")

def task_3():
    print("Running task 3")



schedule.every().day.at("09:00").do(task_1)


schedule.every().monday.at("10:30").do(task_2)


schedule.every(1).minutes.do(task_3)

def job():
    print("a")

schedule.every(3).seconds.do(job)

while True:

    schedule.run_pending()
    time.sleep(1)
