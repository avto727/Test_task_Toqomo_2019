import logging
import sys

log = logging.getLogger()
log.level = logging.WARNING
log.addHandler(logging.StreamHandler(sys.stderr))
# create the logging file handler
fh = logging.FileHandler("Test_task_Toqomo_2019\\log.txt", encoding='utf-8')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add handler to logger object
log.addHandler(fh)