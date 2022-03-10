#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-10 14:37

@author: johannes
"""
"""
Microservice Template: https://github.com/shark-microservices/microservice_template

This service is intended for SMHI-NODC use.
    -


For StnReg guidance see: https://stationsregister.miljodatasamverkan.se/dok/StnReg02_Handledning.pdf

Example:
    kwargs = {
        'force': True
    }
    body = {
        'preferred_name': 'NAMN_PÅ_NY_PROVPLATS',
        'responsible_datahost_name': 'DV Oceanografi och marinbiologi',
        'position_n': '6258263',
        'position_e': '239000',
        'validated': '2022-03-10',
        'associated_datahosts': 'DV Oceanografi och marinbiologi',
        'media': 'Vatten',
    }
    resp = requests.request(
        "POST",
        url='*********/geoserver/rest/nv/stnreg/api/monitoringFacility',
        json=body,
        headers={
            'Content-Type': 'application/json',
            'X-STNREG-APIKEY': '**********************************'
        },
    )
"""  # noqa: E501
import connexion
from handler import Connector

conn = Connector()


def post_new(*args, data=None, **kwargs):
    """Post station function."""
    return conn.post(
        data=data,
        **kwargs
    )


app = connexion.FlaskApp(
    __name__,
    specification_dir='./',
    options={'swagger_url': '/'},
)
app.add_api('openapi.yaml')

if __name__ == "__main__":
    app.run(port=5000)

