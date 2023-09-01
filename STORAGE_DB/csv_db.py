import csv

class CSVDatabase:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def insert(self, data):
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self._get_next_id(), *data])

    def _get_next_id(self):
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            num_rows = sum(1 for _ in reader)
            return num_rows + 1

    def search(self, search_id):
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[0]) == search_id:
                    return row[1:]
        return None

    def update(self, update_id, new_data):
        rows = []
        found = False

        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[0]) == update_id:
                    found = True
                    rows.append([update_id, *new_data])
                else:
                    rows.append(row)

        if found:
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        else:
            raise ValueError(f"Record with ID {update_id} not found")

    def delete(self, delete_id):
        rows = []
        found = False

        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[0]) == delete_id:
                    found = True
                else:
                    rows.append(row)

        if found:
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        else:
            raise ValueError(f"Record with ID {delete_id} not found")

if __name__ == "__main__":
    db = CSVDatabase("data.csv")

    # Insert data
    db.insert(["Alice", 30])
    db.insert(["Bob", 25])
    
    # Get data by ID
    user1 = db.search(1)
    print("User 1:", user1)
    
    # Update data
    db.update(1, ["Alice Smith", 31])
    user1_updated = db.search(1)
    print("Updated User 1:", user1_updated)

    # Delete data
    db.delete(2)
    user2_deleted = db.search(2)
    print("User 2 (after deletion):", user2_deleted)
