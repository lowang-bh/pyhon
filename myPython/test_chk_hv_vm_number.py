import sys, os
import unittest
import mock
sys.path.append("/opt/infinera/lib/Db")
sys.path.append("/opt/infinera/scripts")
from health_check import hv_check_vm_number 
from health_check import hv_check_dns
import health_check
import pexpect



class test_chk_vm_number(unittest.TestCase):
    def setUp(self):
        self.test_item = "HV VMs Number "
        
    def tearDown(self):
        pass
    
    @mock.patch('health_check.output_test_result')
    @mock.patch('Db.db_connections.get_name_path')
    def test_no_vms(self,mock_get_name_path,mock_output):
        #setup the environment
        mock_get_name_path.return_value = None
        ret = hv_check_vm_number()
        mock_output.assert_called_with(self.test_item,"PASSED!!")
        self.assertEqual(ret, True)
    
    @mock.patch('health_check.output_test_result')
    @mock.patch('Db.db_connections.get_vm_state')
    @mock.patch('Db.db_connections.get_name_path')
    def test_reasonal_vm(self,mock_get_name_path,mock_getvmstate,output):
        mock_get_name_path.return_value = ["OLM","OTM"]
        mock_getvmstate.side_effect = ["ON","OFF"]
        ret = hv_check_vm_number()
        output.assert_called_with('HV VMs Number ','PASSED!!')
        self.assertEqual(ret, True)
        #self.assertEqual(self.output(),"success\n")    
    '''
    @mock.patch('health_check.output_test_result')
    #@mock.patch('Db.db_connections.get_vm_state')
    #@mock.patch('Db.db_connections.get_name_path')
    def test_reasonal_vm_v1(self,output):
        #mock_getvmpath.return_value = ["OLM","OTM"]
        #mock_getvmstate.side_effect = ["ON","OFF"]
        ret = hv_check_vm_number()
        output.assert_called_with('HV VMs Number ','PASSED!!')
        self.assertEqual(ret, True)
        #self.assertEqual(self.output(),"success\n")
    '''
    @mock.patch('health_check.output_test_result')
    @mock.patch('Db.db_connections.get_vm_state')
    @mock.patch('Db.db_connections.get_name_path')
    def test_tomany_vms(self,mock_getvmpath,mock_getvmstate,output):
        vm_list = ["OLM" for i in range(100)]
        stat_list= ["ON" for i in range(100)]
        mock_getvmpath.return_value = vm_list
        mock_getvmstate.side_effect = stat_list
        ret = hv_check_vm_number()
        #self.assertEqual(result,'exceeds\n')
        output.assert_called_with('HV VMs Number ','FAILED!!')
        self.assertEqual(ret,False)
    
    @mock.patch('health_check.output_test_result')
    @mock.patch('Db.db_connections.get_vm_state')
    @mock.patch('Db.db_connections.get_name_path')
    def test_warning_vms(self,mock_getvmpath,mock_getvmstate,output):
        vm_list = ["OLM" for i in range(100)]
        stat_list = ["OFF" for i in range(100)]
        
        mock_getvmpath.return_value = vm_list
        mock_getvmstate.side_effect = stat_list
        ret = hv_check_vm_number()
        #self.assertEqual(result,'exceeds\n')
        output.assert_called_with('HV VMs Number ','WARNING!!')
        self.assertEqual(ret,True)
    
    @mock.patch('health_check.output_test_result')
    @mock.patch('Db.db_connections.get_vm_state')
    @mock.patch('Db.db_connections.get_name_path')
    def test_unexpected_vms(self,mock_getvmpath,mock_getvmstate,output):
        vm_list = ["OLM" for i in range(100)]
        
        mock_getvmpath.return_value = vm_list
        mock_getvmstate.return_value = None
        ret = hv_check_vm_number()
        #self.assertEqual(result,'exceeds\n')
        output.assert_called_with('HV VMs Number ','FAILED!!')
        self.assertEqual(ret,False)


if __name__ =="__main__":
    unittest.main()
