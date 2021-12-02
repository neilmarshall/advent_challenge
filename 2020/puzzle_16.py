import re
from functools import reduce
from itertools import chain
from operator import __mul__

def parse_note(s):
    m = re.match(r"^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$", s, re.I)
    return m.group(1), (range(int(m.group(2)), int(m.group(3)) + 1), range(int(m.group(4)), int(m.group(5)) + 1))


def find_invalid_tickets(notes, *tickets):
    values = set(n for r in chain.from_iterable(notes.values()) for n in r)
    return reduce(lambda a, c: a + sum(t for t in c if t not in values), tickets, 0)


def map_fields(notes, *tickets):
    valid_values = set(n for r in chain.from_iterable(notes.values()) for n in r)
    def is_valid_ticket(valid_values, ticket):
        return all(t in valid_values for t in ticket)
    tickets = list(filter(lambda t: is_valid_ticket(valid_values, t), tickets))
    notes = {d: set(chain(r1, r2)) for (d, (r1, r2)) in notes.items()}
    fields = {}
    for i in range(len(tickets[0])):
        values = [ticket[i] for ticket in tickets]
        for note in notes:
            if all(t in notes[note] for t in values):
                if i not in fields:
                    fields[i] = set()
                fields[i].add(note)
    def reduce_map(fields, keys):
        if any(len(fields[f]) > 1 for f in fields):
            for key in keys:
                if sum(1 for f in fields if key in fields[f]) == 1:
                    field = next(filter(lambda f: key in fields[f], fields))
                    fields[field] = set((key,))
            return reduce_map(fields,keys)
        return fields
    return {k: v.pop() for k, v in reduce_map(fields, list(notes.keys())).items()}


if __name__ == '__main__':
    with open('./input/input_16.txt') as f:
        tickets = [[int(n) for n in r.split(',')] for r in f.readlines()]
    ticket = [137, 173, 167, 139, 73, 67, 61, 179, 103, 113, 163, 71, 97, 101, 109, 59, 131, 127, 107, 53]
    notes = ["departure location: 33-430 or 456-967",
             "departure station: 42-864 or 875-957",
             "departure platform: 42-805 or 821-968",
             "departure track: 34-74 or 93-967",
             "departure date: 40-399 or 417-955",
             "departure time: 30-774 or 797-950",
             "arrival location: 50-487 or 507-954",
             "arrival station: 34-693 or 718-956",
             "arrival platform: 42-729 or 751-959",
             "arrival track: 28-340 or 349-968",
             "class: 49-524 or 543-951",
             "duration: 40-372 or 397-951",
             "price: 48-922 or 939-951",
             "route: 33-642 or 666-960",
             "row: 39-238 or 255-973",
             "seat: 48-148 or 161-973",
             "train: 50-604 or 630-971",
             "type: 29-299 or 316-952",
             "wagon: 45-898 or 921-966",
             "zone: 34-188 or 212-959"]
    print(find_invalid_tickets({d: r for d, r in map(parse_note, notes)}, *tickets))  # 26026
    fields = map_fields({d: r for d, r in map(parse_note, notes)}, *tickets)
    print(reduce(__mul__, (ticket[i] for i in (f for f in fields if fields[f].startswith('departure'))), 1))  # 1305243193339
