"""RNA Transcription module."""

TRANSLATION = str.maketrans({
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
})


def to_rna(dna_strand: str) -> str:
    """Given a DNA strand, return transcribed RNA strand."""
    return dna_strand.translate(TRANSLATION)

