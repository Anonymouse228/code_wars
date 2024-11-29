from collections import namedtuple


def format_duration(time):
    if time == 0:
        return 'now'

    Period = namedtuple('Period', ['singular', 'plural', 'max_value'])

    periods = (
        Period(singular='second', plural='seconds', max_value=60),
        Period(singular='minute', plural='minutes', max_value=60),
        Period(singular='hour', plural='hours', max_value=24),
        Period(singular='day', plural='days', max_value=365),
        Period(singular='year', plural='years', max_value=float('inf')),
    )
    separators = (', ', ', ', ', ', ', ', ' and ')[::-1]
    last_used_separator = ''
    sep_i = 0

    answer = ''

    for period in periods:
        time, duration = divmod(time, period.max_value)

        if duration == 0:
            continue

        answer = f'{separators[sep_i]}{int(duration)} {period.singular if duration == 1 else period.plural}{answer}'
        last_used_separator = separators[sep_i]
        sep_i += 1

    return answer[len(last_used_separator):]


# for i in range(10000, 100000):
#     print(format_duration(i))

print(format_duration(101))
