defmodule NameBadge do
  @moduledoc """
  Print name badge for factory employees.
  """

  @spec print(integer(), String.t(), String.t()) :: String.t()
  def print(nil, name, nil),
    do: "#{name} - OWNER"
  def print(nil, name, department),
    do: "#{name} - #{String.upcase(department)}"
  def print(id, name, nil),
    do: "[#{id}] - #{name} - OWNER"
  def print(id, name, department),
    do: "[#{id}] - #{name} - #{String.upcase(department)}"
end
