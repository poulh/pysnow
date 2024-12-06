import pysnow


if __name__ == "__main__":
    dict = {"sys_id": [], "name": []}

    client = pysnow.Client(
        instance="mpgops",
        user="svc_vision_snow",
        password="er8Z(YZW",
    )

    locations_table_path = "/table/cmn_location"
    location_resource = client.resource(api_path=locations_table_path)
    location_centers = location_resource.get(
        path="/table/cmn_location",
        query=pysnow.QueryBuilder().field("sys_id").not_equals(""),
        fields=["sys_id", "name"],
        limit=50000,
    ).all()

    for location_center in location_centers:
        print(location_center)
        dict["sys_id"].append(location_center["sys_id"])
        dict["name"].append(location_center["name"])

    print(dict)
