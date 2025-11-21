defmodule NameBadge do
  @moduledoc """
  Print name badge for factory employees.
  """

  @spec print(integer(), String.t(), String.t()) :: String.t()
  def print(id, name, department),
    do: "#{print_id(id)}#{name} - #{print_department(department)}"

  @spec print_id(integer() | nil) :: String.t()
  defp print_id(id), do:
    if(id, do: "[#{id}] - ", else: "")

  @spec print_department(Stirng.t() | nil) :: String.t()
  defp print_department(department), do:
    if(department, do: String.upcase(department), else: "OWNER")
end
