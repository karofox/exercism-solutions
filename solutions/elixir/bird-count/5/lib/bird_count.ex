defmodule BirdCount do
  @doc """
  Bird counting helper functions.
  """

  @spec today(list(integer())) :: integer()
  def today([]), do: nil
  def today([count | _rest]), do: count

  @spec increment_day_count(list(integer())) :: list(integer())
  def increment_day_count([]), do: [1]
  def increment_day_count([today | rest]), do: [today + 1 | rest]

  @spec has_day_without_birds?(list(integer())) :: boolean()
  def has_day_without_birds?(list), do: 0 in list

  @spec total(list(integer())) :: integer()
  def total([]), do: 0
  def total([day | rest]), do: day + total(rest)

  @spec busy_days(list(integer())) :: integer()
  def busy_days([]), do: 0
  def busy_days([day | rest]) when day >= 5, do: 1 + busy_days(rest)
  def busy_days([_day | rest]), do: busy_days(rest)
end
