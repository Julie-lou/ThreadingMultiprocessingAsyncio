import threading
import time
import random

def simulate_io_task(file_name, duration):
    """Simulate an I/O-bound task by sleeping for a given duration."""
    print(f"Starting download of {file_name}...")
    time.sleep(duration)  # Simulate the time taken to download/process the file
    print(f"Completed download of {file_name}!")

def run_io_tasks():
    """Run multiple I/O tasks concurrently using threads."""
    # List of files to simulate downloading
    files = [f"file_{i}.txt" for i in range(5)]  # Example files: file_0.txt to file_4.txt
    threads = []

    # Create and start a thread for each file
    for file_name in files:
        duration = random.uniform(1, 3)  # Random duration between 1 and 3 seconds
        thread = threading.Thread(target=simulate_io_task, args=(file_name, duration))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All downloads completed.")

# Run the I/O tasks
if __name__ == "__main__":
    run_io_tasks()
