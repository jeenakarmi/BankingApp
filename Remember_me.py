class RememberMe:
    def __init__(self):
        self.events = {}

    def storer(self):
        date = input("Enter the date (e.g., YYYY-MM-DD): ")
        events = input("Enter events to remember separated by commas: ").split(',')
        if date in self.events:
            self.events[date].extend(events)
        else:
            self.events[date] = events

    def checker(self):
        date = input("Enter the date you want to check (e.g., YYYY-MM-DD): ")
        if date in self.events:
            print("Events for {}: {}".format(date, ', '.join(self.events[date])))
        else:
            print("No events found for", date)

if __name__ == "__main__":
    remember = RememberMe()
    while True:
        choice = input("Enter '1' to store events, '2' to check events,'3' to view all events, or 'q' to quit: ")
        if choice == '1':
            remember.storer()
        elif choice == '2':
            remember.checker()
        elif choice == '3':
            if remember.events:
                for date, events in remember.events.items():
                    print("Date:", date)
                    print("Events:", ', '.join(events))
            else:
                print("No events stored.")
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")
