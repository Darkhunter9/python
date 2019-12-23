import datetime
import re

class log(object):
    def __init__(self, log_text):
        temp = log_text.split(';;')
        time = [int(i) for i in temp[0].split('-')]
        self.time = datetime.datetime(*time)
        self.name = temp[1].lower()
        self.address = temp[2]
        return

class session(object):
    def __init__(self,log):
        self.logs = []
        self.add(log)

        self.name = log.name
        p1 = r'//.*?/'
        p2 = r'//.*'
        url = re.search(p1, log.address)
        if url:
            url = url.group(0)[2:-1]
        else:
            url = re.search(p2, log.address)
            url = url.group(0)[2:]
        self.address = url.split('.')[-2] + '.' + url.split('.')[-1]

        self.duration = 1
        self.quantity = 1

        self.MIN = self.logs[-1].time
        self.MAX = self.logs[-1].time
    
    def add(self,log):
        self.logs.append(log)
        self.update()

    def update(self):
        self.quantity = len(self.logs)
        self.MIN = min(self.logs, key=lambda x: x.time).time
        self.MAX = max(self.logs, key=lambda x: x.time).time
        self.duration = (self.MAX-self.MIN).total_seconds()+1
        self.logs.sort(key=lambda x: x.time)
    
    def judge(self,log):
        if log.name != self.name or self.address not in log.address:
            return False
        # elif self.address not in log.address:
        #     return False
        elif any(abs((log.time-i.time).total_seconds()) <= 1800 for i in self.logs):
            return True
        return False
    
    def output(self):
        return '{};;{};;{:.0f};;{}'.format(self.name, self.address, self.duration, self.quantity)
            

def checkio(log_text):
    log_list = []
    session_list = []
    result = []

    for i in log_text.split('\n'):
        log_list.append(log(i))
    
    for i in log_list:
        for j in session_list:
            if j.judge(i):
                j.add(i)
                break
        else:
            session_list.append(session(i))

    session_list.sort(key=lambda x: [x.name, x.address, x.duration, x.quantity])
    for i in session_list:
        result.append(i.output())
    return '\n'.join(result)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(
"""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
==
"""name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"