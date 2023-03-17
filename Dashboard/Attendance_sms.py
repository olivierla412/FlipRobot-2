import requests
import PySimpleGUI as sg

# Replace these values with your own Twilio account details
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number_here'

# Replace this with the phone number of your school's attendance office
ATTENDANCE_PHONE_NUMBER = 'your_attendance_phone_number_here'

# Create the PySimpleGUI window layout
layout = [[sg.Text('Enter your name: '), sg.InputText(key='name')],
          [sg.Text('Enter your student ID: '), sg.InputText(key='student_id')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

# Create the PySimpleGUI window
window = sg.Window('SMS-based Attendance System').Layout(layout)

# Start the PySimpleGUI event loop
while True:
    event, values = window.Read()
    if event == 'Submit':
        # Send an SMS message to the attendance office with the student's name and ID
        message = f"{values['name']} ({values['student_id']}) has arrived at school."
        payload = {'To': ATTENDANCE_PHONE_NUMBER, 'From': TWILIO_PHONE_NUMBER, 'Body': message}
        response = requests.post(f'https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Messages.json',
                                 auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN), data=payload)
        # Display a message indicating whether the SMS was sent successfully or not
        if response.status_code == 201:
            sg.Popup('Attendance submitted successfully!')
        else:
            sg.Popup('There was an error submitting your attendance. Please try again.')
    elif event == 'Cancel' or event == sg.WIN_CLOSED:
        # Close the PySimpleGUI window and exit the program
        window.Close()
        break
