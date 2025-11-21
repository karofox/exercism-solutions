defmodule PaintByNumber do
  @spec palette_bit_size(integer()) :: integer()
  def palette_bit_size(color_count),
    do: Enum.find(1..color_count, &(Math.pow(2, &1) >= color_count))

  @spec empty_picture() :: <<>>
  def empty_picture(), do: <<>>

  @spec test_picture() :: <<_::2>>
  def test_picture(), do: <<0::2, 1::2, 2::2, 3::2>>

  @spec prepend_pixel(bitstring(), integer(), integer()) :: bitstring()
  def prepend_pixel(picture, color_count, pixel_color_index) do
    bit_size = palette_bit_size(color_count)
    <<pixel_color_index::size(bit_size), picture::bitstring>>
  end

  @spec get_first_pixel(bitstring(), integer()) :: integer() | nil
  def get_first_pixel(<<>>, _color_count), do: nil

  def get_first_pixel(picture, color_count) do
    bit_size = palette_bit_size(color_count)
    <<first_bit::size(bit_size), _::bitstring>> = picture
    first_bit
  end

  @spec drop_first_pixel(bitstring(), integer()) :: bitstring()
  def drop_first_pixel(<<>>, _color_count), do: <<>>

  def drop_first_pixel(picture, color_count) do
    bit_size = palette_bit_size(color_count)
    <<_::size(bit_size), rest::bitstring>> = picture
    rest
  end

  @spec concat_pictures(bitstring(), bitstring()) :: bitstring()
  def concat_pictures(picture1, picture2), do: <<picture1::bitstring, picture2::bitstring>>
end
