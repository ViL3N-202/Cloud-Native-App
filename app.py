#modeling app to get cpu and mem metric
import psutil # get cpu and mem ons erver
from flask import Flask, render_template # for app
import socket, time

app = Flask(__name__)

@app.route("/") #home path

def index():
    
    # cpu_percent = psutil.cpu_percent()
    cpu_percent = psutil.cpu_percent(interval=4)
    mem_percent = psutil.virtual_memory().percent
    hostname = socket.gethostname()
    msg = None
    
    boot_time = psutil.boot_time()
    # Get the current time
    current_time = time.time()    

    uptime_seconds = current_time - boot_time

    # Convert uptime to days, hours, and minutes
    uptime_days, remainder = divmod(uptime_seconds, 86400)
    uptime_hours, remainder = divmod(remainder, 3600)
    uptime_minutes, _ = divmod(remainder, 60)
    
    uptime_list = [int(uptime_days), int(uptime_hours), int(uptime_minutes)]
    
    if cpu_percent > 80 or mem_percent > 80:
        msg = "High CPU or Memory Utilization detected."
    
    return render_template("index.html", cpu_metric =cpu_percent, mem_metric=mem_percent, message=msg, hostname=hostname, uptime=uptime_list )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    
    
#run local5000 with python3 app.py