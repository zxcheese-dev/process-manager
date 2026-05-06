import psutil

def script():
    listing_processes = []
    processes = set()

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            name = proc.name()
            pid = proc.pid

            if name not in processes:
                processes.add(name)
                listing_processes.append(f"{name} | {pid}")
        except(psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    listing_processes.sort()
    return listing_processes

def show(processes):
    for names in processes:
        print(names)

def kill(pid):
    try:
        psutil.Process(pid).kill()
        print("KILLED")

    except (psutil.NoSuchProcess):
        print("No such process")
    except (psutil.AccessDenied):
        print("Accept denied")

if __name__ == "__main__":
    while True:
        processes = script()

        cmd = input("\nCommand: ").split(" ")

        if cmd[0] == "stop":
            kill(int(cmd[1]))

        elif cmd[0] == "show":
            show(processes)
        
        else:
            print("No such command:", cmd[0])
