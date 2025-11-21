defmodule LanguageList do
  @doc"""
  List operations.
  """

  @spec new :: list()
  def new(), do: []

  @spec add(list(), String.t()) :: list()
  def add(list, language), do: [language | list]

  @spec remove(list()) :: list()
  def remove(list), do: tl(list)

  @spec first(list()) :: String.t()
  def first(list), do: hd(list)

  @spec count(list()) :: integer()
  def count(list), do: length(list)

  @spec functional_list?(list()) :: boolean()
  def functional_list?(list), do: "Elixir" in list
end
