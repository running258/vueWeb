from selenium import webdriver
from multiprocessing import Process
import os

class record():
    def setUP(self,runEnv):

        sys = runEnv["sys"]
        http = runEnv["http"]
        print(sys)
        print(http)
        a = os.system("mitmdump selenium.py")
        # print('Parent process %s.' % os.getpid())
        # p = Process(target=self.run_proc("sub"), args=('test',))
        # print('Child process will start.')
        # # p.start()
        # # p.join()
        # print('Child process end.')
    
    # def request(runEnv):

    #     flow.request.headers['User-Agent'] = 'MitmProxy'
    #     ctx.log.info(str(flow.request.headers))
    #     print(str(flow.request))

    def run_proc(self,name):
        os.system("mitmdump selenium.py")
        print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()

#     print('Child process end.')