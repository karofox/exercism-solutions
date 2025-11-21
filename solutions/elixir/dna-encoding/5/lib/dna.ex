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
  def encode(dna), do: codes(dna, <<>>)

  @spec codes(charlist(), bitstring()) :: bitstring()
  Enum.each(@nucleotides_and_codes, fn {nucleotide, code} ->
    defp codes([unquote(nucleotide) | rest], encoded),
      do: codes(rest, <<encoded::bitstring, unquote(code)::4>>)
  end)

  defp codes([], encoded), do: encoded

  @spec decode(bitstring()) :: charlist()
  def decode(dna), do: nucleotides(dna, ~c"")

  @spec nucleotides(bitstring(), charlist()) :: charlist()
  Enum.each(@nucleotides_and_codes, fn {nucleotide, code} ->
    defp nucleotides(<<unquote(code)::4, rest::bitstring>>, decoded),
      do: nucleotides(rest, [unquote(nucleotide) | decoded])
  end)

  defp nucleotides(<<>>, decoded), do: decoded |> reverse()

  @spec reverse([any()]) :: [any()]
  defp reverse(enumerable), do: reverse(enumerable, [])

  @spec reverse([any()], [any()]) :: [any()]
  defp reverse([head | tail], reversed), do: reverse(tail, [head | reversed])
  defp reverse([], reversed), do: reversed
end
