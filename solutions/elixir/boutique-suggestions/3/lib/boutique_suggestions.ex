defmodule BoutiqueSuggestions do
  @type clothing_item :: %{
          item_name: String.t(),
          price: float(),
          base_color: String.t()
        }

  @spec get_combinations([clothing_item()], [clothing_item()], Keyword.t()) :: [
          {clothing_item(), clothing_item()}
        ]
  def get_combinations(tops, bottoms, options \\ []),
    do:
      for(
        top <- tops,
        bottom <- bottoms,
        top[:base_color] != bottom[:base_color] &&
          top[:price] + bottom[:price] <= Keyword.get(options, :maximum_price, 100.00),
        do: {top, bottom}
      )
end
