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
            "lat": self.min_lon + (self.max_lon - self.min_lon) * (1 - rel_y),
            "lon": self.min_lat + (self.max_lat - self.min_lat) * (rel_x),
        }

    @beartype
    def get_rel_pixel_points_from_geo_points(
        self, lat: Union[int, float], lon: Union[int, float]
    ) -> Dict:
        return {
            "x": ((lon - self.min_lat) / (self.max_lat - self.min_lat)),
            "y": ((self.max_lon - lat) / (self.max_lon - self.min_lon)),
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
            "min_lat": self.max_lon - (self.max_lon - self.min_lon) * min_y_rel,
            "max_lat": self.max_lon - (self.max_lon - self.min_lon) * max_y_rel,
            "min_lon": self.min_lat + (self.max_lat - self.min_lat) * min_x_rel,
            "max_lon": self.min_lat + (self.max_lat - self.min_lat) * max_x_rel,
        }

    @beartype
    def get_rel_pixel_box_from_geo_box(
        self,
        _min_lat: Union[int, float],
        _max_lat: Union[int, float],
        _min_lon: Union[int, float],
        _max_lon: Union[int, float],
    ) -> Dict:

        return {
            "min_x": (self.min_lon - _min_lat) / (_max_lat - _min_lat),
            "max_x": (_max_lon - self.min_lat) / (_max_lon - _min_lon),
            "min_y": (_max_lon - self.min_lat) / (_max_lon - _min_lon),
            "max_y": (_max_lon - self.max_lat) / (_max_lon - _min_lon),
        }


def pixel_point_2_geo_point(min_lat, max_lat, min_lon, max_lon, rel_x, rel_y):
    p = GeoPix(min_lat, max_lat, min_lon, max_lon)
    return p.get_geo_points_from_rel_pixel_points(rel_x, rel_y)


def geo_point_2_pix_point(min_lat, max_lat, min_lon, max_lon, lat, lon):
    p = GeoPix(min_lat, max_lat, min_lon, max_lon)
    return p.get_rel_pixel_points_from_geo_points(lat, lon)


def pixel_box_2_geo_box(
    min_lat, max_lat, min_lon, max_lon, min_x_rel, min_y_rel, max_x_rel, max_y_rel
):
    p = GeoPix(min_lat, max_lat, min_lon, max_lon)
    return p.get_geo_box_from_rel_pixel_box(min_x_rel, min_y_rel, max_x_rel, max_y_rel)


def geo_box_2_pixel_box(
    min_lat, max_lat, min_lon, max_lon, _min_lat, _max_lat, _min_lon, _max_lon
):
    p = GeoPix(min_lat, max_lat, min_lon, max_lon)
    return p.get_rel_pixel_box_from_geo_box(_min_lat, _max_lat, _min_lon, _max_lon)
