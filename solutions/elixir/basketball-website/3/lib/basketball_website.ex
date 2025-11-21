defmodule BasketballWebsite do
  @spec extract_from_path(map(), String.t()) :: any()
  def extract_from_path(data, path), do: do_extract_from_path(data, String.split(path, "."))

  @spec do_extract_from_path(any(), [String.t()]) :: any()
  def do_extract_from_path(data, []), do: data
  def do_extract_from_path(data, [elem | rest]), do: do_extract_from_path(data[elem], rest)

  @spec get_in_path(map(), String.t()) :: any()
  def get_in_path(data, path),
    do:
      data
      |> get_in(String.split(path, "."))
end
