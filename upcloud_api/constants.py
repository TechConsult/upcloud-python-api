from __future__ import unicode_literals
from __future__ import absolute_import

import re


class ZONE(object):
    """
    Enums for UpCloud's Zones.
    """

    Helsinki = 'fi-hel1'
    Helsinki2 = 'fi-hel2'
    London = 'uk-lon1'
    Chicago = 'us-chi1'
    Frankfurt = 'de-fra1'
    Amsterdam = 'nl-ams1'
    Singapore = 'sg-sin1'
    SanJose = 'us-sjo1'
    NewYork = 'us-nyc1'


class OperatingSystems(object):
    """
    Helper class for dealing with operating system names.
    """

    @classmethod
    def get_OS_UUID(cls, os, cloud_manager):
        """
        Validate Storage OS and its UUID.

        If the OS is a custom OS UUID, don't validate against templates.
        """
        templates = cls.get_templates(cloud_manager)
        if os in templates:
            return templates[os]

        uuid_regexp = '^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$'
        if re.search(uuid_regexp, os):
            return os

        raise Exception((
            "Invalid OS -- valid options are: "
            "'CentOS 6.10', 'CentOS 7', 'Centos 8', "
            "'Debian 8.11', 'Debian 9.9', 'Debian 10.10', "
            "'Ubuntu 12.04', 'Ubuntu 16.04', 'Ubuntu 18.04', 'Ubuntu 20.04', "
            "'Windows 2016', 'Windows 2019'"
        ))

    @classmethod
    def get_templates(cls, cloud_manager):
        templates = {}
        storages = cloud_manager.get_storages(storage_type='template')
        for storage in storages:
            templates.update({storage.title: storage.uuid})
        return templates
