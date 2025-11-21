defmodule Newsletter do
  @moduledoc """
  Module for newsletter management.
  """

  @spec read_emails(Path.t()) :: [String.t()]
  def read_emails(path), do: File.read!(path) |> String.split("\n") |> Enum.filter(&(&1 != ""))

  @spec open_log(Path.t()) :: pid()
  def open_log(path), do: File.open!(path, [:write])

  @spec log_sent_email(pid(), String.t()) :: :ok
  def log_sent_email(pid, email), do: IO.puts(pid, email)

  @spec close_log(pid()) :: :ok | {:error | :badarg | :terminated}
  def close_log(pid), do: File.close(pid)

  @spec send_newsletter(Path.t(), Path.t(), (String.t() -> :ok | :error)) :: :ok
  def send_newsletter(emails_path, log_path, send_fun),
    do:
      with(
        log when is_pid(log) <- open_log(log_path),
        emails when is_list(emails) <- read_emails(emails_path),
        :ok <- Enum.each(emails, &send_and_log(&1, send_fun, log)),
        close_log(log),
        do: :ok
      )

  @spec send_and_log(String.t(), (String.t() -> :ok | :error), pid()) :: :ok | :error
  defp send_and_log(email, send_fun, log_pid),
    do:
      with(
        :ok <- send_fun.(email),
        do: log_sent_email(log_pid, email)
      )
end
