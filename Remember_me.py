
class RememberMe:
    def __init__(self):
        self.events = {}

    def storer(self):
        date = input("Enter the date (e.g., YYYY-MM-DD): ")
        events = input("Enter events to remember separated by commas: ").split(',')
        self.events[date] = events

    def checker(self):
        date = input("Enter the date you want to check (e.g., YYYY-MM-DD): ")
        if date in self.events:
            print("Events for {}: {}".format(date, ', '.join(self.events[date])))
        else:
            print("No events found for", date)

if __name__ == "__main__":
    remember = RememberMe()
    remember.storer()
    remember.checker()
