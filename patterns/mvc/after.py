"""MVC - AFTER: With pattern (clean separation)."""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional


# ============ MODEL ============
class Todo:
    """Represents a single todo item."""
    def __init__(self, todo_id: int, title: str):
        self.id = todo_id
        self.title = title
        self.done = False


class TodoModel:
    """✅ MODEL: Handles all business logic and data."""
    
    def __init__(self):
        self.todos: List[Todo] = []
        self.next_id = 1
    
    def add(self, title: str) -> Todo:
        """Add a new todo."""
        todo = Todo(self.next_id, title)
        self.todos.append(todo)
        self.next_id += 1
        return todo
    
    def get_all(self) -> List[Todo]:
        """Get all todos."""
        return self.todos
    
    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        """Get todo by ID."""
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def mark_done(self, todo_id: int) -> bool:
        """Mark todo as done."""
        todo = self.get_by_id(todo_id)
        if todo:
            todo.done = True
            return True
        return False
    
    def delete(self, todo_id: int) -> bool:
        """Delete a todo."""
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False
    
    def count_done(self) -> int:
        """Count completed todos."""
        return sum(1 for todo in self.todos if todo.done)


# ============ VIEW ============
class TodoView(ABC):
    """✅ VIEW: Abstract view interface."""
    
    @abstractmethod
    def show_todos(self, todos: List[Todo]) -> None:
        pass
    
    @abstractmethod
    def show_message(self, message: str) -> None:
        pass
    
    @abstractmethod
    def show_error(self, error: str) -> None:
        pass


class CliTodoView(TodoView):
    """✅ VIEW: Command-line interface implementation."""
    
    def show_todos(self, todos: List[Todo]) -> None:
        print("\n=== TODO LIST ===")
        if not todos:
            print("No todos yet!")
        for todo in todos:
            status = "✓" if todo.done else " "
            print(f"[{status}] {todo.id}: {todo.title}")
        print("" + "="*15 + "\n")
    
    def show_message(self, message: str) -> None:
        print(f"✅ {message}")
    
    def show_error(self, error: str) -> None:
        print(f"❌ {error}")


class JsonTodoView(TodoView):
    """✅ VIEW: JSON API implementation."""
    
    def show_todos(self, todos: List[Todo]) -> None:
        import json
        data = [
            {"id": t.id, "title": t.title, "done": t.done}
            for t in todos
        ]
        print(json.dumps(data, indent=2))
    
    def show_message(self, message: str) -> None:
        print(f'{{"status": "success", "message": "{message}"}}')
    
    def show_error(self, error: str) -> None:
        print(f'{{"status": "error", "message": "{error}"}}')


# ============ CONTROLLER ============
class TodoController:
    """✅ CONTROLLER: Handles user input and updates Model/View."""
    
    def __init__(self, model: TodoModel, view: TodoView):
        self.model = model
        self.view = view
    
    def add_todo(self, title: str) -> None:
        """User adds a new todo."""
        self.model.add(title)
        self.view.show_message(f"Added: {title}")
    
    def show_todos(self) -> None:
        """User views all todos."""
        todos = self.model.get_all()
        self.view.show_todos(todos)
    
    def mark_done(self, todo_id: int) -> None:
        """User marks todo as done."""
        if self.model.mark_done(todo_id):
            todo = self.model.get_by_id(todo_id)
            self.view.show_message(f"Marked done: {todo.title}")
        else:
            self.view.show_error(f"Todo #{todo_id} not found")
    
    def delete_todo(self, todo_id: int) -> None:
        """User deletes a todo."""
        todo = self.model.get_by_id(todo_id)
        if self.model.delete(todo_id):
            self.view.show_message(f"Deleted: {todo.title}")
        else:
            self.view.show_error(f"Todo #{todo_id} not found")
    
    def get_stats(self) -> Dict:
        """Get app statistics."""
        todos = self.model.get_all()
        return {
            "total": len(todos),
            "done": self.model.count_done(),
            "pending": len(todos) - self.model.count_done()
        }


if __name__ == "__main__":
    print("✅ WITH MVC Pattern (Clean Separation):\n")
    
    # Create Model and CLI View
    model = TodoModel()
    cli_view = CliTodoView()
    controller = TodoController(model, cli_view)
    
    # Use the app
    controller.add_todo("Learn Design Patterns")
    controller.add_todo("Apply MVC")
    controller.add_todo("Build project")
    
    controller.show_todos()
    
    controller.mark_done(1)
    controller.show_todos()
    
    # Easy to switch to JSON view without changing Model or Controller logic!
    print("\n--- Switching to JSON API View ---\n")
    json_view = JsonTodoView()
    api_controller = TodoController(model, json_view)
    
    api_controller.show_todos()
    api_controller.add_todo("New task")
    
    print("\n\n✨ BENEFITS:")
    print("  ✅ Clear separation of concerns")
    print("  ✅ Model: Pure business logic (testable)")
    print("  ✅ View: Display logic only (swappable)")
    print("  ✅ Controller: User interactions (thin)")
    print("  ✅ Easy to test each layer independently")
    print("  ✅ Easy to add new views (HTML, API, etc.)")
    print("  ✅ Model can be used by multiple views")
    print("  ✅ UI changes don't affect business logic")
