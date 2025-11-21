"""Protein translation module"""

from typing import Iterator



def proteins(strand: str) -> list[str]:
    """Translates RNA strands into a list of proteins."""
    protein_generator = ProteinGenerator(strand)

    return [protein for protein in protein_generator]


class ProteinGenerator:
    CODON_LEN = 3

    def __init__(self, strand: str) -> None:
        self.strand = strand
        if len(self.strand) % self.CODON_LEN != 0:
            raise ValueError(f"{strand=} is not a valid strand.")
        self._idx = 0

    def __iter__(self):
        return self
    
    def __next__(self) -> Iterator[str]:
        codon = self._get_next_codon()
        if (protein := self._get_protein(codon)) != "STOP":
            self._idx += self.CODON_LEN
            return protein
        raise StopIteration

    def _get_next_codon(self) -> str:
        """Returns next codon based on current self._idx."""
        return self.strand[self._idx : self._idx + self.CODON_LEN]

    def _get_protein(self, codon: str) -> str:
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
            case "UAA" | "UAG" | "UGA" | "":
                return "STOP"
            case _:
                raise ValueError(f"{codon=} is not a valid codon")
