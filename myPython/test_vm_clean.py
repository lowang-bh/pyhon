#!/usr/bin/env python

import sys,os
import unittest
import mock
sys.path.append("/opt/infinera/lib/Db")
sys.path.append("/opt/infinera/lib/Utils")
sys.path.append("/opt/infinera/scripts")
from Utils.vm_clean import clean_file,vm_clean_tar_file,vm_list_files,vm_clean_other_file,clean_file_in_allbds
from Utils.vm_clean import *
TestValueIp=[('IAM 3-A-1','127.11.3.71'),('MCM 1-A-7A','127.11.1.122'),('IMM 4-A-16','127.11.4.86')]
Iplist     =['127.11.3.71',None,'127.11.4.86','127.1.1.1','127.1.1.2']

def isControlMod(name):
    print "In mock is control model"
    if name in TestValueIp[0]:
        return False
    else:
        return True
def mock_clean_tar(va,board,FileType='.tar'):
    print "mock clean tar file"
    return True
def mock_clean_other(va,board,FileType=None):
    print "mock in clean other"
    return True

'''    
def my_sendCmd(cmd,prompt,outcome):
    outcome['berfore']="Now you are in Mock_sendCmd"
'''
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
        outcome['before']= cmd+"\r\n"+cmd +"\r\n"+cmd
        if '/wang' in cmd:
            outcome['before']+= "\r\n" + "No such file or directory"
        return True
    def send_line(self, cmd):
        print cmd
        
class mock_IDB():
    def __init__(self):
        print "in mock IDB"
        pass
    def execute(self, cmd, attempt=1):
        print cmd
        return [(2,),(3,)]
    def close(self):
        pass
'''mock class will be mocked in each test function'''
class my_hv_access:
    def __call__(self):
        return self
    def __init__(self):
        pass
        
    def is_vm_on(self,board):

        if board in TestValueIp[0]:
            print "%s is not on" %board
            return False
        else:
            print "%s is on"%board
            return True
            

