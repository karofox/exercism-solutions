defmodule HighSchoolSweetheart do
  @doc """
  Helping High School Sweathearts profess their love.
  """

  @spec first_letter(String.t()) :: String.t()
  def first_letter(name), do: String.trim(name) |> String.first()

  @spec initial(String.t()) :: String.t()
  def initial(name), do: first_letter(name) |> String.capitalize() |> Kernel.<>(".")

  @spec initials(String.t()) :: String.t()
  def initials(full_name), do: String.split(full_name) |> Enum.map(&initial/1) |> Enum.join(" ")

  @spec pair(String.t(), String.t()) :: String.t()
  def pair(full_name1, full_name2),
    do: """
         ******       ******
       **      **   **      **
     **         ** **         **
    **            *            **
    **                         **
    **     #{initials(full_name1)}  +  #{initials(full_name2)}     **
     **                       **
       **                   **
         **               **
           **           **
             **       **
               **   **
                 ***
                  *
    """
end
