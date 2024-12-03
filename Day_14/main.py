from prettytable import PrettyTable

table = PrettyTable()
# table.align = 'r'

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Psyduck", "Water"])
table.add_row(["Lucario", "Fighting · Steel"])
print(table)