class test_vm_clean(unittest.TestCase):
    def setUp(self):
        self.patch_hv_access=mock.patch('Utils.vm_clean.hv_access',new_callable=my_hv_access)
        self.patch_va_access=mock.patch('Utils.vm_clean.vm_access.vm_access',new_callable=mock_vm_access)
        self.patch_log=mock.patch('Utils.vm_clean.log.info',new=self._log)
        self.mockhv=self.patch_hv_access.start()
        self.mockva=self.patch_va_access.start()
        self.mocklog=self.patch_log.start()
        self.count=0
    def tearDown(self):
        self.patch_hv_access.stop()
        self.patch_va_access.stop()
        self.patch_log.stop()
    def _getall(self):
        print "in self _getall"
        return [board[0] for board in TestValueIp]
    def _log(self,msg):
        print "my own log:",
        print msg
    def _send_cmd(self,cmd,prompt,outcome=None,error_conds=None,prompt_msg=False,time=-1):
        print "in my send cmd "+cmd+prompt
        outcome['before']='M15.4.0.0362' # +'\n' +'M15.4.0.0999.x86.tar.gz'
        #for x in cmd.split():
        #    print x
        if 'ls' in cmd.split():
            outcome['before']='M15.4.0.0362.x86.tar.gz'
        self.count +=1
        if self.count==1:
            return True
        elif self.count == 2:
            return False
        else:
            return None
    #@mock.patch('Comms.hv_access.hv_access')
    #@mock.patch('Comms.hv_access.hv_access.is_vm_on')
    #@mock.patch('Comms.vm_access.vm_access')
    @mock.patch('Utils.vm_clean.vm_clean_tar_file')
    @mock.patch('Utils.vm_clean.vm_clean_other_file')
    def test_clean_file(self,mock_vm_clean_other_file,mock_vm_clean_tar_file):#,mock_vm_access,mock_is_vm_on,my_hv_access):
        print "test clean file"

        self.mockhv.return_value=my_hv_access()
        self.mockva.return_value=mock_vm_access()
        #mock_is_vm_on.side_affect = isVmOn #[False,False,True]
        mock_vm_clean_other_file.side_effect = mock_clean_other
        mock_vm_clean_tar_file.side_effect = mock_clean_tar
        args=['.tar','.core','.log']
        #boards=[board[0] for board in TestValueIp]
        '''if boards use list here, assert can'n pass'''
        boards=['MCM 1-A-7A']
        clean_file(boards, args)
        mock_vm_clean_other_file.assert_any_call(self.mockva,boards[0],'.core')
        mock_vm_clean_other_file.assert_any_call(self.mockva,boards[0],'.log')
        mock_vm_clean_tar_file.assert_any_call(self.mockva,boards[0])
        
        boards=['IAM 3-A-1']
        clean_file(boards, args)
        
        boards=['IMM 4-A-16']
        clean_file(boards, args)
        mock_vm_clean_other_file.assert_any_call(self.mockva,boards[0],'.core')
        mock_vm_clean_other_file.assert_any_call(self.mockva,boards[0],'.log')
        mock_vm_clean_tar_file.assert_any_call(self.mockva,boards[0])
        
        args=[]
        clean_file(boards, args)          
        
    def test_clean_file_in_dir(self):
        ret=clean_file_in_dir(TestValueIp[0][0],None)
        self.assertEqual(ret, False)
        for board in TestValueIp:
            ret=clean_file_in_dir(board[0],'/')
            if board[0] in TestValueIp[0]:
                self.assertEqual(ret, False)
            else:
                self.assertEqual(ret, True)           

    @mock.patch('Utils.vm_clean.get_cm_tar_ver')    
    @mock.patch('Utils.vm_clean.get_current_RlsVer')    
    #@mock.patch('Comms.vm_access.vm_access')   
    @mock.patch('Db.db_connections.get_vm_ip')
    @mock.patch("Utils.vm_name.isControlModule")
    def test_vm_clean_tar_file(self,mock_isControlMod,mock_get_ip,mock_get_curVer,mock_get_tarVer):
        print "test vm clean tar file" 
        self.mockva.return_value=mock_vm_access()
        mock_isControlMod.side_effect=isControlMod
        mock_get_ip.side_effect=Iplist
        mock_get_curVer.return_value=['M15.4.0.0362']
        mock_get_tarVer.side_effect=[['M15.4.0.0369','M15.4.0.0362'],['M15.4.0.9999','M15.4.0.8888']]
        for boards in TestValueIp:
            va=mock_vm_access(boards[0])            
            vm_clean_tar_file(va, boards[0])
        mock_get_ip.assert_content_equal=['127.11.3.71',None]
        mock_isControlMod.assert_content_equal=[False,True,True]
    
  
    @mock.patch('vm_clean.db.get_vm_ip')
    def test_vm_clean_other_file(self,mock_get_ip):
        print "test vm clean other file"
        self.mockva.return_value=mock_vm_access()
        mock_get_ip.side_effect=Iplist
        for boards in TestValueIp:
            va=mock_vm_access(board=boards[0])   
            vm_clean_other_file(va, boards[0],'.log') 
            mock_get_ip.assert_any_call(boards[0])
        mock_get_ip.assert_content_equal=Iplist
        assert isinstance(va,mock_vm_access)
    
    @mock.patch('Utils.vm_clean.db.get_vm_ip')
    def test_vm_list_files(self,mock_get_ip):
        print "test vm list files"
        self.mockva.return_value=mock_vm_access()
        self.mockhv.return_value=my_hv_access()
        mock_get_ip.side_effect=Iplist
        vm_list_files(TestValueIp[0][0])
        for boards in TestValueIp: 
            vm_list_files(boards[0],path='/',size=100,outdic={})
            mock_get_ip.assert_any_call(boards[0])
        mock_get_ip.assert_content_equal=['127.11.3.71',None,'127.11.4.86']
        vm_list_files(boards[0],path='/',size=100,outdic=[])
        vm_list_files(boards[0],path='/wang',size=100,outdic={})
            
    @mock.patch('Utils.vm_clean.clean_file')    
    @mock.patch('Utils.vm_clean.get_all_boards')
    def test_clean_file_in_allbds(self,mock_getall,mock_clean_file):
        print "test_clean_file_in_allbds"
        mock_getall.return_value=self._getall()
        clean_file_in_allbds(['.tar'])
        mock_clean_file.assert_called_with([board[0] for board in TestValueIp],['.tar'])
    
    @mock.patch('Utils.vm_clean.clean_file')  
    @mock.patch('Utils.vm_clean.db.get_vm_for_chassis')
    @mock.patch('Utils.vm_clean.db.get_chassis_for_ne')
    @mock.patch('Utils.vm_clean.is_neID_exist')
    def test_clean_file_by_ne(self,mock_is_neID_exist,mock_get_chassis,mock_get_vm,mock_clean_file):
        mock_is_neID_exist.side_effect=[True,False]
        mock_get_chassis.return_value=[(1,) ]
        mock_get_vm.return_value=[(2, u'MCM 1-A-7A'), (3, u'BMM 1-A-1')]

        clean_file_by_ne(1,['.tar'])
        clean_file_by_ne(2,['.log'])#mock_is_neID_exist reruen None
        mock_clean_file.assert_called_with(['MCM 1-A-7A','BMM 1-A-1'],['.tar'])

        
    @mock.patch('Utils.vm_clean.clean_file')  
    @mock.patch('Utils.vm_clean.db.get_vm_for_chassis')
    @mock.patch('Utils.vm_clean.is_chassisId_exist')
    def test_clean_file_by_chassis(self,mock_is_chassisId_exist,mock_get_vm,mock_clean_file):
        mock_is_chassisId_exist.side_effect=[True,False]
        mock_get_vm.return_value=[(2, u'MCM 1-A-7A'), (3, u'BMM 1-A-1')]

        clean_file_by_chassis(1,['.tar'])
        clean_file_by_chassis(2,['.log'])#mock_is_chassisId_exist reruen None
        mock_clean_file.assert_called_with(['MCM 1-A-7A','BMM 1-A-1'],['.tar'])
       
    @mock.patch('Utils.vm_clean.clean_file')    
    @mock.patch('Utils.vm_clean.get_all_boards') 
    def test_clean_file_by_board(self,mock_getall,mock_clean_file):
        mock_getall.return_value=self._getall()
        clean_file_by_board('MCM 1-A-7A',['.tar'])
        mock_clean_file.assert_called_with(['MCM 1-A-7A'],['.tar'])
        clean_file_by_board('vswitch',['.tar'])
        clean_file_by_board('noBoard',['.tar'])
        
    @mock.patch('Utils.vm_clean.db.get_vm_for_chassis')
    @mock.patch('Utils.vm_clean.db.get_chassis_for_ne')
    @mock.patch('Utils.vm_clean.db.get_neList')
    def test_get_all_boards(self,mock_getnelist,mock_get_chassis,mock_get_vm):
        mock_getnelist.return_value=[(1,)]
        mock_get_chassis.return_value=[(1,) ]
        mock_get_vm.return_value=[(2, u'MCM 1-A-7A'), (3, u'BMM 1-A-1')]
        ret = get_all_boards()
        self.assertEqual(ret,['MCM 1-A-7A','BMM 1-A-1'])
        
    @mock.patch('__main__.mock_IDB.execute')    
    @mock.patch('Utils.vm_clean.db.IDB')
    def test_is_neID_exist(self,mock_db,mock_db_exec):
        mock_db.return_value=mock_IDB()
        mock_db_exec.side_effect=[[(2,)],[(3,)],None]
        self.assertEqual(is_neID_exist(2), True) 
        self.assertEqual(is_neID_exist(2), False) 
        self.assertEqual(is_neID_exist(2), False) 

    @mock.patch('__main__.mock_IDB.execute')    
    @mock.patch('Utils.vm_clean.db.IDB')    
    def test_is_chassisId_exist(self,mock_db,mock_exe):
        mock_db.return_value=mock_IDB()
        mock_exe.side_effect=[[(2,)],[(3,)],None] #This will mock mock_IDB.execute method
        self.assertEqual(is_chassisId_exist(2), True) 
        self.assertEqual(is_chassisId_exist(2), False) 
        self.assertEqual(is_chassisId_exist(2), False) 
    @mock.patch('__main__.mock_vm_access.send_cmd_v1')    
    def test_get_current_RlsVer(self,mock_send_cmd):
        mock_send_cmd.side_effect=self._send_cmd
        va=mock_vm_access()
        retlist=get_current_RlsVer(va)
        self.assertEqual(retlist,['M15.4.0.0362'])
        retlist=get_current_RlsVer(va)
        self.assertEqual(retlist,[])


    @mock.patch('__main__.mock_vm_access.send_cmd_v1')
    def test_get_cm_tar_ver(self,mock_send_cmd):
        mock_send_cmd.side_effect=self._send_cmd
        va=mock_vm_access()
        retlist=get_cm_tar_ver(va)
        self.assertEqual(retlist,['M15.4.0.0362'])
        retlist=get_cm_tar_ver(va)
        self.assertEqual(retlist,[])
    '''
    @mock.patch('Utils.vm_name.isControlModule')
    @mock.patch('Db.db_connections.get_vmList')
    def test_get_vms_and_cms(self,mock_get_vmList,mock_isControlMod):
        mock_get_vmList.return_value = TestValueIp
        mock_isControlMod.side_effect=isControlMod
        ret = get_vms_and_cms()
        self.assertEqual(ret, [['127.11.1.122','127.11.4.86'],['127.11.1.122','127.11.4.86']])
    '''
        
if __name__ =="__main__":
    unittest.main()
        
