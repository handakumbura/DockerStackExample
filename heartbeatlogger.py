import os, time, yaml
from redis import Redis
import logging.config



def main():
    setup_logging()
    heartbeatlogger()

def heartbeatlogger():
    logger = logging.getLogger('Container Heart Beat')
    hostname=os.getenv('HOSTNAME')
    r=Redis(host='redis',port=6379)
    while True:
        beats=str(r.incr(hostname))
        logger.info(hostname+' beats. '+beats)
        time.sleep(30)

def setup_logging():
    with open('config.yaml', 'rt') as f:
        config = yaml.load(f)
        logging.config.dictConfig(config)



if __name__=='__main__':
    main()


