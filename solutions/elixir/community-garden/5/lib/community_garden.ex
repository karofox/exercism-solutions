# Use the Plot struct as it is provided
defmodule Plot do
  @enforce_keys [:plot_id, :registered_to]
  defstruct [:plot_id, :registered_to]
end

defmodule PlotRegistry do
  @spec new() :: map()
  def new, do: %{__next_id__: 1}

  @spec register(map(), String.t()) :: Plot
  def register(registry = %{__next_id__: next_id}, owner),
    do:
      with(
        plot <- %Plot{plot_id: next_id, registered_to: owner},
        registry <- Map.put_new(registry, next_id, plot),
        registry <- %{registry | __next_id__: next_id + 1},
        do: {plot, registry}
      )

  @spec release(map(), integer()) :: map()
  def release(registry, plot_id),
    do: Map.delete(registry, plot_id)

  @spec all(map()) :: [Plot]
  def all(registry), do: for({_id, plot=%Plot{}} <- registry, do: plot)

  @spec get(map(), integer()) :: Plot
  def get(registry, plot_id), do: Map.get(registry, plot_id, {:not_found, "plot is unregistered"})
end

defmodule CommunityGarden do
  @spec start([any()]) :: {:ok, pid()}
  def start(opts \\ []), do: Agent.start(&PlotRegistry.new/0, opts)

  @spec list_registrations(pid()) :: [Plot]
  def list_registrations(pid), do: Agent.get(pid, &PlotRegistry.all/1)

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
