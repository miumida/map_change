from http import HTTPStatus
import requests
import logging
import asyncio
import aiohttp
import async_timeout

import json
import base64
import subprocess

from typing import Any

import voluptuous as vol

import homeassistant.loader as loader
import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries

from homeassistant.helpers import discovery

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({DOMAIN: {}}, extra=vol.ALLOW_EXTRA)


def subp_run(cmd, allow_failure: bool = False) -> subprocess.CompletedProcess:
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)

    if not allow_failure and output.returncode != 0:
        _LOGGER.error(f'[{DOMAIN}]The command "{cmd}" failed.')
    return output


async def async_setup(hass, config):

    if DOMAIN not in config:
        return True

    return True


async def async_setup_entry(hass, config_entry):
    """Set up this integration using UI."""

    if hass.data.get(DOMAIN) is not None:
        return False

    if config_entry.source == config_entries.SOURCE_IMPORT:
        hass.async_create_task(hass.config_entries.async_remove(config_entry.entry_id))
        return False    

    async def map(service):
        _LOGGER.error(f'[{DOMAIN}] Map Change Service call!')
        cmd = 'bash -c "$(wget -O - \'https://raw.githubusercontent.com/miumida/HA_Related/main/changing_map_20241013.sh\')"'

        _LOGGER.error(subp_run(cmd).stdout)

    hass.services.async_register(DOMAIN, "map_change", map)

    return True
