require Bitwise

defmodule Secrets do
  @doc"""
  Encryption device helpers.
  """

  @spec secret_add(integer()) :: (integer() -> integer())
  def secret_add(secret), do: &(&1 + secret)

  @spec secret_subtract(integer()) :: (integer() -> integer())
  def secret_subtract(secret), do: &(&1 - secret)

  @spec secret_multiply(integer()) :: (integer() -> integer())
  def secret_multiply(secret), do: &(&1 * secret)

  @spec secret_divide(integer()) :: (integer() -> integer())
  def secret_divide(secret), do: &(div(&1, secret))

  @spec secret_and(integer()) :: (integer() -> integer())
  def secret_and(secret), do: &(Bitwise.band(&1, secret))

  @spec secret_xor(integer()) :: (integer() -> integer())
  def secret_xor(secret), do: &(Bitwise.bxor(&1, secret))

  @spec secret_combine((integer() -> integer()), (integer() -> integer())) :: (integer() -> integer())
  def secret_combine(secret_function1, secret_function2) do
    fn x -> secret_function1.(x) |> secret_function2.() end
  end
end
