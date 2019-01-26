from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)

# Just a list to keep track of lootboxes and used lootboxes
lb_list = []
users_df =

def read_lb_file():
    with open('lb_codes.txt', 'r') as f:
        for line in f:
            lb_list.append(line.strip())

class titeenijaba:
    def __init__(self, name, team, equip_list):
        self.name = name
        self.team = team
        self.equip_list = equip_list

@app.route('/')
def hello():
    return "hello world"

# Write a backup to file, called every 20 minutes in scheduler
def write_backup():
    return "TODO"

def check_lootbox(code):
    return code in lb_list


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=write_backup, trigger = "interval", seconds = 1200)
    scheduler.start()
    read_lb_file()
    app.run()




"""
nimi
tiimi
equipped lista
"""