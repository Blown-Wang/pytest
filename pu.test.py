import psutil

# print (psutil.cpu_times())
# print (psutil.cpu_times(percpu=True))
# print(psutil.cpu_times().user)

# print(psutil.virtual_memory())
# print (psutil.disk_partitions())
print(psutil.net_io_counters())
print(psutil.users())
print(psutil.pids())
