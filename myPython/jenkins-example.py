#!/usr/bin/env python

from optparse import OptionParser

import jenkins


def get_jenkins_version(username, password, url="http://localhost:8080"):
    server = jenkins.Jenkins(url, username=username, password=password)
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    return version


def work_with_jenkins_job():
    server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
    jobs = server.get_jobs()
    print jobs
    my_job = server.get_job_config('empty')
    print(my_job)  # prints XML configuration
    server.build_job('empty')
    server.disable_job('empty')
    server.copy_job('empty', 'empty_copy')
    server.enable_job('empty_copy')
    server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)

    server.delete_job('empty')
    server.delete_job('empty_copy')


def build_jenkins_job():
    server.create_job('api-test', jenkins.EMPTY_CONFIG_XML)
    # build a parameterized job
    # requires creating and configuring the api-test job to accept 'param1' & 'param2'
    server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
    last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
    build_info = server.get_build_info('api-test', last_build_number)
    print build_info


def work_with_jenkins_view():
    server.create_view('EMPTY', jenkins.EMPTY_VIEW_CONFIG_XML)
    view_config = server.get_view_config('EMPTY')
    views = server.get_views()
    print views

    # get all jobs from the specific view
    jobs = server.get_jobs(view_name='EMPTY')
    print jobs

    server.delete_view('EMPTY')


def get_job_config(job_name):
    job = server.get_job_name(job_name)
    print("job:", job)
    config = server.get_job_config(job_name)
    print(config)


if __name__ == "__main__":
    parser = OptionParser(usage="jenkins example")
    
    parser.add_option("--host", dest="host", help="IP for host server")
    parser.add_option("-u", "--user", dest="user", help="User name for host server")
    parser.add_option("-p", "--pwd", dest="passwd", help="Passward for host server")

    (options, args) = parser.parse_args()
    server = jenkins.Jenkins(options.host, options.user, options.passwd)
    jobs = server.get_all_jobs()
    for job in jobs:
        print job

    # work_with_jenkins_job()
    # print server.get_nodes(depth=1)
    # print server.get_job_info(name="test")
    # work_with_jenkins_view()

    # plugins = server.get_plugins()
    # get_job_config("gohello-master")
