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


class ErrorDetails(Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Error code identifying the specific error.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param additional_properties: Additional custom properties.
    :type additional_properties: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'additional_properties': {'key': 'additionalProperties', 'type': 'object'},
    }

    def __init__(self, *, code: str, message: str, additional_properties=None, **kwargs) -> None:
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.additional_properties = additional_properties
