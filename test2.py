from threading import Thread
import characters,time

def func1():
    print('Working')

def func2(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("time out!")

if __name__ == '__main__':
    Thread(target = characters.game_timer(10)).start()
    Thread(target = func2(10)).start()