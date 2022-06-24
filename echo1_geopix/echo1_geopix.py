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
        self, rel_x: Union[int, float], rel_y: Union[int, float]
    ) -> Dict:
        return {
            "lon": self.min_lon + (self.max_lon - self.min_lon) * (1 - rel_y),
            "lat": self.min_lat + (self.max_lat - self.min_lat) * (rel_x),
        }

    @beartype
    def get_rel_pixel_points_from_geo_points(
        self, lat: Union[int, float], lon: Union[int, float]
    ) -> Dict:
        return {
            "x": ((lat - self.min_lat) / (self.max_lat - self.min_lat)),
            "y": ((self.max_lon - lon) / (self.max_lon - self.min_lon)),
        }

    @beartype
    def get_geo_box_from_rel_pixel_box(
        self,
        min_x_rel: Union[int, float],
        min_y_rel: Union[int, float],
        max_x_rel: Union[int, float],
        max_y_rel: Union[int, float],
    ) -> Dict:
        return {
            "min_lon": self.max_lon - (self.max_lon - self.min_lon) * min_y_rel,
            "max_lon": self.max_lon - (self.max_lon - self.min_lon) * max_y_rel,
            "min_lat": self.min_lat + (self.max_lat - self.min_lat) * min_x_rel,
            "max_lat": self.min_lat + (self.max_lat - self.min_lat) * max_x_rel,
        }

    @beartype
    def get_rel_pixel_box_from_geo_box(
        self,
        _min_lat: Union[int, float],
        _max_lat: Union[int, float],
        _min_lon: Union[int, float],
        _max_lon: Union[int, float],
    ) -> Dict:

        # lon_min = _min_lon
        # lat_min = _min_lat
        # lon_max = _max_lon
        # lat_max = _max_lat

        # top = self.max_lat
        # bottom = self.min_lat
        # left = self.min_lon
        # right = self.max_lon

        lon_min = _min_lon
        lat_min = _min_lat
        lon_max = _max_lon
        lat_max = _max_lat

        top = self.max_lat
        bottom = self.min_lat
        left = self.min_lon
        right = self.max_lon

        # print(100)
        # print(left, self.min_lon, lon_min, _min_lon)
        # print(bottom, self.min_lat, lat_min, _min_lat)
        # print(right, self.max_lon, lon_max, _max_lon)
        # print(top, self.max_lat, lat_max, _max_lat)

        # return coords for bounding box in pixel coords for a specific image
        # as percentage of image width and height
        x_min = (lon_min - left) / (right - left)
        x_max = (lon_max - left) / (right - left)
        y_min = (top - lat_min) / (top - bottom)
        y_max = (top - lat_max) / (top - bottom)
        return {"x_min": x_min, "y_min": y_min, "x_max": y_min, "y_max": y_max}

        # return {
        #     "min_x": (self.min_lon - _min_lon) / (_max_lat - _min_lat),
        #     "max_x": (_max_lat - self.min_lat) / (_max_lon - _min_lon),
        #     "min_y": (_max_lat - self.min_lat) / (_max_lon - _min_lon),
        #     "max_y": (_max_lat - self.max_lat) / (_max_lon - _min_lon),
        # }
