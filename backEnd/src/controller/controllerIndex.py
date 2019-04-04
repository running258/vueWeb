from src.dao.getVAProjectMongoDB import getVAProjectMongoDB
from src.dao.getVAMongoDB import getVAMongoDB
from src.dao.getInterProjectMongoDB import getInterProjectMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB
from src.dao.getLoginEnvMongoDB import getLoginEnvMongoDB
from src.dao.getOESProjectMongoDB import getOESProjectMongoDB
from src.dao.getOESInterMongoDB import getOESInterMongoDB

class controllerIndex(object):

    def __init__(self):
        self.getVAProjectMongoDB = getVAProjectMongoDB
        self.getVAMongoDB = getVAMongoDB
        self.getInterProjectMongoDB = getInterProjectMongoDB
        self.getInterfacesMongoDB = getInterfacesMongoDB
        self.getLoginEnvMongoDB = getLoginEnvMongoDB
        self.getOESProjectMongoDB = getOESProjectMongoDB
        self.getOESInterMongoDB = getOESInterMongoDB
    
