import os

os.system("python client/generate_keys.py")
os.system("python client/encrypt_data.py")
os.system("python cloud/server.py")
os.system("python client/search_client.py")
