import logging

class LogGen:
    @staticmethod
    def LogGen():
        logging.basicConfig(filename=".\\logs\\automation.txt",
                            format='%(asctime)s: %(lavelname)s: %(message)s', datefmt='%m%d%y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger