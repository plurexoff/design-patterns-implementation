"""Comparison: Factory Method BEFORE vs AFTER."""

import time
from typing import List

from . import before, after


def compare_implementations():
    """Compare before and after implementations."""
    print("="*70)
    print("FACTORY METHOD PATTERN - BEFORE vs AFTER COMPARISON")
    print("="*70)
    
    # ============ BEFORE ============
    print("\n📊 WITHOUT Pattern (before.py):")
    print("-" * 70)
    
    print("\n❌ Problems:")
    print("  1. Hardcoded logic in create_vps()")
    print("  2. Client code knows about all VPS classes")
    print("  3. Adding new provider requires modifying create_vps()")
    print("  4. Violates Open/Closed Principle")
    print("  5. Changes in provider logic leak to client")
    
    # Example
    vps1 = before.create_vps("aws", "web-1", "t2.micro")
    vps2 = before.create_vps("azure", "web-2", "Standard_B1s")
    
    print(f"\n  Created: {vps1.provider}, {vps2.provider}")
    print(f"  Cost: ${vps1.get_cost() + vps2.get_cost()}/month")
    
    # ============ AFTER ============
    print("\n\n📊 WITH Pattern (after.py):")
    print("-" * 70)
    
    print("\n✅ Benefits:")
    print("  1. Object creation logic is centralized in VPSFactory")
    print("  2. Client code doesn't know about concrete implementations")
    print("  3. Adding new provider only requires new class + registration")
    print("  4. Follows Open/Closed Principle")
    print("  5. Easy to extend with new providers at runtime")
    
    # Example
    vps1 = after.VPSFactory.create("aws", "web-1", "t2.micro")
    vps2 = after.VPSFactory.create("azure", "web-2", "Standard_B1s")
    vps3 = after.VPSFactory.create("gcp", "web-3", "e2-micro")
    vps4 = after.VPSFactory.create("digitalocean", "web-4", "s-1vcpu-512mb")
    
    print(f"\n  Created: {vps1.provider}, {vps2.provider}, {vps3.provider}, {vps4.provider}")
    total = vps1.get_cost() + vps2.get_cost() + vps3.get_cost() + vps4.get_cost()
    print(f"  Cost: ${total}/month")
    print(f"  Available providers: {after.VPSFactory.get_providers()}")
    
    # ============ COMPARISON ============
    print("\n\n📈 Detailed Comparison:")
    print("-" * 70)
    
    comparison_table = f"""
    ┌─────────────────────────────────────┬──────────────────┬──────────────────┐
    │ Aspect                              │ BEFORE           │ AFTER            │
    ├─────────────────────────────────────┼──────────────────┼──────────────────┤
    │ Object Creation                     │ Hardcoded if-els │ Centralized      │
    │ Adding New Provider                 │ Modify function  │ Register class   │
    │ Client Dependencies                 │ All classes      │ Only Factory     │
    │ Runtime Extension                   │ ❌ Not possible  │ ✅ Easy          │
    │ Open/Closed Principle              │ ❌ Violated      │ ✅ Followed      │
    │ Lines to Add New Provider            │ ~5-10            │ ~2-3             │
    │ Maintenance Difficulty              │ High             │ Low              │
    │ Testability                         │ Medium           │ High             │
    │ Code Duplication                    │ High             │ Low              │
    │ Extensibility                       │ Poor             │ Excellent        │
    └─────────────────────────────────────┴──────────────────┴──────────────────┘
    """
    print(comparison_table)
    
    # ============ SCALABILITY TEST ============
    print("\n\n⚡ Scalability Test:")
    print("-" * 70)
    
    # Before - measure time to create many VPS instances
    start = time.perf_counter()
    for i in range(1000):
        vps = before.create_vps("aws", f"server-{i}", "t2.micro")
    before_time = time.perf_counter() - start
    
    # After - measure time to create many VPS instances
    start = time.perf_counter()
    for i in range(1000):
        vps = after.VPSFactory.create("aws", f"server-{i}", "t2.micro")
    after_time = time.perf_counter() - start
    
    print(f"\nCreating 1000 VPS instances:")
    print(f"  Before (hardcoded): {before_time*1000:.2f}ms")
    print(f"  After (factory):    {after_time*1000:.2f}ms")
    print(f"  Overhead: {((after_time/before_time - 1) * 100):.1f}%")
    
    # ============ CODE COMPLEXITY ============
    print("\n\n📝 Code Metrics:")
    print("-" * 70)
    
    metrics = f"""
    Before Implementation:
      - create_vps() function: ~10 lines
      - If-elif-elif-else: 4 conditions
      - Client knows: 3 classes (AWSVPS, AzureVPS, GCPVPS)
      - To add new provider: Modify create_vps()
    
    After Implementation:
      - VPSFactory class: ~25 lines (reusable)
      - VPS abstract class: ~15 lines (extensible)
      - Each provider: ~5-8 lines
      - To add new provider: Create new class, call register()
    
    Complexity with n providers:
      - Before: O(n) - O(n) growth in create_vps()
      - After: O(1) - Constant time to add provider
    """
    print(metrics)
    
    # ============ CONCLUSION ============
    print("\n\n🎯 CONCLUSION:")
    print("=" * 70)
    conclusion = """
    Factory Method Pattern ADVANTAGES:
    
    1. 🔐 Encapsulation
       - Object creation logic is hidden from client
       - Changes to creation logic don't affect client
    
    2. 📈 Extensibility
       - Adding new types doesn't require modifying factory function
       - Runtime registration of new providers
    
    3. 🧪 Testability
       - Easy to mock the factory for testing
       - Can test different providers independently
    
    4. 🏗️ Architecture
       - Promotes loose coupling
       - Follows Open/Closed Principle (SOLID)
    
    5. 🔄 Maintainability
       - Central place for object creation logic
       - Easier to understand and modify
    
    COST-BENEFIT ANALYSIS:
      - Small projects: Overhead may not be worth it
      - Large projects: Factory method is essential
      - Dynamic object creation: Factory method is necessary
    
    REAL-WORLD USE CASES:
      ✅ Database driver selection
      ✅ Payment gateway integration
      ✅ Cloud provider abstraction
      ✅ Logger implementations
      ✅ Caching strategies
      ✅ Serialization formats
    """
    print(conclusion)


if __name__ == "__main__":
    compare_implementations()
