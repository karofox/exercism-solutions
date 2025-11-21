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
  Enum.each(@nucleotides_and_codes, fn {nucleotide, code} ->
    defp do_encode([unquote(nucleotide) | rest], encoded),
      do: do_encode(rest, <<encoded::bitstring, unquote(code)::4>>)
  end)

  defp do_encode([], encoded), do: encoded

  @spec decode(bitstring()) :: charlist()
  def decode(dna), do: do_decode(dna, ~c"")

  @spec do_decode(bitstring(), charlist()) :: charlist()
  Enum.each(@nucleotides_and_codes, fn {nucleotide, code} ->
    defp do_decode(<<unquote(code)::4, rest::bitstring>>, decoded),
      do: do_decode(rest, [unquote(nucleotide) | decoded])
  end)

  defp do_decode(<<>>, decoded), do: decoded |> reverse()

  @spec reverse([any()]) :: [any()]
  defp reverse(enumerable), do: do_reverse(enumerable, [])

  @spec do_reverse([any()], [any()]) :: [any()]
  defp do_reverse([head | tail], reversed), do: do_reverse(tail, [head | reversed])
  defp do_reverse([], reversed), do: reversed
end
