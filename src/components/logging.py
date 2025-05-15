import logging
import os
from datetime import datetime

LOG_LIFE=f"{datetime.now().strftime('%m_%d,%_Y,%_H,%_M,_%_S')}.log"
log_path=os.path.join(os.getcwd(),"log",LOG_LIFE)
os.makedirs(log_path, exist_ok=True)

LOG_LIFE_PATH=os.path.join(log_path, LOG_LIFE)

logging.basicConfig(
    filename=LOG_LIFE_PATH
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
