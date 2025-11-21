defmodule LogLevel do
  def to_label(level, legacy?) do
    case {level, legacy?} do
      {0, false} -> :trace
      {1, _} -> :debug
      {2, _} -> :info
      {3, _} -> :warning
      {4, _} -> :error
      {5, false} -> :fatal
      {_, _} -> :unknown
    end
  end

  def alert_recipient(level, legacy?) do
    result = to_label(level, legacy?)
    cond do
      result == :error or result == :fatal -> :ops
      result == :unknown and legacy? -> :dev1
      result == :unknown -> :dev2
      true -> false
    end
  end
end
