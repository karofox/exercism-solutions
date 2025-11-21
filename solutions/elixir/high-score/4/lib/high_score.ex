defmodule HighScore do
  @doc """
  Module for keeping track of the latest scores of our arcade game.
  """

  @initial_score 0

  @spec new() :: %{}
  def new(), do: %{}

  @spec add_player(%{String.t() => integer()}, String.t(), integer()) :: %{String.t() => integer()}
  def add_player(score_by_name, name, score \\ @initial_score),
    do: Map.put_new(score_by_name, name, score)

  @spec remove_player(%{String.t() => integer()}, String.t()) :: %{String.t() => integer()}
  def remove_player(score_by_name, name), do: Map.delete(score_by_name, name)

  @spec reset_score(%{String.t() => integer()}, String.t()) :: %{String.t() => integer()}
  def reset_score(score_by_name, name), do: Map.put(score_by_name, name, @initial_score)

  @spec update_score(%{String.t() => integer()}, String.t(), integer()) :: %{String.t() => integer()}
  def update_score(score_by_name, name, additional_score),
    do: Map.update(score_by_name, name, additional_score, &(&1 + additional_score))

  @spec get_players(%{String.t() => integer()}) :: [String.t()]
  def get_players(score_by_name), do: Map.keys(score_by_name)
end
