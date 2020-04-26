#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


import os

from tobrot import (
    DOWNLOAD_LOCATION
)


import time
from tobrot.helper_funcs.extract_link_from_message import extract_link
from tobrot.helper_funcs.download_aria_p_n import call_apropriate_function, aria_start
from tobrot.helper_funcs.download_from_link import request_download
from tobrot.helper_funcs.display_progress import progress_for_pyrogram
from tobrot.helper_funcs.youtube_dl_extractor import extract_youtube_dl_formats


async def incoming_message_f(client, message):
    """/leech command"""
    is_zip = False
    if len(message.command) > 1:
        if message.command[1] == "archive":
            is_zip = True
    # get link from the incoming message
    dl_url, cf_name = extract_link(message.reply_to_message)
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        akcm = dl_url.split('\n')
<<<<<<< HEAD
        i_m_sefg = []
        for akci in range(len(akcm)):
            i_m_sefg.append(await message.reply_text("processing", quote=True))
        aria_i_p = []
        sagtus = []
        err_message = []
        current_user_id = []
        messagebkp = message
        for akci in range(len(akcm)):
            #message = messagebkp
            #i_m_sefg.append(await messagebkp.reply_text("processing", quote=True))
            await i_m_sefg[akci].edit_text("extracting links")
=======
        for akc_url in akcm:
            await i_m_sefg.edit_text("extracting links")
>>>>>>> parent of baba1ee... Update incoming_message_fn.py
            # start the aria2c daemon
            aria_i_p.append(await aria_start())
            LOGGER.info(aria_i_p[akci])
            current_user_id.append(messagebkp.from_user.id)
            # create an unique directory
            new_download_location = os.path.join(
                DOWNLOAD_LOCATION,
                str(current_user_id[akci]),
                str(time.time())
            )
            # create download directory, if not exist
            if not os.path.isdir(new_download_location):
                os.makedirs(new_download_location)
            await i_m_sefg[akci].edit_text("trying to download")
            # try to download the "link"
<<<<<<< HEAD
            if akci == len(akcm)-1:
                sagtus2, err_message2 = await call_apropriate_function(
                    aria_i_p[akci],
                    akcm[akci],
                    new_download_location,
                    i_m_sefg[akci],
                    is_zip
                )
            else:
                sagtus2, err_message2 = await call_apropriate_function(
                    aria_i_p[akci],
                    akcm[akci],
                    new_download_location,
                    i_m_sefg[akci],
                    is_zip
                )
            sagtus.append(sagtus2)
            err_message.append(err_message2)
=======
            sagtus, err_message = await call_apropriate_function(
                aria_i_p,
                akc_url,
                new_download_location,
                i_m_sefg,
                is_zip
            )
>>>>>>> parent of baba1ee... Update incoming_message_fn.py
            if not sagtus:
                # if FAILED, display the error message
                await i_m_sefg[akci].edit_text(err_message[akci])
    else:
        await i_m_sefg.edit_text("**ERR**! What have you entered. Please read /help")


async def incoming_youtube_dl_f(client, message):
    """ /ytdl command """
    i_m_sefg = await message.reply_text("processing", quote=True)
    # LOGGER.info(message)
    # extract link from message
    dl_url, cf_name = extract_link(message.reply_to_message)
    LOGGER.info(dl_url)
    LOGGER.info(cf_name)
    if dl_url is not None:
        await i_m_sefg.edit_text("extracting links")
        current_user_id = message.from_user.id
        # create an unique directory
        user_working_dir = os.path.join(DOWNLOAD_LOCATION, str(current_user_id))
        # create download directory, if not exist
        if not os.path.isdir(user_working_dir):
            os.makedirs(user_working_dir)
        # list the formats, and display in button markup formats
        thumb_image, text_message, reply_markup = await extract_youtube_dl_formats(
            dl_url,
            user_working_dir
        )
        if thumb_image is not None:
            await message.reply_photo(
                photo=thumb_image,
                quote=True,
                caption=text_message,
                reply_markup=reply_markup
            )
            await i_m_sefg.delete()
        else:
            await i_m_sefg.edit_text(
                text=text_message,
                reply_markup=reply_markup
            )
    else:
        # if no links found, delete the "processing" message
        await i_m_sefg.delete()
