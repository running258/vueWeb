from src.dao.getVAProjectMongoDB import getVAProjectMongoDB
from src.dao.getVAMongoDB import getVAMongoDB
from src.dao.getProjectsMongoDB import getProjectsMongoDB
from src.dao.getInterfacesMongoDB import getInterfacesMongoDB
from src.dao.getLoginEnvMongoDB import getLoginEnvMongoDB

class controllerIndex(object):

    def __init__(self):
        self.getVAProjectMongoDB = getVAProjectMongoDB
        self.getVAMongoDB = getVAMongoDB
        self.getProjectsMongoDB = getProjectsMongoDB
        self.getInterfacesMongoDB = getInterfacesMongoDB
        self.getLoginEnvMongoDB = getLoginEnvMongoDB
    
