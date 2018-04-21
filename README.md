# DockerDynamicMemoryAllocation
If you get warning showed below: 

  WARNING: Your kernel does not support cgroup swap limit.
	
**Solution:**
```bash
  1-Edit the /etc/default/grub file. Add or edit the GRUB_CMDLINE_LINUX line as GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
	
  2- update grub with sudo update-grub
	
  3-Reboot	

```
