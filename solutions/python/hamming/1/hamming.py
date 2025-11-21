"""Hamming Distance module."""

def distance(strand_a: str, strand_b: str) -> int:
    """Returns the Hamming Distance between to DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(strand_a[idx] != strand_b[idx] for idx in range(len(strand_a)))
