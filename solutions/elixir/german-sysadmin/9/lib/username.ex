defmodule Username do
  @moduledoc """
  Manage German email usernames.
  """

  @allowed_chars ~c"abcdefghijklmnopqrstuvwxyz_"

  @spec sanitize(charlist()) :: charlist()
  def sanitize(username), do: do_sanitize(username, ~c"")

  @spec do_sanitize(charlist(), charlist()) :: charlist()
  defp do_sanitize([], sanitized), do: sanitized |> Enum.reverse()
  defp do_sanitize([?ä | rest], sanitized), do: do_sanitize(rest, [?e, ?a | sanitized])
  defp do_sanitize([?ö | rest], sanitized), do: do_sanitize(rest, [?e, ?o | sanitized])
  defp do_sanitize([?ü | rest], sanitized), do: do_sanitize(rest, [?e, ?u | sanitized])
  defp do_sanitize([?ß | rest], sanitized), do: do_sanitize(rest, [?s, ?s | sanitized])
  defp do_sanitize([letter | rest], sanitized) when letter in @allowed_chars,
    do: do_sanitize(rest, [letter | sanitized])
  defp do_sanitize([_letter | rest], sanitized), do: do_sanitize(rest, sanitized)
end
