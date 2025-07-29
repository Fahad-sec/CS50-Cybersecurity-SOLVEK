import string 
import time 
import itertools 
from tqdm import tqdm 

target_password = "4a3$"


charset = string.ascii_letters + string.digits + string.punctuation

start_time = time.time()

found = False  

for password_length in range(1, 6): 
    for attempt in tqdm(itertools.product(charset, repeat=password_length), desc=f"Trying length {password_length}"):
        attempt_password = ''.join(attempt)
        if attempt_password == target_password:
            end_time = time.time()
            print(f"Password cracked: {attempt_password}")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            found = True 
            break
 
    if found:
        break
