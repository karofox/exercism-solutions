"""Module for building tree-like structured posts layout for web forums."""

import dataclasses


@dataclasses.dataclass
class Record:
    """Represents record that specifies tree node data."""

    record_id: int
    parent_id: int


@dataclasses.dataclass
class Node:
    """Represents tree node with id. Optionally, it can have children."""

    node_id: int
    children: list[Record] = dataclasses.field(default_factory=list)


def BuildTree(records: list[Record]) -> Node:
    """Builds tree based on the given Record list."""
    records.sort(key=lambda record: record.record_id)

    if not records:
        return None

    if records[-1].record_id != len(records) - 1:
        raise ValueError("Record id is invalid or out of order.")
    if records[0].record_id != 0:
        raise ValueError("Invalid root id.")
    if any(record.record_id < record.parent_id for record in records):
        raise ValueError("Node parent_id should be smaller than it's record_id.")
    if any(record.record_id == record.parent_id for record in records[1:]):
        raise ValueError("Only root should have equal record and parent id.")

    tree = [Node(record.record_id) for record in records]

    for record in records[1:]:
        parent = tree[record.parent_id]
        child = tree[record.record_id]
        parent.children.append(child)

    return tree[0]
