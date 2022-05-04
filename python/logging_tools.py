import os
from timeTools import dateTimeNow, dateNow

class loggingTools:
    def __init__(self):
        self.log_dir = f"{os.getcwd()}/"
        log_name = f"server-{dateNow()}.log"
        log_path = f"{self.log_dir}{log_name}"
        with open(log_path, "w") as log:
            log.write(F"INFO:{dateTimeNow()}: log init\n")

    def info(self, data:str):
        log_name = f"server-{dateNow()}.log"
        log_path = f"{self.log_dir}{log_name}"
        with open(log_path, "a") as file:
            file.write(f"INFO:{dateTimeNow()}: {data}\n")

    def log_warning(self, data:str):
        log_name = f"server-{dateNow()}.log"
        log_path = f"{self.log_dir}{log_name}"
        with open(log_path, "a") as file:
            file.write(f"WARNING:{dateTimeNow()}: {data}\n")

    def debug(self, data:str):
        log_name = f"server-{dateNow()}.log"
        log_path = f"{self.log_dir}{log_name}"
        with open(log_path, "a") as file:
            file.write(f"DEBUG:{dateTimeNow()}: {data}\n")

    def error(self, data):
        log_name = f"server-{dateNow()}.log"
        log_path = f"{self.log_dir}{log_name}"
        with open(log_path, "a") as file:
            file.write(f"ERROR:{dateTimeNow()}: {str(data)}\n")
