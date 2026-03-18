import schedule
import time
from pipeline import run_pipeline

def start_scheduler():
    print("Scheduler started...")

    #schedule.every().day.at("07:00").do(run_pipeline)
    schedule.every().minute.do(run_pipeline)

    while True:
        schedule.run_pending()
        time.sleep(60)

start_scheduler()