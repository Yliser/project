import psutil


def get_cpu_usage(interval_in_seconds: int) -> float:
    """ measure local CPU """
    current_cpu_measure = psutil.cpu_percent(interval=interval_in_seconds)
    #print(f"current_cpu_measure:{current_cpu_measure}")
    return current_cpu_measure



continue_get_cpu = True
while(continue_get_cpu):
    if get_cpu_usage(1) > 75:
        print(f"your CPU crossed the 75%, please kill processes")