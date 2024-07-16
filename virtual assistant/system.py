import psutil
import speedtest
import GPUtil
from speech import SpeechSystem

class System:
    def __init__(self):
        self.ss = SpeechSystem()
        self.gpu = GPUtil.getGPUs()[0]
        self.cpu_usage_percent = psutil.cpu_percent(interval=5)
        self.memory_usage_percent = psutil.virtual_memory().percent
        self.download_speed = speedtest.Speedtest().download() / 8_000_000  # in MBps
        self.upload_speed = speedtest.Speedtest().upload() / 8_000_000  # in MBps
        
    def stats(self):
        self.ss.speak("Current system details are: ")
        self.ss.speak(f"CPU Usage: {self.cpu_usage_percent}%")
        self.ss.speak(f"Memory Usage: {self.memory_usage_percent}%")
        self.ss.speak(f"Download Speed: {self.download_speed:.2f} MBps")
        self.ss.speak(f"Upload Speed: {self.upload_speed:.2f} MBps")
        self.ss.speak(f"GPU Memory Usage: {self.gpu.memoryUtil * 100:.2f}%")
        self.ss.speak(f"GPU Temperature: {self.gpu.temperature:.2f} °C")

