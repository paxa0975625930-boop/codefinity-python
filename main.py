from abc import ABC, abstractmethod

# Define the abstract base class Notifier
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
# Define the EmailNotifier subclass
class EmailNotifier(Notifier):
    def send(self, message: str):
        return f"Email sent: {message}"
# Define the SMSNotifier subclass
class SMSNotifier(Notifier):
    def send(self, message: str):
        return f"SMS sent: {message}"
# Define the notify_user function
def notify_user(notifier: Notifier, message: str):
    return notifier.send(message)

email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

print(notify_user(email_notifier, "Welcome!"))
print(notify_user(sms_notifier, "Your code is 1234."))