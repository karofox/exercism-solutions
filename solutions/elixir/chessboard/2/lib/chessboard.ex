defmodule Chessboard do
  @spec rank_range() :: Range.t()
  def rank_range, do: 1..8

  @spec file_range() :: Range.t()
  def file_range, do: ?A..?H

  @spec ranks() :: list(integer())
  def ranks, do: rank_range() |> Enum.to_list()

  @spec files() :: list(String.t())
  def files, do: file_range() |> Enum.into([], &<<&1>>)
end
