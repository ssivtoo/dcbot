import pygsheets
gc = pygsheets.authorize(service_file='dcbudget-ebd6ae3a6cc0.json')

sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1OpOhzSdHlHq2CwH87Sda4UEdf3GCvr9Ez4HIDATOTYc/edit?usp=sharing')

wks_list = sht.worksheets()
print(wks_list)

wks = sht[0]

budget = wks.cell('C1')
print(budget.value)
