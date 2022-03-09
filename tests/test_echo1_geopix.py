from echo1_geopix import __version__
from echo1_geopix.echo1_geopix import (
    geo_point_2_pix_point,
    geo_box_2_pixel_box,
    pixel_point_2_geo_point,
    pixel_box_2_geo_box,
)
from loguru import logger
from math import isclose

# test values
x_min = 0.35596034
y_min = 0.94408214
x_max = 0.4102673
y_max = 0.9986186
top = 19.013473367825767
bottom = 19.003535899073533
left = -98.27081680297852
right = -98.26036944570143


def test_point_funcs():

    ##
    # pixel_point_2_geo_point
    ##
    tmp_geo_coords = pixel_point_2_geo_point(left, right, top, bottom, x_min, y_min)
    logger.debug("pixel_point_2_geo_point: {}".format(tmp_geo_coords))

    ##
    # geo_point_2_pix_point
    ##
    tmp_pixel_coords = geo_point_2_pix_point(
        left, right, top, bottom, tmp_geo_coords["lon"], tmp_geo_coords["lat"]
    )
    logger.debug("geo_point_2_pix_point: {}".format(tmp_pixel_coords))
    assert isclose(x_min, tmp_pixel_coords["x"], abs_tol=1e-8)


def test_box_funcs():
    ##
    # pixel_box_2_geo_box
    ##
    tmp_geo_box = pixel_box_2_geo_box(
        x_min, y_min, x_max, y_max, left, right, top, bottom
    )
    assert "lon_min" in tmp_geo_box
    assert "lon_max" in tmp_geo_box
    assert "lat_min" in tmp_geo_box
    assert "lat_max" in tmp_geo_box
    logger.debug("pixel_box_2_geo_box: {}".format(tmp_geo_box))

    ##
    # geo_box_2_pixel_box
    ##
    temp_pixel_box = geo_box_2_pixel_box(
        tmp_geo_box["lon_min"],
        tmp_geo_box["lat_min"],
        tmp_geo_box["lon_max"],
        tmp_geo_box["lat_max"],
        left,
        right,
        top,
        bottom,
    )
    assert "x_min" in temp_pixel_box
    assert "y_min" in temp_pixel_box
    assert "x_max" in temp_pixel_box
    assert "y_max" in temp_pixel_box
    logger.debug("geo_box_2_pixel_box: {}".format(temp_pixel_box))
