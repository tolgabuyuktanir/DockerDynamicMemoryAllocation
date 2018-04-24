# DockerDynamicMemoryAllocation

**randomNumberSort.py**
python randomNumberSort.py param1 param2 
	-param1 : repetation
	-param2 : number of random values
**resourceOptimizer.py**
python resourceOptimizer.py

This script gets status of running container. If the container is using memory more than %90, memory source is doubled. On the other hand, the container is using memory less than %10, half of the allocated memory resource is taken back in this script. It's repeated for each container.

**createMultipleContainer.sh**
./createMultipleContainer.sh

This is bash script which runs ten times randomNumberSort.py on docker.



If you get warning showed below: 

  WARNING: Your kernel does not support cgroup swap limit.
	
**Solution:**
```bash
  1-Edit the /etc/default/grub file. Add or edit the GRUB_CMDLINE_LINUX line as GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
	
  2- update grub with sudo update-grub
	
  3-Reboot	

```
