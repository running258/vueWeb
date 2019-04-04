from src.dao.getCommonMongoDB import getCommonMongoDB

class getInterProjectMongoDB(getCommonMongoDB):

    def __init__(self):
        self.collection = getCommonMongoDB("interProject")
