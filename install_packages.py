import sys, os, subprocess

def execute_cmd(cmd):
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = result.communicate()[0]
    returncode = result.returncode
    return [returncode, out]


file1 = open('requirements.txt', 'r')
lines = file1.readlines()

file2 = open('/data/error.log', 'w')

for i in lines:
    output = execute_cmd(['pip', 'install', i])
    if output[0] == 0:
        file2.writelines(str(i)+'=========='+'SUCCESS==========\n')
        continue
    if output[0] != 0:
        #print(str(i))
        #print('-------------------------------\n')
        #print(str(output[1]))
        file2.writelines(str(i)+'=========='+'FAILED==========\n')
        # file2.writelines('-------------------------------\n')
        file2.writelines(str(output[1])+'\n')
        continue
file2.close()
