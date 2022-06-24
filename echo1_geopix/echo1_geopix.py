from beartype import beartype
from beartype.typing import Dict, Union


class GeoPix:
    @beartype
    def __init__(
        self,
        min_lat: Union[int, float],
        max_lat: Union[int, float],
        min_lon: Union[int, float],
        max_lon: Union[int, float],
    ) -> None:
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon

    @beartype
    def get_geo_points_from_rel_pixel_points(
        self, min_x_rel: Union[int, float], min_y_rel: Union[int, float]
    ) -> Dict:

        # min_lon, max_lon, max_lat, min_lat, min_x_rel, min_y_rel
        # min_x_rel and min_y_rel pixel coords are relative to the max_lat min_lon
        return {
            "lat": self.min_lat + (self.max_lat - self.min_lat) * (1 - min_y_rel),
            "lon": self.min_lon + (self.max_lon - self.min_lon) * (min_x_rel),
        }

    def get_rel_pixel_points_from_geo_points(
        self, lat: Union[int, float], lon: Union[int, float]
    ) -> Dict:
        # min_lon, max_lon, max_lat, min_lat, lon, lat
        # x and y geo coords are in latitude, longitude
        return {
            "x": (lon - self.min_lon) / (self.max_lon - self.min_lon),
            "y": (self.max_lat - lat) / (self.max_lat - self.min_lat),
        }

    def get_geo_box_from_rel_pixel_box(
        self,
        min_x_rel: Union[int, float],
        max_x_rel: Union[int, float],
        min_y_rel: Union[int, float],
        max_y_rel: Union[int, float],
    ) -> Dict:

        # return coords for bounding box in lon,lat format
        return {
            "min_lat": self.max_lat - (self.max_lat - self.min_lat) * min_y_rel,
            "max_lat": self.max_lat - (self.max_lat - self.min_lat) * max_y_rel,
            "min_lon": self.min_lon + (self.max_lon - self.min_lon) * min_x_rel,
            "max_lon": self.min_lon + (self.max_lon - self.min_lon) * max_x_rel,
        }

    def get_rel_pixel_box_from_geo_box(
        self,
        min_lat: Union[int, float],
        max_lat: Union[int, float],
        min_lon: Union[int, float],
        max_lon: Union[int, float],
    ) -> Dict:
        # return coords for bounding box in pixel coords for a specific image
        # as percentage of image width and height
        return {
            "min_x_rel": (min_lon - self.min_lon) / (self.max_lon - self.min_lon),
            "max_x_rel": (self.max_lat - min_lat) / (self.max_lat - self.min_lat),
            "min_y_rel": (self.max_lat - min_lat) / (self.max_lat - self.min_lat),
            "max_y_rel": (self.max_lat - max_lat) / (self.max_lat - self.min_lat),
        }
