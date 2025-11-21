defmodule BoutiqueInventory do
  @type item :: %{
          price: non_neg_integer(),
          name: String.t(),
          quantity_by_size: %{
            s: non_neg_integer(),
            m: non_neg_integer(),
            l: non_neg_integer(),
            xl: non_neg_integer()
          }
        }

  @spec sort_by_price([item()]) :: [item()]
  def sort_by_price(inventory), do: inventory |> Enum.sort_by(&(&1[:price]))

  @spec with_missing_price([item()]) :: [item()]
  def with_missing_price(inventory), do: inventory |> Enum.filter(&(&1[:price] == nil))

  @spec update_names([item()], String.t(), String.t()) :: [item()]
  def update_names(inventory, old_word, new_word),
    do:
      inventory
      |> Enum.map(
        &(&1
          |> Map.update(:name, nil, fn name -> name |> String.replace(old_word, new_word) end))
      )

  @spec increase_quantity(item(), integer()) :: item()
  def increase_quantity(item, count),
    do:
      item
      |> Map.update(
        :quantity_by_size,
        nil,
        &(&1 |> Enum.map(fn {size, quantity} -> {size, quantity + count} end) |> Map.new())
      )

  @spec total_quantity(item()) :: integer()
  def total_quantity(item),
    do:
      item[:quantity_by_size]
      |> Enum.reduce(0, fn {_size, quantity}, total -> quantity + total end)
end
