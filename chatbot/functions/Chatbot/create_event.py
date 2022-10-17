# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:26:43 2022

@author: asus
"""

from datetime import datetime, timedelta
from chatbot.functions.Chatbot.cal_setup import get_calendar_service


def  create(fecha,hora,cedula,numero,correo,nombre):
   # creates one hour event tomorrow 10 AM IST
   service = get_calendar_service()

   d = fecha
   print(fecha.month)
   tomorrow = datetime(fecha.month, fecha.day, fecha.year, hora.hour, hora.minute)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()

   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Automating calendar',
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": start, "timeZone": 'America/Bogota'},
           "end": {"dateTime": end, "timeZone": 'America/Bogota'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   create()