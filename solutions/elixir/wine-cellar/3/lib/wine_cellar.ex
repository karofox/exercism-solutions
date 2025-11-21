defmodule WineCellar do
  @moduledoc """
  Helps with wine selection process.
  """

  @type wine() :: {String.t(), integer(), String.t()}

  @doc """
  Returns a keyword list with descriptions of wine colors.
  """
  @spec explain_colors() :: [white: String.t(), red: String.t(), rose: String.t()]
  def explain_colors,
    do: [
      white: "Fermented without skin contact.",
      red: "Fermented with skin contact using dark-colored grapes.",
      rose: "Fermented with some skin contact, but not enough to qualify as a red wine."
    ]

  @doc """
  Filters the wines by color, then optionally by the year and/or a country.
  """
  @spec filter([white: wine(), red: wine(), rose: wine()], :red | :white | :rose, [
          {atom(), any()}
        ]) :: [wine()]
  def filter(cellar, color, opts \\ []),
    do: cellar |> Keyword.get_values(color) |> do_filter(opts)

  @doc """
  Filters the wine lists based on the provided filters.
  """
  @spec do_filter([wine()], [{atom(), any()}]) :: [wine()]
  defp do_filter(wines, []), do: wines
  defp do_filter(wines, [{:year, year} | more]),
    do: wines |> filter_by_year(year) |> do_filter(more)
  defp do_filter(wines, [{:country, country} | more]),
    do: wines |> filter_by_country(country) |> do_filter(more)

  # The functions below do not need to be modified.

  defp filter_by_year(wines, year)
  defp filter_by_year([], _year), do: []

  defp filter_by_year([{_, year, _} = wine | tail], year) do
    [wine | filter_by_year(tail, year)]
  end

  defp filter_by_year([{_, _, _} | tail], year) do
    filter_by_year(tail, year)
  end

  defp filter_by_country(wines, country)
  defp filter_by_country([], _country), do: []

  defp filter_by_country([{_, _, country} = wine | tail], country) do
    [wine | filter_by_country(tail, country)]
  end

  defp filter_by_country([{_, _, _} | tail], country) do
    filter_by_country(tail, country)
  end
end
