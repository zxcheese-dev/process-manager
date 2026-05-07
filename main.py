import psutil

process_dict = {}

def script():
    listing_processes = []

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            name = proc.name()
            pid = proc.pid

            listing_processes.append(f"{name} | {pid}")

            if name not in process_dict:
                process_dict[name] = []
            process_dict[name].append(pid)

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
            try:
                kill(int(cmd[1]))
            except (ValueError):
                for task in process_dict[cmd[1]]:
                    kill(task)

        elif cmd[0] == "show":
            show(processes)
        
        else:
            print("No such command:", cmd[0])
