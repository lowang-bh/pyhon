# create directory
import os
print os.getcwd()
CurPath = os.path.abspath('.')
print CurPath
JoinPath = os.path.join( CurPath, 'testdir')
print JoinPath
os.mkdir( JoinPath )