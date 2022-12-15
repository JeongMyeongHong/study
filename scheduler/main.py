import time
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Seoul')

# n초마다 실행
interval_times = 3
interval_sleep = 7


def test(a, b, c):
    print(a)
    print(b)
    print(c)


def test_c(k):
    return k


def test_c_c(j):
    return j


@sched.scheduled_job('interval', seconds=interval_times, id='test_1')
def job1():
    a = 'a'
    b = 'b'
    c = 'c'
    test(test_c(test_c_c(c)), a, b)

    time.sleep(interval_sleep)


# 매일 12시 30분에 실행
@sched.scheduled_job('interval', seconds=interval_times * 2, id='test_2')
def job2():
    a = 'a2'
    b = 'b2'
    c = 'c2'
    test(test_c(c), a, b)
    time.sleep(interval_sleep)


print('sched before~')
sched.start()
print('sched after~')
