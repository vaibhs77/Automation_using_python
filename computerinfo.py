

import psutil
import platform
from os import *
import datetime


def CPU_INFO_OS ():
    print ( "ur now in computer" )
    print ( "vaibhav cpu info os_" )
    if platform.system () == "Windows":
        return platform.processor ()
    elif platform.system () == "darwin":
        command = '/usr/sbin/sysctl -n machdep.cpu.brand_string'
        return popen ( command ).read ().strip ()
    elif platform.system () == " Linux":
        command = 'cat/proc/cpuinfo'
        return popen ( command ).read ().strip ()
    return 'platform not identifide'


def get_size (bytes, suffix="B"):
    factor = 1024
    for unit in [ "K", "M", "G", "T", "P"]:
        if  bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def Boot_info ():
    print ( "________vaibhav sys boot time___________" )
    boot_time_timestamp = psutil.boot_time ()
    bt = datetime.fromtimestamp ( boot_time_timestamp )
    print ( f'boot time :{bt.year}/{bt.month}/{bt.month}/{bt.day}{bt.hour} :{bt.minute}:{bt.second}' )


def cpu_info ():
    print ( "______________vaibhav cpu info_______________" )
    print ( "Physical core :", psutil.cpu_count ( logical=False ) )
    print ( "Total core:", psutil.cpu_count ( logical=True ) )
    cpufreq = psutil.cpu_freq ()
    print ( f' Max Frequency: {cpufreq.max:.2f}Mhz' )
    print ( f' Min Frequency: {cpufreq.min :.2f}Mhz' )
    print ( f'Current Frequency: {cpufreq.current:.2f}Mhz' )

    print ( "cpu Usage per core:" )
    for i, percentage in enumerate ( psutil.cpu_percent ( percpu=True ) ):
        print ( f'core{i}:{percentage}%' )
    print ( f"total cpu usage :{psutil.cpu_percent ()}%" )


def RAM_Usage ():
    print ( "___________vaibhav memory information___________" )
    svmem = psutil.virtual_memory ()
    print ( f'Avaiable:{get_size ( svmem.available )}' )
    print ( f"used :{get_size ( svmem.used )}" )
    print ( f"percentage: {svmem.percent}%" )
    print ( "_____swap__________" )

    swap = psutil.swap_memory ()
    print ( f'Total:{get_size ( swap.total )}' )
    print ( f"free:{get_size ( swap.free )}" )
    print ( f'used:{get_size ( swap.used )}' )
    print ( f'percentage:{swap.percent}%' )


def disk_info ():
    print ( "___________Vaibhav disk information___________" )
    print ( "partinion and usage:" )

    partitions = psutil.disk_partitions ()
    for partition in partitions:
        print ( f"===Device :{partition.device}===" )
        print ( f" Mountpoint: {partition.mountpoint}" )
        print ( f'File system type: {partition.fstype} ' )
        try:
            partition_usage = psutil.disk_usage ( partition.mountpoint )
        except PermissionError:
            continue

    print ( f'ToTal size:{get_size ( partition_usage.Total )}' )
    print ( f'Used: {get_size ( partition_usage.used )}' )
    print ( f'free:{get_size ( partition_usage.free )}' )
    print ( f'percentage:{partition_usage.percent}' )
    disk_io = psutil.disk_io_counters ()
    print ( f' Total read:{get_size ( disk_io.read_bytes )}' )
    print ( f'total write:{get_size ( disk_io.write_bytes )}' )


def main ():
    CPU_INFO_OS ()
    get_size ( bytes, suffix="B" )
    Boot_info ()
    cpu_info ()
    RAM_Usage ()
    disk_info ()


if __name__ == "__main__":
    main ()
