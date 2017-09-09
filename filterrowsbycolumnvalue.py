class Importable:
    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def event():
        pass

    @staticmethod
    def render(wf_module, table):
        column = wf_module.get_param_column('column')
        value = wf_module.get_param_string('value')
        typeoffilter = wf_module.get_param_menu_string('typeoffilter')

        if column == '' or value == '':
            wf_module.set_ready(notify=False)
            return None
        elif column not in table.columns:
            wf_module.set_error('Invalid column.')
            return None
        else:
            if typeoffilter == 'Keep':
                newtab = table.loc[table[column].astype(str) == value]
            else:
                newtab = table.loc[table[column].astype(str) != value]
            wf_module.set_ready(notify=False)
            return newtab
