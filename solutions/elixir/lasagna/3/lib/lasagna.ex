defmodule Lasagna do
  @doc """
  Cooking a lasagna
  """

  @layer_prep_time 2
  @lasagna_cooking 40

  @spec expected_minutes_in_oven :: integer()
  def expected_minutes_in_oven, do: @lasagna_cooking

  @spec remaining_minutes_in_oven(integer()) :: integer()
  def remaining_minutes_in_oven(in_oven), do: expected_minutes_in_oven() - in_oven

  @spec preparation_time_in_minutes(integer()) :: integer()
  def preparation_time_in_minutes(layers), do: layers * @layer_prep_time

  @spec total_time_in_minutes(integer(), integer()) :: integer()
  def total_time_in_minutes(layers, in_oven), do: preparation_time_in_minutes(layers) + in_oven

  @spec alarm :: String.t()
  def alarm, do: "Ding!"
end
