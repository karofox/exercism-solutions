defmodule Username do
  @moduledoc """
  Manage German email usernames.
  """

  @allowed_chars ~c"abcdefghijklmnopqrstuvwxyz_"

  @spec sanitize(charlist()) :: charlist()
  def sanitize([]), do: ~c""
  def sanitize([?ä | rest]), do: [ ?a, ?e | sanitize(rest)] 
  def sanitize([?ö | rest]), do: [ ?o, ?e | sanitize(rest)]
  def sanitize([?ü | rest]), do: [ ?u, ?e | sanitize(rest)]
  def sanitize([?ß | rest]), do: [ ?s, ?s | sanitize(rest)]
  def sanitize([letter | rest]) when letter in @allowed_chars, do: [letter | sanitize(rest)]
  def sanitize([_letter | rest]), do: sanitize(rest)
end
