import threading
import time
import requests

def simulate_io_task(file_name, url):
    """Simulate downloading a file from a GitHub repository."""
    print(f"Starting download of {file_name} from {url}...")
    response = requests.get(url)  # Download the file
    if response.status_code == 200:
        # Save the content to a local file
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"Completed download of {file_name}!")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")

def run_io_tasks():
    """Run multiple I/O tasks concurrently using threads."""
    # List of files and their corresponding raw URLs on GitHub
    files = {
        "file_0.txt": "https://raw.githubusercontent.com/Julie-lou/ThreadingMultiprocessingAsyncio/refs/heads/main/file0.txt",
        "file_1.txt": "https://raw.githubusercontent.com/Julie-lou/ThreadingMultiprocessingAsyncio/refs/heads/main/file1.txt",
    }
    
    threads = []

    # Create and start a thread for each file
    for file_name, url in files.items():
        thread = threading.Thread(target=simulate_io_task, args=(file_name, url))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All downloads completed.")

# Run the I/O tasks
if __name__ == "__main__":
    run_io_tasks()
