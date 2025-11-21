defmodule DNA do
  @spec encode_nucleotide(integer()) :: integer()
  def encode_nucleotide(?A), do: 0b0001
  def encode_nucleotide(?C), do: 0b0010
  def encode_nucleotide(?G), do: 0b0100
  def encode_nucleotide(?T), do: 0b1000
  def encode_nucleotide(?\s), do: 0b0000

  @spec decode_nucleotide(integer()) :: integer()
  def decode_nucleotide(0b0001), do: ?A
  def decode_nucleotide(0b0010), do: ?C
  def decode_nucleotide(0b0100), do: ?G
  def decode_nucleotide(0b1000), do: ?T
  def decode_nucleotide(0b0000), do: ?\s

  @spec encode(charlist()) :: bitstring()
  def encode(dna), do: do_encode(dna, <<>>)

  @spec do_encode(charlist(), bitstring()) :: bitstring()
  defp do_encode([], encoded), do: encoded
  defp do_encode([nucleotide | rest], encoded),
    do: do_encode(rest, <<encoded::bitstring, encode_nucleotide(nucleotide)::4>>)

  @spec decode(bitstring()) :: charlist()
  def decode(dna), do: do_decode(dna, ~c"")

  @spec do_decode(bitstring(), charlist()) :: charlist()
  defp do_decode(<<>>, decoded), do: decoded
  defp do_decode(<<nucleotide::4, rest::bitstring>>, decoded),
    do: do_decode(rest, decoded ++ [decode_nucleotide(nucleotide)])
end
