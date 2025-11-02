import platform, os, multiprocessing

def main():
    print("=== System Info ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Python: {platform.python_version()}")
    print(f"Processor: {platform.processor()}")
    try:
        print(f"CPU cores: {multiprocessing.cpu_count()}")
    except:
        pass
    print(f"Working dir: {os.getcwd()}")

if __name__ == "__main__":
    main()
