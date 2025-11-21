defmodule FreelancerRates do
  @doc"""
  Freelancer rates helper functions.
  """

  @daily_rate_mult 8.0
  @billable_days 22

  @spec daily_rate(integer()) :: float()
  def daily_rate(hourly_rate), do: hourly_rate * @daily_rate_mult

  @spec apply_discount(integer(), float()) :: float()
  def apply_discount(before_discount, discount) do
    before_discount * (100 - discount) / 100
  end

  @spec monthly_rate(integer(), float()) :: float()
  def monthly_rate(hourly_rate, discount) do
    daily_rate(hourly_rate) * @billable_days
    |> apply_discount(discount)
    |> ceil
  end

  @spec days_in_budget(integer(), integer(), float()) :: float()
  def days_in_budget(budget, hourly_rate, discount) do
    Float.floor(budget / apply_discount(daily_rate(hourly_rate), discount), 1)
  end
end
