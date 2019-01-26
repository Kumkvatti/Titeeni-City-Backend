from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from titeenijaba import Titeenijaba
import atexit
import json


app = Flask(__name__)

# Just a list to keep track of lootboxes and used lootboxes
lb_list = []
users_list = [Titeenijaba("visa", "TiK", [1,2,3]), Titeenijaba("Hansen","TiK", [1,3,2])]

def read_lb_file():
    with open('lb_codes.txt', 'r') as f:
        for line in f:
            lb_list.append(line.strip())

@app.route('/')
def hello():
    return "hello world"

# Write a backup to file, called every 20 minutes in scheduler
def write_backup():
    with open('lb_codes.txt', 'w') as f:
        for x in lb_list:
            f.write(x + '\n')

    def obj_dict(obj):
        return obj.__dict__
    
    with open('user_info.json', 'w') as f:
        json.dump(users_list, f, default = obj_dict)
            

def check_lootbox(code):
    return code in lb_list

# TODO Fix this, only temporary teset function
def create_user(name):
    return "TODO"
    

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=write_backup, trigger = "interval", seconds = 3)
    scheduler.start()
    read_lb_file()
    app.run()




"""
nimi
tiimi
equipped lista
"""