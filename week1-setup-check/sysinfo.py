import platform, os, multiprocessing

print("=== System Info ===")
print("OS:", platform.system(), platform.release())
print("Python:", platform.python_version())
print("CPU cores:", multiprocessing.cpu_count())
print("Working directory:", os.getcwd())
