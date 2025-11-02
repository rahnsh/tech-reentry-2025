import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

DEFAULT_DB = Path(__file__).with_name("tasks.json")

@dataclass
class Task:
    id: int
    title: str
    done: bool = False

class TaskStore:
    def __init__(self, db_path: Path = DEFAULT_DB):
        self.db_path = Path(db_path)
        self.tasks: List[Task] = []
        self._load()

    def _load(self):
        if self.db_path.exists():
            data = json.loads(self.db_path.read_text(encoding="utf-8"))
            self.tasks = [Task(**item) for item in data]
        else:
            self.tasks = []

    def _save(self):
        self.db_path.write_text(
            json.dumps([asdict(t) for t in self.tasks], indent=2),
            encoding="utf-8"
        )

    def add(self, title: str) -> Task:
        next_id = (max([t.id for t in self.tasks]) + 1) if self.tasks else 1
        task = Task(id=next_id, title=title, done=False)
        self.tasks.append(task)
        self._save()
        return task

    def list(self) -> List[Task]:
        return list(self.tasks)

    def mark_done(self, task_id: int) -> Task:
        for t in self.tasks:
            if t.id == task_id:
                t.done = True
                self._save()
                return t
        raise ValueError(f"No task with id {task_id}")

    def clear(self, done_only: bool = False) -> int:
        if done_only:
            before = len(self.tasks)
            self.tasks = [t for t in self.tasks if not t.done]
            removed = before - len(self.tasks)
        else:
            removed = len(self.tasks)
            self.tasks = []
        self._save()
        return removed
