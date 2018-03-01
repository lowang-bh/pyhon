#!/usr/bin/env python
import mock
import unittest
import sys
sys.path.append("/opt/infinera/lib/Utils")
sys.path.append("/opt/infinera/scripts")
from  Utils.get_server_config import  get_hv_version,get_cpu_width_from_sv



#the mock class will be mocked in each test function 
class mock_vm_access:
    def __call__(self, board=None, user="autotest", passwd="autotest",\
                logfile=None, prompt_msg=True, ip_addr=None,shell_prompt=None):
        return self
    def __init__(self, board=None, user="autotest", passwd="autotest",\
                logfile=None, prompt_msg=True, ip_addr=None,shell_prompt=None):  
        pass
    def __del__(self):
        pass
    #def set_logfile(self, file_name):
    #   pass   
    def send_cmd_v1(self, cmd, exp_prompt, outcome=None, error_conds=None, prompt_msg=False,time=-1):
        outcome['before']= cmd +" width: 64 bits"
        return True
    def send_line(self, cmd):
        print cmd
class mock_pexpect():
    def __init__(self):
        self.before='mock_pexpect'
        self.match=None
        self.after=None
    def sendline(self,cmd):   
        print cmd
    def expect(self,prompt,timeout=-1):
        print prompt 
        self.before='5.5.1'    


class test_get_server_config(unittest.TestCase):
    def setUp(self):
        self.patch_va_access=mock.patch('Utils.get_server_config.vm_access.vm_access',new_callable=mock_vm_access)
        self.patch_log=mock.patch('Utils.get_server_config.log.info',new=self._log)
        self.mockva=self.patch_va_access.start()
        self.mocklog=self.patch_log.start()

    def tearDown(self):
        self.patch_va_access.stop()
        self.patch_log.stop()
        
    def _log(self,msg):
        print "my own log:",
        print msg   
    '''    
    def _send_cmd_v1(self, cmd, exp_prompt, outcome=None, error_conds=None, prompt_msg=False,time=-1):
        print cmd
        outcome['before']='width: 64 bits'
        return True
    '''

    def test_get_cpu_width_from_sv(self):
        sv_ip='10.220.36.161'
        ret=get_cpu_width_from_sv(sv_ip)
        self.assertEqual(ret, "64")
        
    @mock.patch('Utils.get_server_config.connect_ssh')
    def test_get_hv_version(self,mock_ssh):
        ip='127.0.0.1'
        mock_ssh.return_value=None
        get_hv_version(ip)
        mock_ssh.return_value=mock_pexpect()
        get_hv_version(ip)
        
        
        
if  __name__=="__main__":
    unittest.main()        
        
        
        
        
        