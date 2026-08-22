from pathlib import Path

from dry4c.core import find_duplicates


def test_cross_file_duplicate_is_found(tmp_path: Path) -> None:
    first = tmp_path / ("a_" + 'sample.c')
    second = tmp_path / ("b_" + 'sample.c')
    first.write_text('int choose(int a, int b) {\n  if (a && b) { return 1; }\n  return 0;\n}\n', encoding="utf-8")
    second.write_text('int decide(int a, int b) {\n  if (a && b) { return 1; }\n  return 0;\n}\n', encoding="utf-8")
    duplicates = find_duplicates(tmp_path, min_tokens=8)
    assert duplicates


def test_non_overlapping_same_file_duplicate_is_found(tmp_path: Path) -> None:
    path = tmp_path / 'sample.c'
    path.write_text('int choose(int a, int b) {\n  if (a && b) { return 1; }\n  return 0;\n}\n' + "\n" + 'int decide(int a, int b) {\n  if (a && b) { return 1; }\n  return 0;\n}\n', encoding="utf-8")
    duplicates = find_duplicates(tmp_path, min_tokens=8)
    assert any(item.locations[0].file == item.locations[1].file for item in duplicates)
