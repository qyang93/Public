####################################################################################################
#####            This code can extract the necessary data from 1-NH2.run and COF-bph.out       #####       
#####               to form a new output file (write for yyz)                                  #####
#####                                date: 20 of April 2021                                    #####
#####                      Written by Qun Yang (Qun.Yang@cpfs.mpg.de) in MPI-CPFS              #####
####################################################################################################

#!/Users/qyang/opt/miniconda3/envs/anaconda/bin/python
import re
import numpy

pattern_1 = re.compile(r'.*Atoms')
pattern_2 = re.compile(r'End')
pattern_3 = re.compile(r'.*Index Symbol')
line_num_Atoms = 0
line_num_End = 0
line_num_IndexSym = 0
with open("1-NH2.run","r") as frun, open("COF-bph.out","r") as fout:
    freadrun = frun.readlines()
    freadout = fout.readlines()
    for cnt, line in enumerate(freadrun):
        if re.match(pattern_1,line):
            line_num_Atoms=cnt+1
        elif re.match(pattern_2,line,0):    
            line_num_End = cnt+1
            break
    for cnt, line in enumerate(freadout):
        if re.match(pattern_3,line):
            line_num_IndexSym=cnt+1

    with open("output.txt","w") as fw:
        for line in freadrun[0:line_num_Atoms]:
            fw.write(str(line))
        for line in freadout[line_num_IndexSym:]:
            if re.match(r'\s*\n',line):
                break
            else:
                fw.write(str(re.sub(r'\s*\d*',' ',line, 1)))
        for line in freadrun[line_num_End-2:]:
            fw.write(str(line))
