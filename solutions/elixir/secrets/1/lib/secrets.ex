require Bitwise

defmodule Secrets do
  @doc"""
  Encryption device helpers.
  """

  @spec secret_add(integer()) :: integer() :: integer()
  def secret_add(secret) do
    fn x -> x + secret end
  end

  @spec secret_subtract(integer()) :: integer() :: integer()
  def secret_subtract(secret) do
    fn x -> x - secret end
  end

  @spec secret_multiply(integer()) :: integer() :: integer()
  def secret_multiply(secret) do
    fn x -> x * secret end
  end

  @spec secret_divide(integer()) :: integer() :: integer()
  def secret_divide(secret) do
    fn x -> div(x, secret) end
  end

  @spec secret_and(integer()) :: integer() :: integer()
  def secret_and(secret) do
    fn x -> Bitwise.band(x, secret) end
  end

  @spec secret_xor(integer()) :: integer() :: integer()
  def secret_xor(secret) do
    fn x -> Bitwise.bxor(x, secret) end
  end

  @spec secret_combine(integer() :: integer(), integer() :: integer()) :: integer() :: integer()
  def secret_combine(secret_function1, secret_function2) do
    fn x -> secret_function1.(x) |> secret_function2.() end
  end
end
