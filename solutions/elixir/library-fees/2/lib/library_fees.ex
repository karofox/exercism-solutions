defmodule LibraryFees do
  @moduledoc """
  Helper functions for maintainance of library fees.
  """

  @spec datetime_from_string(String.t()) :: NaiveDateTime.t()
  def datetime_from_string(datetime), do: NaiveDateTime.from_iso8601(datetime) |> elem(1)

  @spec before_noon?(NaiveDateTime.t()) :: boolean()
  def before_noon?(checkout_datetime), do: checkout_datetime.hour < 12

  @spec return_date(NaiveDateTime.t()) :: Date.t()
  def return_date(checkout_datetime),
    do:
      checkout_datetime
      |> NaiveDateTime.add(if(before_noon?(checkout_datetime), do: 28, else: 29), :day)
      |> NaiveDateTime.to_date()

  @spec days_late(NaiveDateTime.t(), Date.t()) :: non_neg_integer()
  def days_late(planned_return_date, actual_return_datetime),
    do:
      actual_return_datetime
      |> NaiveDateTime.to_date()
      |> Date.diff(planned_return_date)
      |> max(0)

  @spec monday?(NaiveDateTime.t()) :: boolean()
  def monday?(datetime), do: datetime |> NaiveDateTime.to_date() |> Date.day_of_week() == 1

  @spec calculate_late_fee(String.t(), String.t(), non_neg_integer()) :: non_neg_integer()
  def calculate_late_fee(checkout, return, rate),
    do:
      ((checkout
        |> datetime_from_string()
        |> return_date()
        |> days_late(return |> datetime_from_string())) * rate *
         if(monday?(return |> datetime_from_string()), do: 0.5, else: 1))
      |> trunc()
end
