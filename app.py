import subprocess
import platform
import time
from datetime import datetime

log_file_path = "internet_access_log.txt"
prev_state = None

def check_internet():
    global prev_state
    
    target_ip = "8.8.8.8"

    # Use 'n' on Windows and 'c' on Unix-like systems
    option = '-n' if platform.system().lower() == 'windows' else '-c'
    
    result = subprocess.run(['ping', option, '3', target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    is_connected = result.returncode == 0

    if is_connected != prev_state:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"[{datetime.now()}] Internet {'connected' if is_connected else 'disconnected'}\n")
        prev_state = is_connected


check_interval = 3

with open(log_file_path, "w") as log_file:
    log_file.write('Log started\n')
while True:
    check_internet()
    time.sleep(check_interval)
