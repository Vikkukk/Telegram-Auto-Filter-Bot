#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @victorlctt

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("16869866"))

API_HASH = os.environ.get("b6defd08178346ef6d0539e4db127acf")

BOT_TOKEN = os.environ.get("5735937868:AAG6rfVcLc-OEJV_kzaNIJY1XTtbGlTnWcs")

DB_URI = os.environ.get("mongodb+srv://Vikkukk:Lami@123#@cluster0.jpd0xtm.mongodb.net/?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("1889791911")

BUTTON = os.environ.get("BUTTON", "Channel - https://t.me/allbots4uall")  # Button - link

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
