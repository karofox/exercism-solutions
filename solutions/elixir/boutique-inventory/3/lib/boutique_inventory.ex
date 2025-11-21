defmodule BoutiqueInventory do
  import Map, only: [update: 4, new: 1, values: 1]
  import Enum, only: [sort_by: 2, reject: 2, map: 2, sum: 1]

  @type item :: %{
          price: non_neg_integer(),
          name: String.t(),
          quantity_by_size: map()
        }

  @spec sort_by_price([item()]) :: [item()]
  def sort_by_price(inventory), do: inventory |> sort_by(& &1[:price])

  @spec with_missing_price([item()]) :: [item()]
  def with_missing_price(inventory), do: inventory |> reject(& &1[:price])

  @spec update_names([item()], String.t(), String.t()) :: [item()]
  def update_names(inventory, old_word, new_word),
    do: inventory |> map(&update_name(&1, old_word, new_word))

  @spec update_name(item(), String.t(), String.t()) :: item()
  defp update_name(item, old_word, new_word),
    do: item |> update(:name, "", &String.replace(&1, old_word, new_word))

  @spec increase_quantity(item(), integer()) :: item()
  def increase_quantity(item, amount),
    do: item |> update(:quantity_by_size, %{}, &update_quantity(&1, amount))

  @spec update_quantity(map(), integer()) :: map()
  defp update_quantity(quantity_by_size, amount),
    do:
      quantity_by_size
      |> map(fn {size, quantity} -> {size, quantity + amount} end)
      |> new()

  @spec total_quantity(item()) :: integer()
  def total_quantity(%{quantity_by_size: qbs}),
    do: sum(values(qbs))
end
