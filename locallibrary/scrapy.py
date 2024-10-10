
# fieldsets is a tuple, the key is either 'None' or 'Availability'
# the values are a dictionary
# the whole thing is a dictionary inside a tuple inside a list
fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )

print(type(fieldsets))

# for key, value in fieldsets:
#     print(key, value)
# for item in fieldsets:
#     print(item)


for key, value in fieldsets:
    if key == None or 'Availability':
        print(value['fields'])