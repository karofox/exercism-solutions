defmodule LanguageList do
  @doc """
  List operations.
  """
  require Enum

  @functional_languages ["Clojure", "Haskell", "Erlang", "Elixir", "F#"]

  @spec new :: list()
  def new(), do: []

  @spec add(list(String.t()), String.t()) :: list(String.t())
  def add(languages, language), do: [language | languages]

  @spec remove(nonempty_list(String.t())) :: list(String.t())
  def remove([_first_elem | rest]), do: rest

  @spec first(nonempty_list(String.t())) :: String.t()
  def first([first_elem | _rest]), do: first_elem

  @spec count(list(String.t())) :: integer()
  def count(languages), do: length(languages)

  @spec functional_list?(list(String.t())) :: boolean()
  def functional_list?(languages),
    do: Enum.any?(languages, fn l -> Enum.member?(@functional_languages, l) end)
end
