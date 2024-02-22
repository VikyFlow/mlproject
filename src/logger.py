'''
    Ogni esecuzione che viene svolta, deve venire loggata ogni info che viene eseguita
    e cosi possiamo loggare se ci sono errori
    ogni eccezione che viene registrata, cercheremo di loggarla in un text file
    Come deve essere creato il mio LOGFILE?
'''
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path= os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)#even if there is a file , keep on appending the file inside that

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level= logging.INFO,
    
)   # whwerever i use logging.info, import login and login.info it will use the basic config we configurated
'''
    if __name__ == "__main__":
        logging.info("Logging has started")
'''