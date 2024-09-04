from pathlib import Path
from Device import *

def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())
def check_file(file) -> bool:
    """Checks if the file exists. Returns True if exist else returns False"""
    return file.is_file()





def main() -> None:
    """Runs the simulation program in its entirety"""
    input_file_path = _read_input_file_path()
    if check_file(input_file_path):
        data = device_list(input_file_path)
        device_dic = store_device(data)
        sorted_alerts = (sorted_alert_lis(store_alert(alert_lis(input_file_path))))
        blc_lis = []
        blc_lis2 = []
        while sorted_alerts:
            cmd = sorted_alerts[0]

            if (len(blc_lis) >= 1) and cmd[0] == "ALERT" and blc_lis[0][-1] == cmd[-1] and blc_lis[0][-2] == cmd[-2]:
                blc_lis.remove(blc_lis[0])
                sorted_alerts.pop(0)

            elif (len(blc_lis2) >= 1) and (cmd[0] == "CANCELLATION" or cmd[0] == "CANCEL") and blc_lis2[0][-1] == cmd[-1] and blc_lis2[0][-2] == cmd[-2]:
                blc_lis2.remove(blc_lis2[0])
                sorted_alerts.pop(0)


            elif cmd[0] == "ALERT":
                if cmd[2] not in device_dic.keys():
                    sorted_alerts.pop(0)
                else:
                    for i in device_dic[cmd[2]]:
                        time2 = int(cmd[1])
                        print(f'@{time2} #{cmd[2]} SENT {cmd[0]} TO #{i[0]}: {cmd[-1]}')
                        time2 += int(i[-1])
                        sorted_alerts.append(("RECEIVED", time2, cmd[2], "ALERT", i[0], cmd[-1]))
                        sorted_alerts.append(("ALERT", time2, i[0], cmd[-1]))
                    sorted_alerts.pop(0)


            elif cmd[0] == "CANCEL" or cmd[0] == "CANCELLATION":
                if cmd[2] not in device_dic.keys():
                    sorted_alerts.pop(0)
                else:
                    for i in device_dic[cmd[2]]:
                        time2 = int(cmd[1])
                        print(f'@{time2} #{cmd[2]} SENT CANCELLATION TO #{i[0]}: {cmd[-1]}')
                        time2 += int(i[-1])
                        sorted_alerts.append(("RECEIVED", time2, cmd[2], "CANCELLATION", i[0], cmd[-1]))
                        sorted_alerts.append(("CANCELLATION", time2, i[0], cmd[-1]))
                    sorted_alerts.pop(0)



            elif cmd[0] == "RECEIVED":
                time2 = int(cmd[1])
                print(f'@{time2} #{cmd[-2]} {cmd[0]} {cmd[3]} FROM #{cmd[2]}: {cmd[-1]}')
                sorted_alerts.pop(0)


            if cmd[0] == "CANCEL":
                if cmd not in blc_lis:
                    blc_lis.append(cmd)
                if cmd not in blc_lis2:
                    blc_lis2.append(cmd)

            sorted_alert_lis(sorted_alerts)

    else:
        print("FILE NOT FOUND")


if __name__ == '__main__':
    main() #Cant be tested, This is running the actual program, which cant really be tested.
