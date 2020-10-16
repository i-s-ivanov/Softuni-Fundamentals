command = input()
company_dict = {}

while command != 'End':
    tokens = command.split(' -> ')
    company = tokens[0]
    employee = tokens[1]
    if company not in company_dict:
        company_dict[company] = []
    if employee in company_dict[company]:
        command = input()
        continue
    company_dict[company].append(employee)
    command = input()

company_dict = dict(sorted(company_dict.items()))
for i in company_dict:
    print(i)
    for x in company_dict[i]:
        print(f'-- {x}')