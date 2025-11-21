defmodule RPG.CharacterSheet do
  @moduledoc """
  Helpers for creating a character sheet for RPG.
  """

  @spec welcome() :: :ok
  def welcome(), do: IO.puts("Welcome! Let's fill out your character sheet together.")

  @spec ask_name() :: String.t()
  def ask_name(), do: ask("What is your character's name?\n")

  @spec ask_class() :: String.t()
  def ask_class(), do: ask("What is your character's class?\n")

  @spec ask_level() :: integer()
  def ask_level(),
    do:
      ask("What is your character's level?\n")
      |> String.to_integer()

  @spec run() :: %{class: String.t(), level: integer(), name: String.t()}
  def run() do
    welcome()
    name = ask_name()
    class = ask_class()
    level = ask_level()
    character = %{class: class, level: level, name: name}
    IO.write("Your character: ")
    IO.inspect(character)
    character
  end

  @spec ask(String.t()) :: String.t()
  defp ask(prompt),
    do:
      IO.gets(prompt)
      |> String.trim()
end
