# -*- coding: utf-8 -*-
"""
################################################################################
# Copyright (c) 2010, Ilgar Mashayev
# 
# E-mail: pyzimbra@lab.az
# Website: http://github.com/ilgarm/pyzimbra
################################################################################
# This file is part of pyzimbra.
# 
# Pyzimbra is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Pyzimbra is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Pyzimbra.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

Account info samples.

@author: ilgar
"""
from ConfigParser import ConfigParser
from pyzimbra import pconstant


def load_properties():
    properties = "client-local.properties"
    cfg = ConfigParser()
    cfg.read(properties)

    p = {}
    p[pconstant.DOMAIN] = cfg.get(pconstant.DOMAIN, pconstant.NAME)
    p[pconstant.HOSTNAME] = cfg.get(pconstant.DOMAIN, pconstant.HOST)
    p[pconstant.DOMAIN_KEY] = cfg.get(pconstant.DOMAIN, pconstant.KEY)
    p[pconstant.DOMAINS] = {p[pconstant.DOMAIN]:
                    {pconstant.HOSTNAME: p[pconstant.HOSTNAME],
                     pconstant.KEY: p[pconstant.DOMAIN_KEY]}}

    p[pconstant.PROXY_SCHEME] = cfg.get(pconstant.PROXY, pconstant.SCHEME)
    p[pconstant.PROXY_HOSTNAME] = cfg.get(pconstant.PROXY, pconstant.HOST)
    p[pconstant.PROXY_PORT] = cfg.get(pconstant.PROXY, pconstant.SCHEME)
    p[pconstant.PROXY_USERNAME] = cfg.get(pconstant.PROXY, pconstant.USERNAME)
    p[pconstant.PROXY_PASSWORD] = cfg.get(pconstant.PROXY, pconstant.PASSWORD)

    p[pconstant.USERNAME] = cfg.get(pconstant.AUTH, pconstant.USERNAME)
    p[pconstant.ACCOUNT_NAME] = '%s@%s' % (p[pconstant.USERNAME], p[pconstant.DOMAIN])
    p[pconstant.PASSWORD] = cfg.get(pconstant.AUTH, pconstant.PASSWORD)

    return p
