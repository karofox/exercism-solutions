defmodule KitchenCalculator do
  @doc """
  Conversion of volume units.
  """
  @milliliters_per_cup 240
  @milliliters_per_fluid_ounce 30
  @milliliters_per_teaspoon 5
  @milliliters_per_tablespoon 15

  @spec get_volume({:atom, float()}) :: float()
  def get_volume({_, volume}), do: volume

  @spec to_milliliter({:atom, float()}) :: {:atom, float()}
  def to_milliliter({:cup, cups}), do: {:milliliter, @milliliters_per_cup * cups}
  def to_milliliter({:fluid_ounce, fluid_ounces}), do: {:milliliter, @milliliters_per_fluid_ounce * fluid_ounces}
  def to_milliliter({:teaspoon, teaspoons}), do: {:milliliter, @milliliters_per_teaspoon * teaspoons}
  def to_milliliter({:tablespoon, tablespoons}), do: {:milliliter, @milliliters_per_tablespoon * tablespoons}
  def to_milliliter({:milliliter, milliliters}), do: {:milliliter, milliliters}

  @spec from_milliliter({:atom, float()}, :atom) :: {:atom, float()}
  def from_milliliter({:milliliter, milliliters}, :cup), do: {:cup, milliliters / @milliliters_per_cup}
  def from_milliliter({:milliliter, milliliters}, :fluid_ounce), do: {:fluid_ounce, milliliters / @milliliters_per_fluid_ounce}
  def from_milliliter({:milliliter, milliliters}, :teaspoon), do: {:teaspoon, milliliters / @milliliters_per_teaspoon}
  def from_milliliter({:milliliter, milliliters}, :tablespoon), do: {:tablespoon, milliliters / @milliliters_per_tablespoon}
  def from_milliliter({:milliliter, milliliters}, :milliliter), do: {:milliliter, milliliters}

  @spec convert({:atom, float()}, :atom) :: {:atom, float()}
  def convert(volume, unit) when unit == elem(volume, 0), do: volume
  def convert(volume, unit), do: from_milliliter(to_milliliter(volume), unit)
end
