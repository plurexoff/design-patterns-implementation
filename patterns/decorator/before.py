"""Decorator - BEFORE: Without pattern (inheritance explosion)."""


class Notification:
    """Base notification class."""
    def send(self, message: str):
        return f"Sending: {message}"


class EmailNotification(Notification):
    """Email notification."""
    def send(self, message: str):
        return f"Email: {message}"


class SMSNotification(Notification):
    """Email + SMS notification."""
    def send(self, message: str):
        email = f"Email: {message}"
        sms = f"SMS: {message}"
        return f"{email}\n{sms}"


class SlackNotification(Notification):
    """Email + Slack notification."""
    def send(self, message: str):
        email = f"Email: {message}"
        slack = f"Slack: {message}"
        return f"{email}\n{slack}"


class EmailSMSNotification(Notification):
    """Email + SMS notification."""
    def send(self, message: str):
        email = f"Email: {message}"
        sms = f"SMS: {message}"
        return f"{email}\n{sms}"


class EmailSlackNotification(Notification):
    """Email + Slack notification."""
    def send(self, message: str):
        email = f"Email: {message}"
        slack = f"Slack: {message}"
        return f"{email}\n{slack}"


class EmailSMSSlackNotification(Notification):
    """Email + SMS + Slack notification."""
    def send(self, message: str):
        email = f"Email: {message}"
        sms = f"SMS: {message}"
        slack = f"Slack: {message}"
        return f"{email}\n{sms}\n{slack}"


if __name__ == "__main__":
    print("❌ WITHOUT Decorator Pattern (Inheritance Explosion):\n")
    
    # Client needs to know which combination to use
    notif = EmailSMSSlackNotification()
    print(notif.send("Alert: Server down!"))
    
    print("\n⚠️  PROBLEMS:")
    print("  - Class explosion: 2^n combinations for n channels")
    print("  - Rigid hierarchy")
    print("  - Hard to add new channels")
    print("  - Hard to combine channels dynamically")
    print("  - Violates Single Responsibility Principle")
    print("  - Violates DRY (Don't Repeat Yourself)")
    print("\n  Possible combinations (nightmare!):")
    print("  - Email")
    print("  - Email + SMS")
    print("  - Email + Slack")
    print("  - Email + SMS + Slack")
    print("  - SMS")
    print("  - SMS + Slack")
    print("  ... exponential growth!")
