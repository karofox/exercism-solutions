defmodule FileSniffer do
  @extensions_types_signatures [
    {"exe", "application/octet-stream", <<0x7F, 0x45, 0x4C, 0x46>>},
    {"bmp", "image/bmp", <<0x42, 0x4D>>},
    {"png", "image/png", <<0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A>>},
    {"jpg", "image/jpg", <<0xFF, 0xD8, 0xFF>>},
    {"gif", "image/gif", <<0x47, 0x49, 0x46>>}
  ]

  Enum.each(@extensions_types_signatures, fn {extension, type, _signature} ->
    def type_from_extension(unquote(extension)), do: unquote(type)
  end)

  def type_from_extension(_extension), do: nil

  Enum.each(@extensions_types_signatures, fn {_extension, type, signature} ->
    def type_from_binary(unquote(signature) <> <<_::binary>>),
      do: unquote(type)
  end)

  def type_from_binary(_binary), do: nil

  Enum.each(@extensions_types_signatures, fn {extension, type, signature} ->
    def verify(unquote(signature) <> <<_::binary>>, unquote(extension)),
      do: {:ok, unquote(type)}
  end)

  def verify(_file_binary, _extension),
    do: {:error, "Warning, file format and file extension do not match."}
end
