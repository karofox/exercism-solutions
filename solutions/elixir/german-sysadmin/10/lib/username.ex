defmodule Username do
  @moduledoc """
  Manage German email usernames.
  """

  @allowed_chars ~c"abcdefghijklmnopqrstuvwxyz_"

  @chars_and_replacements [
    {?ä, [?e, ?a]},
    {?ö, [?e, ?o]},
    {?ü, [?e, ?u]},
    {?ß, [?s, ?s]}
  ]

  @spec sanitize(charlist()) :: charlist()
  def sanitize(username), do: do_sanitize(username, ~c"")

  @spec do_sanitize(charlist(), charlist()) :: charlist()
  defp do_sanitize([], sanitized), do: sanitized |> Enum.reverse()

  Enum.each(@chars_and_replacements, fn {char, [repl1, repl2]} ->
    defp do_sanitize([unquote(char) | rest], sanitized),
      do: do_sanitize(rest, [unquote(repl1), unquote(repl2) | sanitized])
  end)

  defp do_sanitize([letter | rest], sanitized) when letter in @allowed_chars,
    do: do_sanitize(rest, [letter | sanitized])

  defp do_sanitize([_letter | rest], sanitized), do: do_sanitize(rest, sanitized)
end
