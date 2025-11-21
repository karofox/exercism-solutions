defmodule Username do
  @moduledoc """
  Manage German email usernames.
  """

  @allowed_chars ~c"abcdefghijklmnopqrstuvwxyz_"

  @spec sanitize(charlist()) :: charlist()
  # def sanitize([]), do: ~c""
  # def sanitize([?ä | rest]), do: [?a, ?e | sanitize(rest)]
  # def sanitize([?ö | rest]), do: [?o, ?e | sanitize(rest)]
  # def sanitize([?ü | rest]), do: [?u, ?e | sanitize(rest)]
  # def sanitize([?ß | rest]), do: [?s, ?s | sanitize(rest)]
  # def sanitize([letter | rest]) when letter in @allowed_chars, do: [letter | sanitize(rest)]
  # def sanitize([_letter | rest]), do: sanitize(rest)

  def sanitize(username), do: do_sanitize(username, ~c"")

  defp do_sanitize([], sanitized), do: sanitized
  defp do_sanitize([?ä | rest], sanitized), do: do_sanitize(rest, [?a, ?e | sanitized])
  defp do_sanitize([?ö | rest], sanitized), do: do_sanitize(rest, [?o, ?e | sanitized])
  defp do_sanitize([?ü | rest], sanitized), do: do_sanitize(rest, [?u, ?e | sanitized])
  defp do_sanitize([?ß | rest], sanitized), do: do_sanitize(rest, [?s, ?s | sanitized])
  defp do_sanitize([letetr | rest], sanitized) when letter in @allowed_chars,
    do: do_sanitize(rest, [letter | sanitized])
  defp do_sanitize([_letter | rest], sanitized), do: do_sanitize(rest, sanitized)
end
