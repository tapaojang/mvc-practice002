import csv
csv_path = 'Model/username.csv'

def csvUsername():
    with open(csv_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = []
        next(csv_reader) 
        for row in csv_reader:
            if row:  # ตรวจสอบว่า row ไม่เป็นรายการว่าง
                if len(row) > 0: 
                    data.append(row[0])
        return data

def writeUsername(username):
    with open(csv_path, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([username])