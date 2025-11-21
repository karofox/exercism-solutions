defmodule Username do
  @moduledoc """
  Manage German email usernames.
  """

  @allowed_chars ~c"abcdefghijklmnopqrstuvwxyz_"

  @spec sanitize(charlist()) :: charlist()
  def sanitize([]), do: ~c""
  def sanitize([letter | rest]) when letter == ?ä, do: ~c"ae" ++ sanitize(rest)
  def sanitize([letter | rest]) when letter == ?ö, do: ~c"oe" ++ sanitize(rest)
  def sanitize([letter | rest]) when letter == ?ü, do: ~c"ue" ++ sanitize(rest)
  def sanitize([letter | rest]) when letter == ?ß, do: ~c"ss" ++ sanitize(rest)
  def sanitize([letter | rest]) when letter in @allowed_chars, do: [letter] ++ sanitize(rest)
  def sanitize([latter | rest]), do: sanitize(rest)
end
