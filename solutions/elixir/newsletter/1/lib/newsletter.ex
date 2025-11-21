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
  def open_log(path) do
    case File.open(path, [:write]) do
      {:ok, pid} -> pid
    end
  end

  @spec log_sent_email(pid(), String.t()) :: :ok
  def log_sent_email(pid, email), do: IO.write(pid, email <> "\n")

  @spec close_log(pid()) :: :ok | {:error | :badarg | :terminated}
  def close_log(pid), do: File.close(pid)

  @spec send_newsletter(Path.t(), Path.t(), (String.t() -> :ok | :error)) :: :ok
  def send_newsletter(emails_path, log_path, send_fun) do
    pid = open_log(log_path)

    emails_path
    |> read_emails()
    |> Enum.each(fn email ->
      case send_fun.(email) do
        :ok -> log_sent_email(pid, email)
        :error -> nil
      end
    end)

    close_log(pid)
  end
end
