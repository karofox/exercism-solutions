# Use the Plot struct as it is provided
defmodule Plot do
  @enforce_keys [:plot_id, :registered_to]
  defstruct [:plot_id, :registered_to]
end

defmodule CommunityGarden do
  @spec start([any()]) :: {:ok, pid()}
  def start(opts \\ []), do: Agent.start(fn -> %{id: 1, plots: []} end, opts)

  @spec list_registrations(pid()) :: [Plot]
  def list_registrations(pid), do: Agent.get(pid, fn %{plots: plots} -> plots end)

  @spec register(pid(), String.t()) :: Plot
  def register(pid, register_to),
    do:
      Agent.get_and_update(pid, fn %{id: id, plots: plots} ->
        with(
          plot <- %Plot{plot_id: id, registered_to: register_to},
          do: {plot, %{id: id + 1, plots: [plot | plots]}}
        )
      end)

  @spec release(pid(), integer()) :: :ok
  def release(pid, plot_id),
    do:
      Agent.update(pid, fn state ->
        Map.update(state, :plots, state[:plots], fn plots ->
          Enum.filter(plots, fn plot -> plot.plot_id != plot_id end)
        end)
      end)

  @spec get_registration(pid(), integer()) :: Plot | {:not_found, String.t()}
  def get_registration(pid, plot_id),
    do:
      Agent.get(pid, fn %{plots: plots} ->
        Enum.find(plots, {:not_found, "plot is unregistered"}, fn plot ->
          plot.plot_id == plot_id
        end)
      end)
end
