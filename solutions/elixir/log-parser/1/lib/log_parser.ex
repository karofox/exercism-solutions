defmodule LogParser do
  @moduledoc """
  Helper functions for log parsing.
  """

  @line_validation_re ~r/^\[(DEBUG|INFO|WARNING|ERROR)\]/
  @split_re ~r/<[~*=-]*>/
  @sanitize_re ~r/end-of-line\d+/i
  @username_re ~r/User\s+(\S+)/u

  @spec valid_line?(String.t()) :: boolean()
  def valid_line?(line), do: line =~ @line_validation_re

  @spec split_line(String.t()) :: [String.t()]
  def split_line(line), do: Regex.split(@split_re, line)

  @spec remove_artifacts(String.t()) :: String.t()
  def remove_artifacts(line), do: Regex.replace(@sanitize_re, line, "")

  @spec tag_with_user_name(String.t()) :: String.t()
  def tag_with_user_name(line),
    do:
      if(line =~ @username_re,
        do: "[USER] " <> Enum.at(Regex.run(@username_re, line), 1) <> " " <> line,
        else: line
      )
end
