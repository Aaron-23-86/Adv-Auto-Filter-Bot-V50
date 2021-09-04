#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

class Translation(object):
    
    START_TEXT = """<b>Hey {}!!</b>
<i>

You can call this as an Auto Filter Bot 

This is Version 2 of Auto Filter Bot

Bot gives button link to files in connected channels on query !

No need to add filters for your files or movies from now on!


</i>"""    
    
    HELP_TEXT = """
<b><i><u>How To Use Me!?</u></i></b>

<i>
-> Add Me To Any Group And Make Me Admin
-> Add Me To Your Desired Channel
</i>

<b>Bot Commands (Works Only In Groups) :</b>

    -> <code>/add chat_id</code>
                OR                  - To Connect A Group With A Channel (Bot Should Be Admin With Full Previlages In Both Group And Channel)
     <code>/add @Username</code>
     
    -> <code>/del chat_id</code>
                OR                  - To disconnect A Group With A Channel
     <code>/del @Username</code>
     
    -> <code>/delall</code>  - This Command Will Disconnect All Connected Channel With The Group And Deletes All Its File From DB
    
    -> <code>/settings</code> -  This Command Will Display You A Settings Pannel Instance Which Can Be Used To Tweek Bot's Settings Accordingly

            -> <code>Channel</code> - Button Will Show You All The Connected Chats With The Group And Will Show Buttons Correspnding To There Order For Furthur Controls
            
            -> <code>Filter Types</code> - Button Will Show You The 3 Filter Option Available In Bot... Pressing Each Buttons Will Either Enable or Disable Them And This Will Take Into Action As Soon As You Use Them Without The Need Of A Restart

            -> <code>Configure</code> - Button Will Helps You To Change No. of Pages/ Buttons Per Page/ Total Result Without Acutally Editing The Repo... Also It Provide Option To Enable/Disable For Showing Invite Link In Each Results
            
            -> <code>Status</code> - Button Will Shows The Stats Of Your Channel
            

"""
    
    ABOUT_TEXT = """<b>➥ Name</b> : <code> Auto Filter Bot</code>
    
<b>➥ Creator</b> : <b><i><a href="https://t.me/Termin_a_t_o_r">Aaron</a></i></b>

<b>➥ Language</b> : <code>Python3</code>

<b>➥ Library</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>

<b>➥ Channel</b> : <i><a href="https://t.me/hollywood_only">Click Me</a></i>
"""
