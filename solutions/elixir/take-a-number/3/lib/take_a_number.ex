defmodule TakeANumber do
  @moduledoc """
  Take-A-Number machine embedded system.
  """

  @spec start() :: pid()
  def start(), do: spawn(&loop/0)

  @spec loop(integer()) :: integer()
  defp loop(last_number \\ 0) do
    receive do
      {:report_state, sender_pid} -> 
        send(sender_pid, last_number)
        loop(last_number)
      {:take_a_number, sender_pid} -> 
        send(sender_pid, last_number + 1)
        loop(last_number + 1)
      :stop -> last_number
      _ -> loop(last_number)
    end
  end
end
