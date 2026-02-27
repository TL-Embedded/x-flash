import json, subprocess, os

def load_config(path: str):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        fail("Configuration file could not be loaded")

def print_color(color:str, text: str):
    code = {
        "r":"\033[31m",
        "g":"\033[32m",
        "y":"\033[33m",
        "w":"\033[0m",
    }[color]

    print(code + text + "\033[0m")

def fail(message: str):
    print_color("r", "Error: " + message)
    input("Press enter to exit...")
    exit(1)

def success(message: str):
    print_color("g", message)
    input("Press enter to exit...")
    exit(0)

def flash_target(cfg, openocd_path: str):
    cmd = [
        "./openocd/bin/openocd.exe",
        "-f", cfg['interface'],
        "-c", "transport select swd",
        "-f", cfg['target'],
        "-c", f"program \"{cfg['firmware']}\" verify reset exit"
        ]
    result = subprocess.run(cmd, capture_output=True)
    status, stderr = result.returncode, result.stderr.decode()
    if status != 0:
        if "Error: open failed" in stderr:
            fail("Adaptor not detected")
        if "Error: target voltage may be too low for reliable debugging" in stderr:
            fail("Target low voltage")
        if "Error: init mode failed" in stderr:
            fail("Target connection failure")
        else:
            print_color("y", stderr)
            fail("Unknown failure!")


if __name__ == "__main__":
    openocd_path = "./openocd/bin/openocd.exe"
    cfg = load_config("config.json")
    if not os.path.exists(cfg['firmware']):
        fail("Firmware not found")
    if not os.path.exists(openocd_path):
        fail("OpenODC not found")
    input("Press enter to flash target...")
    flash_target(cfg, openocd_path)
    success("Target programmed successfully")
