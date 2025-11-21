"""Protein translation module"""


def proteins(strand: str) -> list[str]:
    """Translates RNA strands into a list of proteins."""
    protein_list = []
    if len(strand) % 3 != 0:
        raise ValueError(f"{strand=} is not a valid strand.")

    return [protein for protein in proteins_from_strand(strand)]


def proteins_from_strand(strand: str) -> str:
    """Yields proteins from a strand."""
    idx = 0
    codon = strand[idx : idx + 3]
    while idx <= len(strand) - 3 and (protein := get_protein(codon)) != "STOP":
        yield protein
        idx += 3
        codon = strand[idx : idx + 3]


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
