from src.dao.getVAProjectMongoDB import getVAProjectMongoDB
from src.dao.getVAMongoDB import getVAMongoDB
from src.dao.getOESProjectMongoDB import getOESProjectMongoDB
from src.dao.getOESInterMongoDB import getOESInterMongoDB

class controllerIndex(object):

    def __init__(self):
        self.getVAProjectMongoDB = getVAProjectMongoDB
        self.getVAMongoDB = getVAMongoDB
        self.getOESProjectMongoDB = getOESProjectMongoDB
        self.getOESInterMongoDB = getOESInterMongoDB
    
