#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:26:38 2023

@author: mac
"""


import pickle
from pathlib import Path

import streamlit_authenticator as stauth


names = ["Muhammad Kashir Khan","Muhammad Daniyal Khan"]

usernames = ["mkashirk", "mdaniyalk"]

passwords = ["abc123", "def456"]


hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "LOGIN.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)