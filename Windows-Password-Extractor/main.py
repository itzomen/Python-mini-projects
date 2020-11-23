import subprocess

cmd = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [wifi.split(':')[1][1:-1] for wifi in cmd if "All User Profile" in wifi]
file = open(r'file.txt', 'w')
print('Extracting...')
for wifi in wifis:
    outputs = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    password = [output.split(':')[1][1:-1] for output in outputs if "Key Content" in output]
    try:
        file.write(f'WIFI: {wifi} Password: {password[0]} \n')
    except IndexError:
        file.write(f'WIFI: {wifi} Password: Not Found \n')
print('Done')