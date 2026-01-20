"""Decorator - AFTER: With pattern (flexible composition)."""

from abc import ABC, abstractmethod


class Notification(ABC):
    """Abstract notification interface."""
    
    @abstractmethod
    def send(self, message: str) -> str:
        pass


class EmailNotification(Notification):
    """Base email notification."""
    def send(self, message: str) -> str:
        return f"Email: {message}"


class NotificationDecorator(Notification, ABC):
    """Abstract decorator for notifications."""
    
    def __init__(self, notification: Notification):
        self.notification = notification
    
    def send(self, message: str) -> str:
        return self.notification.send(message)


class SMSDecorator(NotificationDecorator):
    """Adds SMS capability to any notification."""
    
    def send(self, message: str) -> str:
        base = self.notification.send(message)
        sms = f"SMS: {message}"
        return f"{base}\n{sms}"


class SlackDecorator(NotificationDecorator):
    """Adds Slack capability to any notification."""
    
    def send(self, message: str) -> str:
        base = self.notification.send(message)
        slack = f"Slack: {message}"
        return f"{base}\n{slack}"


class TelegramDecorator(NotificationDecorator):
    """Adds Telegram capability to any notification."""
    
    def send(self, message: str) -> str:
        base = self.notification.send(message)
        telegram = f"Telegram: {message}"
        return f"{base}\n{telegram}"


class PushDecorator(NotificationDecorator):
    """Adds Push notification capability."""
    
    def send(self, message: str) -> str:
        base = self.notification.send(message)
        push = f"Push: {message}"
        return f"{base}\n{push}"


if __name__ == "__main__":
    print("✅ WITH Decorator Pattern (Flexible Composition):\n")
    
    # Create base notification
    notif = EmailNotification()
    print("1. Base Email:")
    print(notif.send("Alert: Server down!"))
    
    # Add SMS decorator
    print("\n2. Email + SMS:")
    notif_with_sms = SMSDecorator(notif)
    print(notif_with_sms.send("Alert: Server down!"))
    
    # Add Slack decorator
    print("\n3. Email + SMS + Slack:")
    notif_full = SlackDecorator(notif_with_sms)
    print(notif_full.send("Alert: Server down!"))
    
    # Add Telegram decorator
    print("\n4. Email + SMS + Slack + Telegram:")
    notif_all = TelegramDecorator(notif_full)
    print(notif_all.send("Alert: Server down!"))
    
    # Dynamic composition
    print("\n5. Different combination (Email + Slack + Push):")
    notif_custom = EmailNotification()
    notif_custom = SlackDecorator(notif_custom)
    notif_custom = PushDecorator(notif_custom)
    print(notif_custom.send("System update available"))
    
    # User preference configuration
    print("\n6. User-configured notifications:")
    
    class User:
        def __init__(self, name, has_sms=False, has_slack=False, has_telegram=False):
            self.name = name
            self.has_sms = has_sms
            self.has_slack = has_slack
            self.has_telegram = has_telegram
        
        def get_notification(self):
            notif = EmailNotification()
            if self.has_sms:
                notif = SMSDecorator(notif)
            if self.has_slack:
                notif = SlackDecorator(notif)
            if self.has_telegram:
                notif = TelegramDecorator(notif)
            return notif
    
    # Different users with different preferences
    alice = User("Alice", has_sms=True, has_slack=True)
    bob = User("Bob", has_slack=True, has_telegram=True)
    charlie = User("Charlie", has_sms=True, has_telegram=True)
    
    print(f"\nAlice's notification ({alice.name}):")
    print(alice.get_notification().send("New message"))
    
    print(f"\nBob's notification ({bob.name}):")
    print(bob.get_notification().send("New message"))
    
    print(f"\nCharlie's notification ({charlie.name}):")
    print(charlie.get_notification().send("New message"))
    
    print("\n✨ BENEFITS:")
    print("  ✅ Flexible composition (unlimited combinations)")
    print("  ✅ Add/remove features dynamically at runtime")
    print("  ✅ Single Responsibility: each decorator does one thing")
    print("  ✅ No inheritance explosion")
    print("  ✅ Open/Closed Principle: open for extension, closed for modification")
    print("  ✅ Easy to test individual decorators")
