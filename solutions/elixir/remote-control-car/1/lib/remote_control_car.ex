defmodule RemoteControlCar do
  @enforce_keys [:nickname]
  defstruct [
    :nickname,
    battery_percentage: 100,
    distance_driven_in_meters: 0
  ]

  @spec new() :: RemoteControlCar
  def new(), do: %RemoteControlCar{nickname: "none"}

  @spec new(String.t()) :: RemoteControlCar
  def new(nickname), do: %RemoteControlCar{nickname: nickname}

  @spec display_distance(RemoteControlCar) :: String.t()
  def display_distance(remote_car) when is_struct(remote_car, RemoteControlCar),
    do: "#{remote_car.distance_driven_in_meters} meters"

  def display_battery(remote_car)
      when is_struct(remote_car, RemoteControlCar) and remote_car.battery_percentage == 0,
      do: "Battery empty"

  @spec display_battery(RemoteControlCar) :: String.t()
  def display_battery(remote_car) when is_struct(remote_car, RemoteControlCar),
    do: "Battery at #{remote_car.battery_percentage}%"

  @spec drive(RemoteControlCar) :: RemoteControlCar
  def drive(remote_car)
      when is_struct(remote_car, RemoteControlCar) and remote_car.battery_percentage == 0,
      do: remote_car

  def drive(remote_car) when is_struct(remote_car, RemoteControlCar),
    do: %{
      remote_car
      | battery_percentage: remote_car.battery_percentage - 1,
        distance_driven_in_meters: remote_car.distance_driven_in_meters + 20
    }
end
