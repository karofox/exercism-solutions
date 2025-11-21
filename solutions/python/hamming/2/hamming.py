"""Hamming Distance module."""


def distance(strand_a: str, strand_b: str) -> int:
    """Returns the Hamming Distance between to DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(
        nucleotide_a != nucleotide_b
        for nucleotide_a, nucleotide_b in zip(strand_a, strand_b)
    )
