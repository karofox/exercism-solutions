defmodule Newsletter do
  @moduledoc """
  Module for newsletter management.
  """

  @spec read_emails(Path.t()) :: [String.t()]
  def read_emails(path) do
    case File.read(path) do
      {:ok, emails} -> emails |> String.split("\n") |> Enum.filter(&(&1 != ""))
    end
  end

  @spec open_log(Path.t()) :: pid()
  def open_log(path), do: File.open!(path, [:write])

  @spec log_sent_email(pid(), String.t()) :: :ok
  def log_sent_email(pid, email), do: IO.puts(pid, email)

  @spec close_log(pid()) :: :ok | {:error | :badarg | :terminated}
  def close_log(pid), do: File.close(pid)

  @spec send_newsletter(Path.t(), Path.t(), (String.t() -> :ok | :error)) :: :ok
  def send_newsletter(emails_path, log_path, send_fun) do
    pid = open_log(log_path)

    emails_path
    |> read_emails()
    |> Enum.each(fn email -> send_and_log(email, send_fun, pid) end)

    close_log(pid)
  end

  @spec send_and_log(String.t(), (String.t() -> :ok | :error), pid()) :: :ok
  defp send_and_log(email, send_fun, log_pid) do
    with :ok <- send_fun.(email) do
      log_sent_email(log_pid, email)
    end
  end
end
