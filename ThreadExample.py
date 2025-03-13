# real life thread example
import threading
import time
import random

# Simulate downloading data from a website
def download_data(url):
    print(f"Downloading data from {url} ...")
    time.sleep(random.uniform(1,3))
    data = f"Data from {url}"
    print(f"Downloaded data from {url}")
    return data

#Simulate processing data
def process_data(data):
    print(f"Processing data {data}")
    time.sleep(random.uniform(1,2))
    processed_data= data.upper()
    print(f"Processed data {processed_data}")
    return processed_data

#Simulate data to database

def save_to_db(data):
    print(f"Saving data to db: {data}")
    time.sleep(random.uniform(1,2))
    print(f"Data saved to database: {data}")
    return data

# wrapper to handle process download, process and save

def handle_taks(url):
    data = download_data(url)
    processed_data = process_data(data)
    save_to_db(data)

# create multiple threads to handle different tasks concurrently
def main():

    urls = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]

    threads = []

# creates and start threads for each urls
    for url in urls:
        thread = threading.Thread(target=handle_taks(url))
        threads.append(thread)
        thread.start()

# wait for all threads to complete
    for thread in threads:
        thread.join()

print("All tasks completed")

if __name__== "__main__":
    main()
