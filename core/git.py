# core/git.py

import subprocess
import logging

def check_git():
    try:
        result = subprocess.run(['git', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            logging.info(f"[GIT] Git Client Found [{result.stdout.strip()}]")
            return True
        else:
            logging.warning("[GIT] Git Client Not Found!")
            return False
    except Exception as e:
        logging.error(f"[GIT] Error checking Git: {e}")
        return False

# Check on import
check_git()
