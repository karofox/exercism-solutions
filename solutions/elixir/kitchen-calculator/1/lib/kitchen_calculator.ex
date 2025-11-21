defmodule KitchenCalculator do
  @doc """
  Conversion of volume units.
  """
  @spec get_volume({:atom, float()}) :: float()
  def get_volume({_, volume}), do: volume

  @spec to_milliliter({:atom, float()}) :: {:atom, float()}
  def to_milliliter({:cup, volume}), do: {:milliliter, 240 * volume}
  def to_milliliter({:fluid_ounce, volume}), do: {:milliliter, 30 * volume}
  def to_milliliter({:teaspoon, volume}), do: {:milliliter, 5 * volume}
  def to_milliliter({:tablespoon, volume}), do: {:milliliter, 15 * volume}
  def to_milliliter({:milliliter, volume}), do: {:milliliter, volume}

  @spec from_milliliter({:atom, float()}, :atom) :: {:atom, float()}
  def from_milliliter({_, volume}, :cup), do: {:cup, volume / 240}
  def from_milliliter({_, volume}, :fluid_ounce), do: {:fluid_ounce, volume / 30}
  def from_milliliter({_, volume}, :teaspoon), do: {:teaspoon, volume / 5}
  def from_milliliter({_, volume}, :tablespoon), do: {:tablespoon, volume / 15}
  def from_milliliter({_, volume}, :milliliter), do: {:milliliter, volume}

  @spec convert({:atom, float()}, :atom) :: {:atom, float()}
  def convert(volume_pair, unit), do: to_milliliter(volume_pair) |> from_milliliter(unit)
end
