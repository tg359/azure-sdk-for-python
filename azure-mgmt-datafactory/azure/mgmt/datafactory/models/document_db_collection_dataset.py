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

from .dataset import Dataset


class DocumentDbCollectionDataset(Dataset):
    """Microsoft Azure Document Database Collection dataset.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Dataset description.
    :type description: str
    :param structure: Columns that define the structure of the dataset. Type:
     array (or Expression with resultType array), itemType: DatasetDataElement.
    :type structure: object
    :param linked_service_name: Required. Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param parameters: Parameters for dataset.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param folder: The folder that this Dataset is in.
    :type folder: ~azure.mgmt.datafactory.models.DatasetFolder
    :param type: Required. Constant filled by server.
    :type type: str
    :param collection_name: Required. Document Database collection name. Type:
     string (or Expression with resultType string).
    :type collection_name: object
    """

    _validation = {
        'linked_service_name': {'required': True},
        'type': {'required': True},
        'collection_name': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'structure': {'key': 'structure', 'type': 'object'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'folder': {'key': 'folder', 'type': 'DatasetFolder'},
        'type': {'key': 'type', 'type': 'str'},
        'collection_name': {'key': 'typeProperties.collectionName', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(DocumentDbCollectionDataset, self).__init__(**kwargs)
        self.collection_name = kwargs.get('collection_name', None)
        self.type = 'DocumentDbCollection'
