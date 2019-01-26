from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)

# Just a list to keep track of lootboxes and used lootboxes
lb_list = []

def read_lb_file():
    with open('lb_codes.txt', 'r') as f:
        for line in f:
            lb_list.append(line.strip())

@app.route('/')
def hello():
    return "hello world"

# Writing data to a backup file
def write_backup():
    return "TODO"

def check_lootbox(code):
    return "TODO"

scheduler = BackgroundScheduler()
scheduler.add_job(func=write_backup, trigger = "interval", seconds = 1200)
scheduler.start()

if __name__ == '__main__':
    read_lb_file():
    app.run()




"""
nimi
tiimi
equipped lista
"""