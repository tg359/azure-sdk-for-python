# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QueryConnectionMonitorsParameters(Model):
    """Parameters to query connection monitors.

    :param connection_monitor_ids: List of connection monitors ID.
    :type connection_monitor_ids: list[str]
    """

    _attribute_map = {
        'connection_monitor_ids': {'key': 'connectionMonitorIds', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(QueryConnectionMonitorsParameters, self).__init__(**kwargs)
        self.connection_monitor_ids = kwargs.get('connection_monitor_ids', None)
