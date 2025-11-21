defmodule TakeANumber do
  @moduledoc """
  Take-A-Number machine embedded system.
  """

  @spec start() :: pid()
  def start(), do: spawn(&loop/0)

  @spec loop(integer()) :: integer()
  defp loop(state \\ 0) do
    receive do
      {:report_state, sender_pid} -> 
        send(sender_pid, state)
        loop(state)
      {:take_a_number, sender_pid} -> 
        send(sender_pid, state + 1)
        loop(state + 1)
      :stop -> state
      _ -> loop(state)
    end
  end
end
