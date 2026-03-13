from location_v4 import Location, LocationDescriptions
from world_v4 import World


class WorldFactory:
    @staticmethod
    def create(
        location_descriptions: LocationDescriptions,
    ) -> World:
        """Create a World from a description of its locations."""
        locations = {
            data["name"]: Location.from_description(data)
            for data in location_descriptions
        }
        initial_location_name = location_descriptions[0]["name"]
        _build_connections_for_all_locations(locations, location_descriptions)
        return World(locations, initial_location_name)


def _build_connections_for_all_locations(
    locations: dict[str, Location], location_descriptions: LocationDescriptions
):
    for location_description in location_descriptions:
        connections = {
            direction: locations[name]
            for direction, name in location_description.get("connections", {}).items()
        }
        locations[location_description["name"]].connections = connections
