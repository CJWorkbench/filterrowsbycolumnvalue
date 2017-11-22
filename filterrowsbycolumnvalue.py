def render(table, params):
    column = params['column']
    value = params['value']
    typeoffilter = params['typeoffilter']

    if column == '' or value == '':
        return table
    else:
        if typeoffilter == 'Keep':
            newtab = table.loc[table[column].astype(str) == value]
        else:
            newtab = table.loc[table[column].astype(str) != value]
        return newtab
