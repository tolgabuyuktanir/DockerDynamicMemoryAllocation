from subprocess import Popen, PIPE
import os


def extractResourceUsage(out):
	allContainer=out.split(" ");
	allContainer = filter(None, allContainer)
	if(len(allContainer)==14 and allContainer[12]>"50.00%"):
		memoryOptimizer(allContainer[0],allContainer[5])
	return

def memoryOptimizer(id,totalMemory):
	totalMemory=totalMemory[:-3]
	updateCommand="docker update "+id+" -m=\""+str(int(totalMemory)*2)+"mb\"";
	print(updateCommand)
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
    for path in run("docker stats --all --format \"table {{.Container}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}\t{{.MemPerc}}\t{{.PIDs}}\""):
        print path
        extractResourceUsage(path)




