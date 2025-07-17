import json
import subprocess

def get_os_info():
    try:
        command = [
            "pwsh", "-Command",
            "@{OSName=(Get-CimInstance Win32_OperatingSystem).Caption; OSVersion=(Get-CimInstance Win32_OperatingSystem).Version; OsArchitecture=(Get-CimInstance Win32_OperatingSystem).OSArchitecture} | ConvertTo-Json"
        ]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            return json.loads(result.stdout)
        else:
            return {}
    except Exception as e:
        print("Error fetching OS info:", e)
        return {}

if __name__ == "__main__":
    print(json.dumps(get_os_info(), indent=2))
