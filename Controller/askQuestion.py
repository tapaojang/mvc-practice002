import csv
csv_path = 'Model/questions.csv'
from datetime import datetime
def check_office_hours():
    currentTime = datetime.now().time()
    startTime = datetime.strptime('17:00:00', '%H:%M:%S').time()
    endTime = datetime.strptime('08:00:00', '%H:%M:%S').time()

    if currentTime >= startTime or currentTime <= endTime:
        return True
    return False

def askQuestions(name, question):
    answer = f'Sorry, we are out of service in this moment'
    if not check_office_hours():
        answer = f'That is interesting {name} , that you said {question}. I will send this message to someone else very soon. Anything else I can help?'
        with open(csv_path, mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([name, question, answer]) 
            csv_writer.writerow([]) 
    return answer
   
