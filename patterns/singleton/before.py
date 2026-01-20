"""Singleton - BEFORE: Without pattern (multiple instances)."""


class DatabaseConnection:
    """Database connection WITHOUT Singleton pattern."""
    
    _instance_count = 0
    
    def __init__(self, host: str, port: int, database: str):
        DatabaseConnection._instance_count += 1
        self.instance_id = DatabaseConnection._instance_count
        self.host = host
        self.port = port
        self.database = database
        self.is_connected = False
        print(f"Creating database connection #{self.instance_id}")
    
    def connect(self):
        self.is_connected = True
        return f"Connected to {self.host}:{self.port}/{self.database}"
    
    def execute_query(self, query: str):
        if not self.is_connected:
            return "Error: Not connected"
        return f"[Instance #{self.instance_id}] Executing: {query}"


if __name__ == "__main__":
    print("❌ WITHOUT Singleton Pattern:\n")
    
    # Problem: Client creates multiple instances
    db1 = DatabaseConnection("localhost", 5432, "myapp")
    db2 = DatabaseConnection("localhost", 5432, "myapp")
    db3 = DatabaseConnection("localhost", 5432, "myapp")
    
    print(f"db1 is db2: {db1 is db2}  # False - Different objects!")
    print(f"db1 is db3: {db1 is db3}  # False - Different objects!")
    
    print(f"\ndb1: {db1.connect()}")
    print(f"db2: {db2.connect()}")
    print(f"db3: {db3.connect()}")
    
    print(f"\ndb1: {db1.execute_query('SELECT * FROM users')}")
    print(f"db2: {db2.execute_query('SELECT * FROM products')}")
    print(f"db3: {db3.execute_query('SELECT COUNT(*) FROM orders')}")
    
    print(f"\nTotal instances created: {DatabaseConnection._instance_count}")
    
    print("\n⚠️  PROBLEMS:")
    print("  - Multiple instances of the same connection")
    print("  - Resource waste (3 connections instead of 1)")
    print("  - Each instance has its own state")
    print("  - Potential data consistency issues")
    print("  - Inefficient database connection pooling")
    print("  - Thread-safety issues with multiple instances")
