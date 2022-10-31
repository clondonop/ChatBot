# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:26:43 2022

@author: asus
"""

from datetime import datetime, timedelta
from chatbot.functions.Chatbot.cal_setup import get_calendar_service


def  create(fecha,hora,cedula,numero,correo,nombre):
   service = get_calendar_service()

   print("en evento",hora)
   tomorrow = datetime( fecha.year,int(fecha.month), fecha.day,hora.hour, hora.minute )
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1)).isoformat()
   summary = 'Cita con ' + nombre + cedula
   des= "Cedula del usuario: "+ cedula +" Numero de contacto: "+numero +" Correo electronico:" + correo
   
   print(des)
   event_result = service.events().insert(calendarId='hntd7birug6tp3gtcblhbq6dpc@group.calendar.google.com',
       body={
           "summary": summary,
           "description": str(des),
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