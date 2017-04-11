#
# Copyright (c) 2017 Juniper Networks, Inc. All rights reserved.
#

_WEB_HOST = '127.0.0.1'
_WEB_PORT = 6991
_CASSANDRA_HOST = '127.0.0.1'
_CASSANDRA_PORT = 9160
_CASSANDRA_MAX_RETRIES = 5
_CASSANDRA_TIMEOUT = 0.5
_ZK_HOST = '127.0.0.1'
_ZK_PORT = 2181
DEFAULT_VERSION='1.0'

# MESOS CNI DEFAULTS
MESOS_DEFAULT_PRIVATE_NETWORK = "default-network"
MESOS_DEFAULT_PRIVATE_SUBNET  = "10.32.0.0/16"
MESOS_DEFAULT_PUBLIC_NETWORK  = "Public"
MESOS_DEFAULT_PUBLIC_SUBNET   = "172.31.0.0/16"
MESOS_DEFAULT_SERVICE_SUBNET  = "10.64.0.0/16"
MESOS_DEFAULT_DOMAIN          = "default-domain"
MESOS_DEFAULT_PROJECT         = "default-project"

# MESOS Labels
MESOS_LABEL_PRIVATE_NETWORK = "network"
MESOS_LABEL_SERVICE         = "service"
MESOS_LABEL_SERVICE_SUBNET  = "service_subnet"
MESOS_LABEL_PUBLIC_NETWORK  = "public"
MESOS_LABEL_PUBLIC_SUBNET   = "public_subnet"
MESOS_LABEL_POLICY          = "policy"

