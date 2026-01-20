"""MVC - BEFORE: Without pattern (spaghetti code)."""

from typing import List, Dict


class TodoApp:
    """❌ WITHOUT MVC - Everything mixed together."""
    
    def __init__(self):
        self.todos: List[Dict] = []
        self.next_id = 1
    
    def add_todo(self, title: str):
        """Mix of business logic and UI."""
        todo = {
            "id": self.next_id,
            "title": title,
            "done": False
        }
        self.todos.append(todo)
        self.next_id += 1
        # UI logic mixed in
        print(f"✅ Added: {title}")
    
    def show_todos(self):
        """Mix of data retrieval and display."""
        print("\n=== TODO LIST ===")
        if not self.todos:
            print("No todos yet!")
        for todo in self.todos:
            status = "✓" if todo["done"] else " "
            print(f"[{status}] {todo['id']}: {todo['title']}")
        print("" + "="*15)
    
    def mark_done(self, todo_id: int):
        """Mix of business logic and UI."""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["done"] = True
                # UI logic mixed in
                print(f"✓ Marked done: {todo['title']}")
                return
        print(f"\u274c Todo #{todo_id} not found")
    
    def delete_todo(self, todo_id: int):
        """Mix of business logic and display."""
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                title = todo["title"]
                del self.todos[i]
                print(f"🗑️ Deleted: {title}")
                self.show_todos()  # Forced refresh
                return
        print(f"\u274c Todo #{todo_id} not found")


if __name__ == "__main__":
    print("❌ WITHOUT MVC Pattern (Spaghetti Code):\n")
    
    app = TodoApp()
    app.add_todo("Learn Design Patterns")
    app.add_todo("Apply MVC")
    app.add_todo("Build project")
    
    app.show_todos()
    
    app.mark_done(1)
    
    app.show_todos()
    
    print("\n⚠️  PROBLEMS:")
    print("  - Data (Model) mixed with UI (View)")
    print("  - Business logic tangled with display logic")
    print("  - Impossible to test business logic separately")
    print("  - Can't change UI without touching business logic")
    print("  - Hard to reuse code for other UIs (API, CLI, etc.)")
    print("  - Violates Separation of Concerns")
    print("  - Difficult to maintain and extend")
