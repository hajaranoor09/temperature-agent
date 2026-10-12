print ("\n=====================MODEL BASED AGENT ===================================")
model = {"Room1": None, "Room2": None}
heater_on_count = {"Room1": 0, "Room2": 0}


def temperature_agent(room, reading):
    """Model-based reflex agent managing a heater for two rooms."""
    global model, heater_on_count
    model[room] = reading
    if reading == "Cold":
        action = "Turn Heater ON"
        heater_on_count[room] += 1
    elif reading == "Hot":
        action = "Turn Heater OFF"
    elif model["Room1"] == "Normal" and model["Room2"] == "Normal":
        action = "All Rooms Comfortable - Idle"
    else:
        action = "Move to Other Room to Check"

    return action


def run_agent_simulation():
    percept_sequence = [
        ("Room1", "Cold"),
        ("Room1", "Normal"),
        ("Room2", "Hot"),
        ("Room2", "Normal"),
    ]
    print(f"{'Room':<10} {'Reading':<10} {'Action':<35} {'Model'}")
    print("-" * 85)
    for room, reading in percept_sequence:
        action = temperature_agent(room, reading)
        print(f"{room:<10} {reading:<10} {action:<35} {str(model)}")

    print(f"\nHeater ON count: {heater_on_count}")
if __name__ == "__main__":
    run_agent_simulation()
