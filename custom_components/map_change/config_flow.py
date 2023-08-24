"""Config flow for Map Change"""
import logging
import json

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class CattConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Map Change."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize flow."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is None:
            return self.async_show_form(step_id="user")

        uniqid = 'naver-map-change-service'

        await self.async_set_unique_id(uniqid)

        tit = 'Map Change'

        return self.async_create_entry(title=tit, data=user_input)


    async def async_step_import(self, import_info):
        """Handle import from config file."""
        return await self.async_step_user(import_info)
