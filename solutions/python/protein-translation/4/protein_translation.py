"""Protein translation module"""

CODON_LEN = 3


def proteins(strand: str) -> list[str]:
    """Translates RNA strands into a list of proteins."""
    if len(strand) % CODON_LEN != 0:
        raise ValueError(f"{strand=} is not a valid strand.")

    return [protein for protein in proteins_from_strand(strand)]


def proteins_from_strand(strand: str) -> str:
    """Yields proteins from a strand."""
    for protein in (
        get_protein(strand[pos : pos + CODON_LEN])
        for pos in range(0, len(strand), CODON_LEN)
    ):
        if protein == "STOP":
            return
        yield protein


def get_protein(codon: str) -> str:
    """Returns the protein coded by the codon."""
    match codon:
        case "AUG":
            return "Methionine"
        case "UUU" | "UUC":
            return "Phenylalanine"
        case "UUA" | "UUG":
            return "Leucine"
        case "UCU" | "UCC" | "UCA" | "UCG":
            return "Serine"
        case "UAU" | "UAC":
            return "Tyrosine"
        case "UGU" | "UGC":
            return "Cysteine"
        case "UGG":
            return "Tryptophan"
        case "UAA" | "UAG" | "UGA":
            return "STOP"
        case _:
            raise ValueError(f"{codon=} is not a valid codon")
