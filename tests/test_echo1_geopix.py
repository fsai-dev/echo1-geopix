from echo1_geopix.echo1_geopix import GeoPix
from loguru import logger
from math import isclose

# test values (rel pixel values)
min_x_rel = 0.35596034
min_y_rel = 0.94408214
max_x_rel = 0.4102673
max_y_rel = 0.9986186

# test values (geo values)
min_lat = -98.27081680297852
max_lat = -98.26036944570143
min_lon = 19.003535899073533
max_lon = 19.013473367825767


def test_point_funcs():

    ##
    # pixel_point_2_geo_point
    ##
    gp = GeoPix(min_lat, max_lat, min_lon, max_lon)
    tmp_geo_coords = gp.get_geo_points_from_rel_pixel_points(min_x_rel, min_y_rel)
    assert tmp_geo_coords == {"lon": -98.26709795813007, "lat": 19.004091581059974}
    # logger.debug("pixel_point_2_geo_point: {}".format(tmp_geo_coords))

    ##
    # geo_point_2_pix_point
    ##
    gp = GeoPix(min_lat, max_lat, min_lon, max_lon)
    tmp_pixel_coords = gp.get_rel_pixel_points_from_geo_points(
        tmp_geo_coords["lat"], tmp_geo_coords["lon"]
    )
    assert tmp_pixel_coords == {"x": 0.3559603399996717, "y": 0.9440821400000854}
    assert isclose(min_x_rel, tmp_pixel_coords["x"], abs_tol=1e-8)
    assert isclose(min_y_rel, tmp_pixel_coords["y"], abs_tol=1e-8)
    # logger.debug("geo_point_2_pix_point: {}".format(tmp_pixel_coords))


def test_box_funcs():

    ##
    # pixel_box_2_geo_box
    ##
    gp = GeoPix(min_lat, max_lat, min_lon, max_lon)
    tmp_geo_box = gp.get_geo_box_from_rel_pixel_box(
        min_x_rel,
        min_y_rel,
        max_x_rel,
        max_y_rel,
    )

    assert tmp_geo_box == {
        "min_lon": -98.26709795813007,
        "max_lon": -98.26653059391631,
        "min_lat": 19.004091581059974,
        "max_lat": 19.003549626692866,
    }
    # logger.debug("pixel_box_2_geo_box: {}".format(tmp_geo_box))

    ##
    # geo_box_2_pixel_box
    ##
    gp = GeoPix(
        tmp_geo_box["min_lat"],
        tmp_geo_box["max_lat"],
        tmp_geo_box["min_lon"],
        tmp_geo_box["max_lon"],
    )

    temp_pixel_box = gp.get_rel_pixel_box_from_geo_box(
        min_lat, max_lat, min_lon, max_lon
    )

    assert temp_pixel_box == {
        "min_x": 0.3559603399996717,
        "min_y": 0.9440821400000854,
        "max_x": 0.9440821400000854,
        "max_y": 0.998618600000152,
    }

    # logger.debug("geo_box_2_pixel_box: {}".format(temp_pixel_box))
