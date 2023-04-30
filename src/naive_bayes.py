def classify_with_naive_bayes(classified_points, points_to_classify):
    scams = [point for point in classified_points if point["scam"] is True]
    nonscams = [point for point in classified_points if point["scam"] is False]

    for point_to_classify in points_to_classify:
        prob_of_scam = len(scams) / len(classified_points)
        prob_of_nonscam = len(nonscams) / len(classified_points)

        scams_with_point_error_val = 0
        scams_with_point_link_val = 0

        nonscams_with_point_error_val = 0
        nonscams_with_point_link_val = 0

        for scam in scams:
            if scam["errors"] == point_to_classify["errors"]:
                scams_with_point_error_val += 1
            if scam["links"] == point_to_classify["links"]:
                scams_with_point_link_val += 1

        for nonscam in nonscams:
            if nonscam["errors"] == point_to_classify["errors"]:
                nonscams_with_point_error_val += 1
            if nonscam["links"] == point_to_classify["links"]:
                nonscams_with_point_link_val += 1

        p_scam_with_point_error_val = scams_with_point_error_val / len(scams)
        p_scam_with_point_link_val = scams_with_point_link_val / len(scams)

        p_nonscam_with_point_error_val = nonscams_with_point_error_val / len(nonscams)
        p_nonscam_with_point_link_val = nonscams_with_point_link_val / len(nonscams)

        p_of_point_being_scam = (
            prob_of_scam * p_scam_with_point_error_val * p_scam_with_point_link_val
        )
        p_of_point_being_nonscam = (
            prob_of_nonscam
            * p_nonscam_with_point_error_val
            * p_nonscam_with_point_link_val
        )

        if p_of_point_being_scam > p_of_point_being_nonscam:
            point_to_classify["scam"] = True
        elif p_of_point_being_nonscam > p_of_point_being_scam:
            point_to_classify["scam"] = False
        else:
            point_to_classify["scam"] = prob_of_scam > prob_of_nonscam

    return points_to_classify


classified_data = [
    {"scam": False, "errors": False, "links": False},
    {"scam": True, "errors": True, "links": True},
    {"scam": True, "errors": True, "links": True},
    {"scam": False, "errors": False, "links": False},
    {"scam": False, "errors": False, "links": True},
    {"scam": True, "errors": True, "links": True},
    {"scam": False, "errors": True, "links": False},
    {"scam": False, "errors": False, "links": True},
    {"scam": True, "errors": True, "links": False},
    {"scam": False, "errors": False, "links": True},
]

data_to_classify = [
    {"errors": False, "links": False},
    {"errors": True, "links": True},
    {"errors": True, "links": False},
    {"errors": False, "links": True},
]

print(classify_with_naive_bayes(classified_data, data_to_classify))
