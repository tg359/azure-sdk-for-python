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

from .migrate_schema_sql_server_sql_db_task_output import MigrateSchemaSqlServerSqlDbTaskOutput


class MigrateSchemaSqlTaskOutputError(MigrateSchemaSqlServerSqlDbTaskOutput):
    """MigrateSchemaSqlTaskOutputError.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar error: Migration error
    :vartype error: ~azure.mgmt.datamigration.models.ReportableException
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'error': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'error': {'key': 'error', 'type': 'ReportableException'},
    }

    def __init__(self, **kwargs):
        super(MigrateSchemaSqlTaskOutputError, self).__init__(**kwargs)
        self.error = None
        self.result_type = 'ErrorOutput'
