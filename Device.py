

def device_list(file) -> list:
    """Opens the file and returns the list of devices"""
    lis = []
    with open(file, "r") as data:
        for i in data:
            if "PROPAGATE" in i:
                lis.append(i.strip())
    return lis


def store_device(lis) -> dict:
    """Creates a dictionary out of the List of devices"""
    dic = {}
    for j in lis:
        data = j.split()
        if data[1] in dic.keys():
            dic[data[1]].append((data[2], data[3]))#If key already exits append to the value list
        else:
            dic[data[1]] = [(data[2], data[3])]#KEYS: Device ID, VALUES: tuple(Device id, propagation time)
    return dic

def alert_lis(file) -> list:
    """Opens and reads the file and returns the list of alerts"""
    lis = []
    with open(file, "r") as data:
        for i in data:
            if "ALERT" in i:
                lis.append(i.strip())
            elif "CANCEL" in i:
                lis.append(i.strip())
    return lis

def store_alert(lis) -> list:
    """Creates a custom data list out of the List of alerts"""
    priority_lis = []
    for i in lis:
        data = i.split()
        priority_lis.append((data[0], data[-1], data[1], data[2]))#alert type, time, source, message
    return priority_lis

def sorted_alert_lis(lis) -> list:
    """sorts the alert list according to the priority"""
    lis.sort(key=lambda x: len(x[-1])) #based on the size of the message
    lis.sort(key=lambda x: x[2]) #giving priority to device with smaller ID
    lis.sort(key=lambda x: x[0], reverse=True) #giving priority to cancellation over alert
    lis.sort(key=lambda x: int(x[1]))#sort based on time
    return lis

