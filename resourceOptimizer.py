from subprocess import Popen, PIPE
import os


def extractResourceUsage(out):
	allContainer=out.split(" ");
	allContainer = filter(None, allContainer)
	if(len(allContainer)==14 and (allContainer[12]>"90.00%" or allContainer[12]<"10.00%")):
		memoryOptimizer(allContainer[0],allContainer[5],allContainer[12])
	return

def memoryOptimizer(id,totalMemory,memPerc):
	memoryUnit=totalMemory[-3:]
	tMem=totalMemory[:-3]
	factor=1
	if(memoryUnit=="GiB"):
		memoryUnit="g"
	if(memoryUnit=="MiB"):
		memoryUnit="mb"
	if(memPerc>"90.00%"):
		factor=2
	if(memPerc<"10.00%"):
		factor=0.5
	if(tMem.isdigit()):
		updateCommand="docker update "+id+" -m=\""+str(float(tMem)*factor)+memoryUnit+"\""
		os.system(updateCommand)
	return

def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line


if __name__ == "__main__":
    for path in run("docker stats --format \"table {{.Container}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.MemPerc}}\t{{.PIDs}}\""):
        extractResourceUsage(path)
        #print path




