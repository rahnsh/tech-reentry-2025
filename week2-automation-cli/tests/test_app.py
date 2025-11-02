from pathlib import Path
from app import TaskStore

def test_add_list_done(tmp_path: Path):
    db = tmp_path / "tasks.json"
    store = TaskStore(db)

    store.add("task A")
    store.add("task B")
    items = store.list()

    assert len(items) == 2
    assert items[0].title == "task A"
    assert items[1].title == "task B"

    store.mark_done(1)
    items = store.list()

    assert items[0].done is True
    assert items[1].done is False

def test_clear(tmp_path: Path):
    db = tmp_path / "tasks.json"
    store = TaskStore(db)

    store.add("task A")
    store.add("task B")
    store.mark_done(2)

    removed_done = store.clear(done_only=True)
    assert removed_done == 1
    assert len(store.list()) == 1

    removed_all = store.clear(done_only=False)
    assert removed_all == 1
    assert len(store.list()) == 0
