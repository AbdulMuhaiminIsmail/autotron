import psutil
import speedtest
import GPUtil

def tellStats():
    # CPU usage
    cpu_usage_percent = psutil.cpu_percent(interval=5)
    print(f"CPU Usage: {cpu_usage_percent}%")

    # Memory usage
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / 1024 / 1024 / 1024:.2f} GBs")
    print(f"Available Memory: {memory.available / 1024 / 1024 / 1024:.2f} GBs")
    print(f"Memory Usage: {memory.percent}%")

    # WiFi speed (using speedtest-cli)
    st = speedtest.Speedtest()
    download_speed = st.download() / 8_000_000  # in MBps
    upload_speed = st.upload() / 8_000_000  # in MBps
    print(f"Download Speed: {download_speed:.2f} MBps")
    print(f"Upload Speed: {upload_speed:.2f} MBps")

    # GPU usage and temperature
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        print(f"GPU ID: {gpu.id}, Name: {gpu.name}")
        print(f"GPU Load: {gpu.load * 100:.2f}%")
        print(f"GPU Memory Used: {gpu.memoryUsed / 1024:.2f} GBs")
        print(f"GPU Memory Total: {gpu.memoryTotal / 1024:.2f} GBs")
        print(f"GPU Memory Usage: {gpu.memoryUtil * 100:.2f}%")
        print(f"GPU Temperature: {gpu.temperature:.2f} °C")

