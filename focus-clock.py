import time

def pomodoro_timer(work_duration, break_duration, rounds):
    for _ in range(round):
        print("Work session started. Stay focused!")
        time.sleep(work_duration * 60)  # 将分钟转换为秒
        print("Work session ended. Take a break!")
        time.sleep(break_duration * 60)  # 将分钟转换为秒
    print("All sessions completed. Great work!")

# 设置工作时间、休息时间和循环次数（可以根据需要进行调整）
work_time = 25
break_time = 5
rounds = 4

pomodoro_timer(work_time, break_time, rounds)
