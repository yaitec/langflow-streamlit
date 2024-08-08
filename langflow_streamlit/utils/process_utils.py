from subprocess import run, PIPE
import logging
import httpx
import time
import sys

LOGGER = logging.getLogger(__name__)


def wait_for_server_ready(host, port):
    """
    Wait for the server to become ready by polling the health endpoint.
    """
    status_code = 0
    while status_code != 200:
        try:
            status_code = httpx.get(f"http://{host}:{port}/health").status_code
        except Exception:
            time.sleep(1)


def check_if_port_is_used_by_program(port, programs=[]):
    if sys.platform.startswith("linux") or sys.platform == "darwin":  # Linux and macOS
        command = f"lsof -i :{port}"
    elif sys.platform == "win32":
        command = f"netstat -ano | findstr :{port}"
    else:
        raise OSError(f"Unsupported platform: {sys.platform}")

    result = run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True).stdout
    if any([program in result for program in programs]):
        return True
    else:
        return False


def kill_process_on_port(port):
    if sys.platform.startswith("linux") or sys.platform == "darwin":  # Linux and macOS
        command = f"fuser -k {port}/tcp"
    elif sys.platform == "win32":
        command = (
            f"netstat -ano | findstr :{port} | " "for /F \"tokens=5\" %P in ('findstr :{port}') do taskkill /F /PID %P"
        )
    else:
        raise OSError(f"Unsupported platform: {sys.platform}")

    result = run(command, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    if result.returncode == 0:
        LOGGER.debug(f"Successfully killed the process using port {port}.")
    else:
        LOGGER.debug(f"Failed to kill the process using port {port}. Error: {result.stderr}")