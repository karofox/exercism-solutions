defmodule Username do
  @moduledoc """
  Manage German email usernames.
  """

  @allowed_chars ~c"abcdefghijklmnopqrstuvwxyz_äöüß"

  @spec sanitize(charlist()) :: charlist()
  def sanitize(username),
    do:
      username
      |> only_lowercase()
      |> Enum.map_join(&substitute/1)
      |> to_charlist()

  @spec only_lowercase(charlist()) :: charlist()
  defp only_lowercase(username),
    do:
      username
      |> Enum.filter(&(&1 in @allowed_chars))

  @spec substitute(char()) :: charlist()
  defp substitute(char) do
    case char do
      ?ä -> ~c"ae"
      ?ö -> ~c"oe"
      ?ü -> ~c"ue"
      ?ß -> ~c"ss"
      _ -> [char]
    end
  end
end
