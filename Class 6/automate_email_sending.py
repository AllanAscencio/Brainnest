""" You work at a company that sends daily reports to clients via email. The goal of this project is to automate the
process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of
    the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred

    during the email sending process. """

# --------------------- IMPORTS ------------------ #

import smtplib
import os
import csv
import schedule
import pytz

# ------------------------ CREATING TEST CSV FILE ------------------------ #

with open('report_files.csv', 'w', newline='') as fhandle:
    writer = csv.writer(fhandle)
    writer.writerow(["email", "name", "lastname", "age"])
    writer.writerow(["john@example.com", "John", 'Doe', 25])
    writer.writerow(["jane@example.com", "Jane", 'Smith', 30])
    writer.writerow(["alex@example.com", "Alex", 'Johnson', 40])
    writer.writerow(["sara@example.com", "Sara", 'Williams', 28])
    writer.writerow(["mike@example.com", "Mike", 'Miller', 45])
    writer.writerow(["lisa@example.com", "Lisa", 'Davis', 32])
    writer.writerow(["david@example.com", 'David', 'Jones', 27])
    writer.writerow(["emily@example.com", 'Emily', 'Moore', 35])
    writer.writerow(["ryan@example.com", 'Ryan', 'Taylor', 31])
    writer.writerow(["amy@example.com", 'Amy', 'Anderson', 29])

# Use the os library to access the report files that need to be sent.
try:
    myFile = os.open("report_files.csv", os.O_RDONLY)
    myData = os.read(myFile, 1000)
    myStr = myData.decode("UTF-8")
    rows = (myStr.split())

except Exception as e:
    print(str(e))

finally:
    os.close(myFile)

emails = []
# We iterate from 1 and not 0 because we know 0 is the column names
for i in range(1, len(rows)):
    emails.append(rows[i].split(',')[0])

# ---------- CREDENTIALS ----------- #
MY_EMAIL = "YOUR_EMAIL"
PW = "YOUR_PASSWORD"

# ------------ MESSAGE -------------- #
SUBJECT = "Daily Report"
TEXT = "Report of the day: There is a Chilean Python Dev that is outstanding, very efficient and willing to work..."
msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

berlin_tz = pytz.timezone('Europe/Berlin')


def job():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PW)
        for email in emails:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=msg
            )
            return f"Email successfully sent to: {email}"


# Schedule the job every day at 10:30 am
try:
    schedule.every().day.at("10:30", "Europe/Berlin").do(job).timezone(berlin_tz)

except Exception as e:
    print(str(e))

finally:
    print(job())
