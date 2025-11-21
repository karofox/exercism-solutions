defmodule HighScore do
  @doc """
  Module for keeping track of the latest scores of our arcade game.
  """

  @default_score 0

  @spec new() :: %{}
  def new(), do: %{}

  @spec add_player(%{String.t() => integer()}, String.t(), integer()) :: %{String.t() => integer()}
  def add_player(scores, name, score \\ @default_score), do: Map.put_new(scores, name, score)

  @spec remove_player(%{String.t() => integer()}, String.t()) :: %{String.t() => integer()}
  def remove_player(scores, name), do: Map.delete(scores, name)

  @spec reset_score(%{String.t() => integer()}, String.t()) :: %{String.t() => integer()}
  def reset_score(scores, name), do: Map.put(scores, name, @default_score)

  @spec update_score(%{String.t() => integer()}, String.t(), integer()) :: %{String.t() => integer()}
  def update_score(scores, name, score), do: Map.update(scores, name, score, &(&1 + score))

  @spec get_players(%{String.t() => integer()}) :: [String.t()]
  def get_players(scores), do: Map.keys(scores)
end
