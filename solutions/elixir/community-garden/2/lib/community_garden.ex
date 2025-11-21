# Use the Plot struct as it is provided
defmodule Plot do
  @enforce_keys [:plot_id, :registered_to]
  defstruct [:plot_id, :registered_to]
end

defmodule PlotRegistry do
  @spec new() :: %{id: integer(), plots: [Plot]}
  def new, do: %{id: 1, plots: []}

  @spec register(%{id: integer(), plots: [Plot]}, String.t()) :: Plot
  def register(%{id: id, plots: plots}, owner),
    do:
      with(
        plot <- %Plot{plot_id: id, registered_to: owner},
        do: {plot, %{id: id + 1, plots: [plot | plots]}}
      )

  @spec release(%{id: integer(), plots: [Plot]}, integer()) :: %{id: integer(), plots: [Plot]}
  def release(state, plot_id),
    do:
      Map.update(state, :plots, state[:plots], fn plots ->
        Enum.filter(plots, fn plot -> plot.plot_id != plot_id end)
      end)

  @spec all(%{id: integer(), plots: [Plot]}) :: [Plot]
  def all(%{plots: plots}), do: plots

  @spec get(%{id: integer(), plots: [Plot]}, integer()) :: Plot
  def get(%{plots: plots}, plot_id),
    do:
      Enum.find(plots, {:not_found, "plot is unregistered"}, fn plot ->
        plot.plot_id == plot_id
      end)
end

defmodule CommunityGarden do
  @spec start([any()]) :: {:ok, pid()}
  def start(opts \\ []), do: Agent.start(&PlotRegistry.new/0, opts)

  @spec list_registrations(pid()) :: [Plot]
  def list_registrations(pid), do: Agent.get(pid, &PlotRegistry.all(&1))

  @spec register(pid(), String.t()) :: Plot
  def register(pid, register_to),
    do: Agent.get_and_update(pid, &PlotRegistry.register(&1, register_to))

  @spec release(pid(), integer()) :: :ok
  def release(pid, plot_id),
    do: Agent.update(pid, &PlotRegistry.release(&1, plot_id))

  @spec get_registration(pid(), integer()) :: Plot | {:not_found, String.t()}
  def get_registration(pid, plot_id),
    do: Agent.get(pid, &PlotRegistry.get(&1, plot_id))
end
