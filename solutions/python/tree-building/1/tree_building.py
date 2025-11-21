class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []


def BuildTree(records: list[Record]) -> Node:
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

    for record in records:
        if record.record_id == 0:
            continue
        parent = tree[record.parent_id]
        child = tree[record.record_id]
        parent.children.append(child)

    return tree[0]
