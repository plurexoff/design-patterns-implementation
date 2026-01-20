"""Singleton - AFTER: With pattern (single instance)."""

from threading import Lock
from typing import Optional


class Singleton:
    """Base Singleton metaclass for thread-safe implementation."""
    _instances = {}
    _lock = Lock()
    
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__new__(cls)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(Singleton):
    """Database connection WITH Singleton pattern."""
    
    def __init__(self, host: str, port: int, database: str):
        # Prevent re-initialization
        if hasattr(self, 'host'):
            return
        
        self.host = host
        self.port = port
        self.database = database
        self.is_connected = False
        print(f"Creating SINGLE database connection")
    
    def connect(self):
        self.is_connected = True
        return f"Connected to {self.host}:{self.port}/{self.database}"
    
    def execute_query(self, query: str):
        if not self.is_connected:
            return "Error: Not connected"
        return f"Executing: {query}"
    
    @classmethod
    def get_instance(cls, host: str = "localhost", 
                     port: int = 5432, 
                     database: str = "myapp") -> 'DatabaseConnection':
        """Get or create the single instance."""
        return cls(host, port, database)


class Logger(Singleton):
    """Logger service - another example of Singleton."""
    
    def __init__(self):
        if hasattr(self, 'logs'):
            return
        self.logs = []
        print("Creating SINGLE logger instance")
    
    def log(self, message: str):
        self.logs.append(message)
        print(f"[LOG] {message}")
    
    def get_logs(self):
        return self.logs


class Cache(Singleton):
    """Cache service - another example of Singleton."""
    
    def __init__(self):
        if hasattr(self, 'data'):
            return
        self.data = {}
        print("Creating SINGLE cache instance")
    
    def set(self, key: str, value):
        self.data[key] = value
    
    def get(self, key: str):
        return self.data.get(key)
    
    def clear(self):
        self.data.clear()


if __name__ == "__main__":
    print("✅ WITH Singleton Pattern:\n")
    
    # Problem solved: Only one instance is created
    db1 = DatabaseConnection("localhost", 5432, "myapp")
    db2 = DatabaseConnection("localhost", 5432, "myapp")
    db3 = DatabaseConnection("localhost", 5432, "myapp")
    
    print(f"\ndb1 is db2: {db1 is db2}  # True - Same object!")
    print(f"db1 is db3: {db1 is db3}  # True - Same object!")
    
    print(f"\ndb1: {db1.connect()}")
    print(f"db2: {db2.execute_query('SELECT * FROM users')}")
    print(f"db3: {db3.execute_query('SELECT * FROM products')}")
    
    # Logger singleton
    print("\n--- Logger Singleton ---")
    logger1 = Logger()
    logger2 = Logger()
    logger3 = Logger()
    
    print(f"logger1 is logger2: {logger1 is logger2}  # True")
    print(f"logger1 is logger3: {logger1 is logger3}  # True")
    
    logger1.log("Starting application")
    logger2.log("Processing request")
    logger3.log("Application started")
    
    print(f"Total logs: {len(logger1.get_logs())}")
    
    # Cache singleton
    print("\n--- Cache Singleton ---")
    cache1 = Cache()
    cache2 = Cache()
    
    print(f"cache1 is cache2: {cache1 is cache2}  # True")
    
    cache1.set("user:1", {"name": "Alice", "age": 30})
    print(f"cache2.get('user:1'): {cache2.get('user:1')}")
    
    print("\n✨ BENEFITS:")
    print("  ✅ Only one instance exists")
    print("  ✅ Global point of access")
    print("  ✅ Resource efficiency")
    print("  ✅ Thread-safe implementation")
    print("  ✅ Lazy initialization (on first use)")
    print("  ✅ Easy to access from anywhere in application")
