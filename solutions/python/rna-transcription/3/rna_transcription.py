"""RNA Transcription module."""

TRANSLATION = str.maketrans("GCTA", "CGAU")


def to_rna(dna_strand: str) -> str:
    """Given a DNA strand, return transcribed RNA strand."""
    if any(letter not in "ACGT" for letter in dna_strand):
        raise ValueError(f"{dna_strand=} is not a valid DNA strand.")
    return dna_strand.translate(TRANSLATION)
