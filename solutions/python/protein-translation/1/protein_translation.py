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
        protein = strand[idx : idx + 3]

        if protein not in CODONS:
            raise ValueError(f"{protein=} is not a valid protein.")
        if CODONS[protein] == "STOP":
            return protein_list

        protein_list.append(CODONS[protein])
    return protein_list
