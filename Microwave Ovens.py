class MicrowaveBase:
    def __init__(self):
        self.minute = 0
        self.second = 0

    def set_time(self,time):
        timelist = time.split(":")
        self.minute = int(timelist[0])
        self.second = int(timelist[1])
    
    def add_time(self, time):
        if "s" in time:
            self.second += int(time[:-1])
        elif "m" in time:
            self.minute += int(time[:-1])
        while self.second >= 60:
            self.second -= 60
            self.minute += 1
        if self.minute >= 90:
            self.minute = 90
            self.second = 0

    def del_time(self,time):
        if "s" in time:
            self.second -= int(time[:-1])
        elif "m" in time:
            self.minute -= int(time[:-1])
        while self.second < 0:
            self.second += 60
            self.minute -= 1
        if self.minute < 0:
            self.minute = 0
            self.second = 0
    
    def show_time(self):
        pass

class Microwave1(MicrowaveBase):
    def show_time(self):
        result = "{:0>2}:{:0>2}".format(self.minute,self.second)
        return "_"+result[1:]

class Microwave2(MicrowaveBase):
    def show_time(self):
        result = "{:0>2}:{:0>2}".format(self.minute,self.second)
        return result[:-1]+"_"

class Microwave3(MicrowaveBase):
    def show_time(self):
        return "{:0>2}:{:0>2}".format(self.minute,self.second)

class RemoteControl:
    def __init__(self,microwave):
        self.microwave = microwave
    
    def set_time(self,time):
        self.microwave.set_time(time)

    def add_time(self,time):
        self.microwave.add_time(time)

    def del_time(self,time):
        self.microwave.del_time(time)
    
    def show_time(self):
        return self.microwave.show_time()


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")
    
    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")
    
    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")