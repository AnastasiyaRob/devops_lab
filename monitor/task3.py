import psutil
import time
import json
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Interval", type=int, default=30)
parser.add_argument("-t", help="Output file type", default="txt")
args = parser.parse_args()


class ResourcesMonitor:
    def __init__(self, snapshot, jsonform):
        self.jsonform = jsonform
        self.snapshot = snapshot

    def resources(self):
        cpu = psutil.cpu_percent()
        memory = list(map(str, str(psutil.virtual_memory()).split(",")))
        swap = list(map(str, str(psutil.swap_memory()).split(",")))
        list1 = ["Snapshot"+str(self.snapshot), "cpu", "memory", " swap"]
        list2 = [str(datetime.now()), cpu, memory[2], swap[3]]
        dict1 = {}
        for i in range(0, len(list1)):
            dict1[list1[i]] = list2[i]
        if self.jsonform is True:
            y = json.dumps(dict1, indent=3)
            with open("resources.json", 'a') as file:
                file.write(y)
        else:
             with open("resources.txt", 'a') as file:
                file.write("Snapshot" + str(self.snapshot) + " ") \
                      + file.write(str(datetime.now()) + " " + "cpu:" + str(cpu)) \
                      + file.write(" " + "memory:" + memory[2] + " ") \
                      + file.write("swap:" + swap[3] + "\n")


def main():
    jsonform = False
    snapshot = 0
    while True:
        snapshot += 1
        time.sleep(args.i)
        if args.t == "json":
            jsonform = True
        monitor = ResourcesMonitor(snapshot, jsonform)
        monitor.resources()


if __name__ == "__main__":
    main()
