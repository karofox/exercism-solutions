"""Protein translation module"""

CODONS = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}


def proteins(strand: str) -> list[str]:
    """Translates RNA strands into a list of proteins."""
    protein_list = []
    if len(strand) % 3 != 0:
        raise ValueError(f"{strand=} is not a valid strand.")

    for idx in range(0, len(strand), 3):
        codon = strand[idx : idx + 3]
        protein = get_protein(codon)
        if protein == "STOP":
            return protein_list
        protein_list.append(protein)
    return protein_list

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