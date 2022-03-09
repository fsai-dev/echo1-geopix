def pixel_point_2_geo_point(left, right, top, bottom, x_min, y_min):
    # left, right, top, bottom, x_min, y_min
    # x and y pixel coords are in fractions from top left
    lat = bottom + (top - bottom) * (1 - y_min)
    lon = left + (right - left) * (x_min)
    return {"lon": lon, "lat": lat}


def geo_point_2_pix_point(left, right, top, bottom, lon, lat):
    # left, right, top, bottom, lon, lat
    # x and y geo coords are in latitude, longitude
    x = (lon - left) / (right - left)
    y = (top - lat) / (top - bottom)
    return {"x": x, "y": y}


def pixel_box_2_geo_box(x_min, y_min, x_max, y_max, left, right, top, bottom):
    # return coords for bounding box in lon,lat format
    lon_min = left + (right - left) * x_min
    lon_max = left + (right - left) * x_max
    lat_min = top - (top - bottom) * y_min
    lat_max = top - (top - bottom) * y_max
    return {
        "lon_min": lon_min,
        "lat_min": lat_min,
        "lon_max": lon_max,
        "lat_max": lat_max,
    }


def geo_box_2_pixel_box(lon_min, lat_min, lon_max, lat_max, left, right, top, bottom):
    # return coords for bounding box in pixel coords for a specific image
    # as percentage of image width and height
    x_min = (lon_min - left) / (right - left)
    x_max = (lon_max - left) / (right - left)
    y_min = (top - lat_min) / (top - bottom)
    y_max = (top - lat_max) / (top - bottom)
    return {"x_min": x_min, "y_min": y_min, "x_max": y_min, "y_max": y_max}
