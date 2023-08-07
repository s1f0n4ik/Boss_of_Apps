import psutil, datetime
import pygetwindow as pg
import getpass


def get_app_dict():
    app_dict = {}
    key = 1
    for prog in psutil.process_iter():
        t = datetime.datetime.fromtimestamp(prog.create_time())
        time = t.strftime("%Y-%m-%d %H:%M:%S")
        app_dict[key] = [prog.name(), prog.status(), time, prog.pid]
        key += 1
    return app_dict


def get_win_dict():
    win_dict = {}
    for window in pg.getAllTitles():
        if window != "":
            win_dict[window] = "running"
    return win_dict


def close_window(name):
    window = pg.getWindowsWithTitle(f"{name}")[0]
    print(window)
    window.close()


def close_all():
    win_dict = {}
    for window in pg.getAllTitles():
        print(window)
        if "Boss of Apps - Opera" == window or "Boss of Apps – app_script.py" == window:
            win_dict[window] = "running"
        else:
            close_window(window)
    return win_dict


def get_username():
    user_name = getpass.getuser()
    return user_name


def terminate_process(pid: int):
    proc = psutil.Process(pid)
    proc.terminate()
    proc.wait()


# print(get_app_dict())
# print(get_win_dict())
# get_username()
# close_window("0502_Орлов_Лаба№11.pdf - Adobe Acrobat Reader (64-bit)")
# close_all()
