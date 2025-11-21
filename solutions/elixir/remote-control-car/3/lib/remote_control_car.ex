defmodule RemoteControlCar do
  @enforce_keys [:nickname]
  defstruct [
    :nickname,
    battery_percentage: 100,
    distance_driven_in_meters: 0
  ]

  @doc """
  Creates a new RemoteControlCar struct.
  """
  @spec new(String.t()) :: RemoteControlCar
  def new(nickname \\ "none"), do: %RemoteControlCar{nickname: nickname}

  @doc """
  Displays the distance driven by the RemoteControlCar in meters.
  """
  @spec display_distance(RemoteControlCar) :: String.t()
  def display_distance(%RemoteControlCar{distance_driven_in_meters: distance}),
    do: "#{distance} meters"

  @doc """
  Displays the battery percentage of the RemoteControlCar.
  """
  @spec display_battery(RemoteControlCar) :: String.t()
  def display_battery(%RemoteControlCar{battery_percentage: 0}),
    do: "Battery empty"

  def display_battery(%RemoteControlCar{battery_percentage: battery}),
    do: "Battery at #{battery}%"

  @doc """
  Updates the RemoteControlCar battery and distance after driving.
  """
  @spec drive(RemoteControlCar) :: RemoteControlCar
  def drive(%RemoteControlCar{battery_percentage: 0} = remote_car),
    do: remote_car

  def drive(
        %RemoteControlCar{battery_percentage: battery, distance_driven_in_meters: distance} =
          remote_car
      ),
      do: %{
        remote_car
        | battery_percentage: battery - 1,
          distance_driven_in_meters: distance + 20
      }
end
