defmodule Username do
  @moduledoc """
  Manage German email usernames.
  """

  @allowed_chars ~c"abcdefghijklmnopqrstuvwxyz_äöüß"

  @spec sanitize(charlist()) :: charlist()
  def sanitize(username),
    do:
      username
      |> only_allowed()
      |> Enum.map(&substitute/1)
      |> Enum.concat()

  @spec only_allowed(charlist()) :: charlist()
  defp only_allowed(username),
    do:
      username
      |> Enum.filter(&(&1 in @allowed_chars))

  @spec substitute(char()) :: charlist()
  defp substitute(character) do
    case character do
      ?ä -> ~c"ae"
      ?ö -> ~c"oe"
      ?ü -> ~c"ue"
      ?ß -> ~c"ss"
      _ -> [character]
    end
  end
end
