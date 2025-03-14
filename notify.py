from pushbullet import Pushbullet

API_KEY = "o.rPzjmQqA9P15fvbPlCmwcHhVQmEjwIYZ"

def send_notification():
    pb = Pushbullet(API_KEY)
    push = pb.push_note("Test Notification", "This is a test notification from GitHub Actions!")
    print("Notification Sent!")

send_notification()
