"""RNA Transcription module."""

TRANSLATION = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand: str) -> str:
    """Given a DNA strand, return transcribed RNA strand."""
    return dna_strand.translate(TRANSLATION)

