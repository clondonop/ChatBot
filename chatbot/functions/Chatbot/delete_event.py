from operator import contains
from chatbot.functions.Chatbot.cal_setup import get_calendar_service

def delete(cedula):
    # Delete the event
    service = get_calendar_service()
    id = None
    while id is None :
        events = service.events().list(calendarId='hntd7birug6tp3gtcblhbq6dpc@group.calendar.google.com', timeMin= '2022-01-01T00:00:00Z').execute()
        for event in events['items']:
            print("evento",event)
            if  cedula in event['summary']:
                id= event['id']
                break
    print(id)
    try:
        service.events().delete(
            calendarId='hntd7birug6tp3gtcblhbq6dpc@group.calendar.google.com',
            eventId=id,
        ).execute()
    except:
        print("Failed to delete event")

    return("Cita cancelada")

if __name__ == '__main__':
    delete()