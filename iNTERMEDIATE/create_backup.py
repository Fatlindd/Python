import os
import shutil
import time
from datetime import datetime
import schedule
from functools import partial


def backup_project(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    backup_subdir = os.path.join(backup_dir, f'{current_time}')

    shutil.copytree(source_dir, backup_subdir)
    print(f'Backup created at {backup_subdir}')


source_dir = '/Users/dev1/Documents/Python/iNTERMEDIATE/Collections'  # replace with your project path
backup_dir = '/Users/dev1/Documents/Python/iNTERMEDIATE/Backup'  # replace with your backup location path

# Create a partial function with the specified parameters
backup_job = partial(backup_project, source_dir, backup_dir)

# Schedule the backup to run every 5 seconds
schedule.every(5).seconds.do(backup_job)

while True:
    schedule.run_pending()  # Run pending scheduled tasks
    time.sleep(1)  # Sleep for a short time to avoid high CPU usage
