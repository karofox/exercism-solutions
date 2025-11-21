defmodule NameBadge do
  @moduledoc """
  Print name badge for factory employees.
  """

  @spec print(integer(), String.t(), String.t()) :: String.t()
  def print(id, name, department),
    do:
      if(id, do: "[#{id}] - ", else: "") <>
        name <>
        " - " <>
        if(department, do: String.upcase(department), else: "OWNER")
end
