from datetime import datetime, timedelta
import numpy as np
import pandas as pd

class ProductivityTracker:
    def __init__(self):
        self.activities = pd.DataFrame(columns=['Activity','Date', 'Start Time', 'Stop Time'])
        self.current_activity = None
        self.current_start_time = None
        self.date_st = None

    def start_activity(self, activity):
        self.current_activity = activity
        self.current_start_time = datetime.now()
        self.date_st=self.current_start_time.date()
        self.current_start_time = self.current_start_time.time()
        print(f"Started activity '{activity}' at {self.current_start_time}")

    def stop_activity(self):
        if self.current_activity is not None:
            stop_time = datetime.now()
            stop_time = stop_time.time()
            log_entry = pd.DataFrame({'Activity': [self.current_activity],'Date':[self.date_st], 'Start Time': [self.current_start_time], 'Stop Time': [stop_time]})
            self.activities = pd.concat([self.activities, log_entry], ignore_index=True)
            print(f"Stopped activity '{self.current_activity}' at {stop_time}")
            self.current_activity = None
            self.current_start_time = None
        else:
            print("No activity is currently in progress.")

    def display_productivity(self):
        print("\nActivity Breakdown:")
        for index, row in self.activities.iterrows():
            duration = row['Stop Time'] - row['Start Time']
            print(f"{row['Activity']}: {duration}")

    def export_to_excel(self, file_path=r'C:\Users\hilcr\OneDrive\Desktop\Documents\Productivity_planner.xlsx'):
        self.activities.to_excel(file_path, index=False)
        print(f"Exported data to {file_path}")

if __name__ == "__main__":
    tracker = ProductivityTracker()

    while True:
        print("\n1. Start Activity")
        print("2. Stop Activity")
        print("3. Display Productivity")
        print("4. Export to Excel")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            activity = input("Enter the activity: ")
            tracker.start_activity(activity)
        elif choice == '2':
            tracker.stop_activity()
        elif choice == '3':
            tracker.display_productivity()
        elif choice == '4':
            tracker.export_to_excel()
        elif choice == '5':
            print("Exiting the productivity tracker.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
