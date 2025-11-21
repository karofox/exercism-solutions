defmodule BasketballWebsite do
  @spec extract_from_path(map(), String.t()) :: any()
  def extract_from_path(data, path),
    do:
      path
      |> String.split(".")
      |> Enum.reduce(data, fn key, acc -> acc[key] end)

  @spec get_in_path(map(), String.t()) :: any()
  def get_in_path(data, path), do: 
    data 
    |> get_in(String.split(path, "."))
end
