import platform
import socket
import getpass
import os
import psutil

from pathlib import Path


def get_cpu_model() -> str:
    try:
        with Path("/proc/cpuinfo").open(encoding="utf-8") as file:
            for line in file:
                if line.startswith("model name"):
                    return line.split(":", 1)[1].strip()

    except OSError:
        pass

    return platform.processor() or "Unknown"


def get_os_name() -> str:
    try:
        return platform.freedesktop_os_release().get(
            "PRETTY_NAME",
            platform.system()
        )

    except OSError:
        return platform.system()


def get_interface() -> str:
    desktop = os.getenv("XDG_CURRENT_DESKTOP") or os.getenv(
        "DESKTOP_SESSION", "Unknown"
    )

    session = os.getenv("XDG_SESSION_TYPE", "Unknown")

    return f"{desktop} / {session.upper()}"


def system_info() -> dict:
    memory = psutil.virtual_memory()

    return {
        "host": socket.gethostname(),
        "os": get_os_name(),
        "kernel": platform.release(),
        "arch": platform.machine(),
        "user": getpass.getuser(),
        "interface": get_interface(),
        "cpu": get_cpu_model(),
        "memory_total": round(memory.total / (1024 ** 3), 2)
    }