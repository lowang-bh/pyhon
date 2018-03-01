path1=".;%JAVA_HOME%\bin;C:\ProgramData\Oracle\Java\javapath;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\OpenCL SDK\3.0\bin\x86;C:\Program Files (x86)\Intel\OpenCL SDK\3.0\bin\x64;C:\Program Files\Intel\WiFi\bin\;C:\Program Files\Common Files\Intel\WirelessCommon\;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Lenovo\Fingerprint Manager Pro\;C:\Program Files\Perforce;c:\Reviewboard;D:\Python27"

path2="c:\Reviewboard;C:\Python27\;C:\Python27\Scripts;C:\ProgramData\Oracle\Java\javapath;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;C:\windows\system32;C:\windows;C:\windows\System32\Wbem;C:\windows\System32\WindowsPowerShell\v1.0\;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Lenovo\Fingerprint Manager Pro\;C:\Program Files (x86)\Perforce;C:\Program Files\Perforce;C:\Program Files\mingw-w64\x86_64-5.2.0-win32-seh-rt_v4-rev0\mingw64\bin;C:\Program Files (x86)\IDM Computer Solutions\UltraEdit\\"
import re
list1 = re.split(r';',path1)
list2 = re.split(r';',path2)
a=[]
b=[]
for each in list1:
    if each in list2:
        print each
        b.append(each)
    else:
        a.append(each)
print "\n"
for each in a:
    print each
print "\n"
for each in [item for item in list2 if item not in b]:
    print each