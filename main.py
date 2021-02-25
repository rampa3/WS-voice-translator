import capture
import csv
import websockets
import asyncio

with open('settings.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)
    lang_processing_settings = next(csv_reader)

    capture.main(int(lang_processing_settings[0]), int(lang_processing_settings[1]), int(lang_processing_settings[2]), str(lang_processing_settings[3]), str(lang_processing_settings[4]))

