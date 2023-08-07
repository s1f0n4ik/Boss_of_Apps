import getpass

import psutil
import pygetwindow as pg
import wmi


def close_window(name):
    window = pg.getWindowsWithTitle(f"{name}")[0]
    print(window)
    window.close()


def show_proceses():
    f = wmi.WMI()
    # Printing the header for the later columns
    print("pid   Process name")
    # Iterating through all the running processes
    for process in f.Win32_Process():
        # Displaying the P_ID and P_Name of the process
        print(f"{process.ProcessId:<10} {process.Name}")


def func_1():
    for p in psutil.process_iter(['name', 'username']):
        if p.info['username'] == getpass.getuser():
            print(p.pid, p.info['name'])
    a = [(p.pid, p.info['name']) for p in psutil.process_iter(['name', 'username'])
         if p.info['username'] == getpass.getuser()]
    print(a)

# print(psutil.users())
# print([
#      (p.pid, p.info)
#      for p in psutil.process_iter(['name', 'status'])
#      if p.info['status'] == psutil.STATUS_RUNNING
#     ])
