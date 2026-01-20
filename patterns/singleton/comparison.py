"""Comparison: Singleton BEFORE vs AFTER."""

import time
from threading import Thread
from . import before, after


def compare_implementations():
    """Compare before and after implementations."""
    print("="*70)
    print("SINGLETON PATTERN - BEFORE vs AFTER COMPARISON")
    print("="*70)
    
    # ============ BEFORE ============
    print("\n📊 WITHOUT Pattern:")
    print("-" * 70)
    
    db1 = before.DatabaseConnection("localhost", 5432, "myapp")
    db2 = before.DatabaseConnection("localhost", 5432, "myapp")
    db3 = before.DatabaseConnection("localhost", 5432, "myapp")
    
    print(f"\ndb1 is db2: {db1 is db2}")
    print(f"Instance count: {before.DatabaseConnection._instance_count}")
    print("\n❌ Problems:")
    print("  - Multiple instances waste resources")
    print("  - Database connection pooling inefficient")
    print("  - Potential race conditions")
    print("  - Inconsistent state management")
    
    # ============ AFTER ============
    print("\n\n📊 WITH Pattern:")
    print("-" * 70)
    
    db1 = after.DatabaseConnection("localhost", 5432, "myapp")
    db2 = after.DatabaseConnection("localhost", 5432, "myapp")
    db3 = after.DatabaseConnection("localhost", 5432, "myapp")
    
    print(f"\ndb1 is db2: {db1 is db2}")
    print(f"db1 is db3: {db1 is db3}")
    print("\n✅ Benefits:")
    print("  - Single instance ensures resource efficiency")
    print("  - Global point of access")
    print("  - Thread-safe implementation")
    print("  - Consistent state management")
    
    # ============ COMPARISON ============
    print("\n\n📈 Detailed Comparison:")
    print("-" * 70)
    
    comparison_table = f"""
    ┌───────────────────────┬────────────────┬────────────────┐
    │ Aspect                    │ BEFORE           │ AFTER            │
    ├───────────────────────┼────────────────┼────────────────┤
    │ Instance Count             │ Multiple (3+)    │ Single           │
    │ Resource Efficiency        │ Low              │ High             │
    │ Thread Safety              │ ❌ Risky         │ ✅ Safe           │
    │ Global Access              │ Need to pass ref │ Easy access      │
    │ State Consistency          │ ❌ Inconsistent  │ ✅ Guaranteed    │
    │ Memory Usage                │ High             │ Low              │
    │ Connection Pooling         │ ❌ Complex      │ ✅ Simple        │
    │ Testing Difficulty         │ Medium           │ High             │
    └───────────────────────┴────────────────┴────────────────┘
    """
    print(comparison_table)
    
    # ============ REAL WORLD EXAMPLES ============
    print("\n\n🔹 Real-World Examples:")
    print("-" * 70)
    
    logger1 = after.Logger()
    logger2 = after.Logger()
    
    print("\nLogger Singleton:")
    logger1.log("Application started")
    logger2.log("Processing request")
    logger1.log("Received response")
    
    print(f"\nAll logs from logger1: {len(logger1.get_logs())} entries")
    print(f"Same logs in logger2: {len(logger2.get_logs())} entries")
    print(f"logger1 is logger2: {logger1 is logger2}")
    
    # Cache example
    cache1 = after.Cache()
    cache2 = after.Cache()
    
    print("\n\nCache Singleton:")
    cache1.set("user:1", {"name": "Alice"})
    cache1.set("user:2", {"name": "Bob"})
    
    print(f"Set in cache1: 2 items")
    print(f"Get from cache2: user:1 = {cache2.get('user:1')}")
    print(f"Get from cache2: user:2 = {cache2.get('user:2')}")
    print(f"cache1 is cache2: {cache1 is cache2}")
    
    # ============ PERFORMANCE ============
    print("\n\n⚡ Performance Test:")
    print("-" * 70)
    
    # Without Singleton
    start = time.perf_counter()
    for i in range(1000):
        db = before.DatabaseConnection("localhost", 5432, f"db{i}")
    before_time = time.perf_counter() - start
    before_instances = before.DatabaseConnection._instance_count
    
    # With Singleton
    start = time.perf_counter()
    for i in range(1000):
        db = after.DatabaseConnection("localhost", 5432, f"db{i}")
    after_time = time.perf_counter() - start
    
    print(f"\nCreating 1000 database connections:")
    print(f"  Without Singleton:")
    print(f"    - Time: {before_time*1000:.2f}ms")
    print(f"    - Instances created: {before_instances}")
    print(f"    - Memory: ~{before_instances * 100}MB (estimate)")
    print(f"\n  With Singleton:")
    print(f"    - Time: {after_time*1000:.2f}ms")
    print(f"    - Instances created: 1")
    print(f"    - Memory: ~100MB (estimate)")
    print(f"\n  Efficiency: {before_time / after_time:.0f}x faster with Singleton")
    print(f"  Memory saved: ~{(before_instances - 1) * 100}MB")
    
    # ============ CONCLUSION ============
    print("\n\n🎯 CONCLUSION:")
    print("=" * 70)
    conclusion = """
    Singleton Pattern ADVANTAGES:
    
    1. 💾 Resource Efficiency
       - Single instance = single connection/resource
       - Perfect for expensive objects (database, file handles)
    
    2. 📦 Global Point of Access
       - Easy to access from anywhere without passing references
       - Reduces function parameter coupling
    
    3. 🛡️ Thread Safety
       - When properly implemented with locks
       - Ensures data consistency in multi-threaded environments
    
    4. 🎨 Lazy Initialization
       - Instance created only when first needed
       - Reduces startup time if not all singletons are used
    
    SINGLETON ANTI-PATTERNS:
    ❌ Don't overuse - can hide dependencies
    ❌ Makes testing harder - creates global state
    ❌ Can lead to tight coupling
    ❌ Not suitable for stateless services
    
    REAL-WORLD USE CASES:
      ✅ Database connections
      ✅ Logging services
      ✅ Configuration management
      ✅ Caching services
      ✅ Thread pools
      ✅ Application settings
    """
    print(conclusion)


if __name__ == "__main__":
    compare_implementations()
