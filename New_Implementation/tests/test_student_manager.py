from student_manager import StudentManager


def test_add_student():
    manager = StudentManager()
    student = manager.add_student("S101", "Alice", "AI")
    assert student["id"] == "S101"
    assert len(manager.get_all_students()) == 1


def test_search_student():
    manager = StudentManager()
    manager.add_student("S101", "Alice", "AI")
    results = manager.search_student("alice")
    assert len(results) == 1


def test_delete_student():
    manager = StudentManager()
    manager.add_student("S101", "Alice", "AI")
    deleted = manager.delete_student("S101")
    assert deleted["name"] == "Alice"
    assert len(manager.get_all_students()) == 0
