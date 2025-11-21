defmodule Username do
  @moduledoc """
  Manage German email usernames.
  """

  @sanitized_chars [
    {?ä, ~c"ae"},
    {?ö, ~c"oe"},
    {?ü, ~c"ue"},
    {?ß, ~c"ss"}
    | Enum.map(
        ~c"abcdefghijklmnopqrstuvwxyz_",
        &{&1, &1}
      )
  ]

  @spec sanitize(charlist()) :: charlist()
  def sanitize(username), do: do_sanitize(username, ~c"")

  @spec do_sanitize(charlist(), charlist()) :: charlist()
  defp do_sanitize([], sanitized), do: sanitized |> Enum.reverse()

  Enum.each(@sanitized_chars, fn
    {char, [repl1, repl2]} ->
      defp do_sanitize([unquote(char) | rest], sanitized),
        do: do_sanitize(rest, [unquote(repl2), unquote(repl1) | sanitized])

    {char, repl} ->
      defp do_sanitize([unquote(char) | rest], sanitized),
        do: do_sanitize(rest, [unquote(repl) | sanitized])
  end)

  defp do_sanitize([_letter | rest], sanitized), do: do_sanitize(rest, sanitized)
end
