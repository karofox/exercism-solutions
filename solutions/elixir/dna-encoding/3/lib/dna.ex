defmodule DNA do
  @nucleotides_and_codes [
    {?A, 0b0001},
    {?C, 0b0010},
    {?G, 0b0100},
    {?T, 0b1000},
    {?\s, 0b0000}
  ]

  @spec encode_nucleotide(integer()) :: integer()
  Enum.each(@nucleotides_and_codes, fn {nucleotide, code} ->
    def encode_nucleotide(unquote(nucleotide)), do: unquote(code)
  end)

  @spec decode_nucleotide(integer()) :: integer()
  Enum.each(@nucleotides_and_codes, fn {nucleotide, code} ->
    def decode_nucleotide(unquote(code)), do: unquote(nucleotide)
  end)

  @spec encode(charlist()) :: bitstring()
  def encode(dna), do: do_encode(dna, <<>>)

  @spec do_encode(charlist(), bitstring()) :: bitstring()
  defp do_encode([], encoded), do: encoded

  Enum.each(@nucleotides_and_codes, fn {nucleotide, code} ->
    defp do_encode([unquote(nucleotide) | rest], encoded),
      do: do_encode(rest, <<encoded::bitstring, unquote(code)::4>>)
  end)

  @spec decode(bitstring()) :: charlist()
  def decode(dna), do: do_decode(dna, ~c"")

  @spec do_decode(bitstring(), charlist()) :: charlist()
  defp do_decode(<<>>, decoded), do: decoded |> Enum.reverse()

  Enum.each(@nucleotides_and_codes, fn {nucleotide, code} ->
    defp do_decode(<<unquote(code)::4, rest::bitstring>>, decoded),
      do: do_decode(rest, [unquote(nucleotide) | decoded])
  end)
end
