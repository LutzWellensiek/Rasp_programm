import serial
import time
import subprocess

# Öffne serielle Verbindung auf UART3 (GPIO4/5)
ser = serial.Serial('/dev/ttyAMA3', 9600, timeout=1)
def get_last_git_push_time():
    try:
        output = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%cd', '--date=iso', '--branches', '--remotes', '--grep=push'],
            cwd='.'
        )
        if not output:
            # Fallback: get last commit time
            output = subprocess.check_output(
                ['git', 'log', '-1', '--pretty=format:%cd', '--date=iso'],
                cwd='.'
            )
        return output.decode('utf-8')
    except Exception as e:
        return f"Fehler beim Abrufen der Git-Informationen: {e}"

print("Letzter Git-Push/Commit:", get_last_git_push_time())

# Dauerschleife
while True:
    message = 'Hallo vom Raspberry Pi!\n'
    print("Sende:", message.strip())
    ser.write(message.encode('utf-8'))
    ser.flush()
    time.sleep(5)
