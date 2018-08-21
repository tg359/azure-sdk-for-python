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

from .gallery_artifact_publishing_profile_base_py3 import GalleryArtifactPublishingProfileBase


class GalleryImageVersionPublishingProfile(GalleryArtifactPublishingProfileBase):
    """The publishing profile of a gallery image version.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param regions: The regions where the artifact is going to be published.
    :type regions: list[str]
    :param source: Required.
    :type source: ~azure.mgmt.compute.v2018_06_01.models.GalleryArtifactSource
    :param scale_tier: The scale tier of the gallery image version. Valid
     values are 'S30' and 'S100'. Possible values include: 'S30', 'S100'
    :type scale_tier: str or ~azure.mgmt.compute.v2018_06_01.models.ScaleTier
    :param exclude_from_latest: The flag means that if it is set to true,
     people deploying VMs with 'latest' as version will not use this version.
    :type exclude_from_latest: bool
    :ivar published_date: The time when the gallery image version is
     published.
    :vartype published_date: datetime
    :param end_of_life_date: The end of life date of the gallery image
     version.
    :type end_of_life_date: datetime
    """

    _validation = {
        'source': {'required': True},
        'published_date': {'readonly': True},
    }

    _attribute_map = {
        'regions': {'key': 'regions', 'type': '[str]'},
        'source': {'key': 'source', 'type': 'GalleryArtifactSource'},
        'scale_tier': {'key': 'scaleTier', 'type': 'str'},
        'exclude_from_latest': {'key': 'excludeFromLatest', 'type': 'bool'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'end_of_life_date': {'key': 'endOfLifeDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, source, regions=None, scale_tier=None, exclude_from_latest: bool=None, end_of_life_date=None, **kwargs) -> None:
        super(GalleryImageVersionPublishingProfile, self).__init__(regions=regions, source=source, **kwargs)
        self.scale_tier = scale_tier
        self.exclude_from_latest = exclude_from_latest
        self.published_date = None
        self.end_of_life_date = end_of_life_date
