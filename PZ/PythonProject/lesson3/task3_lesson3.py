def thesaurus_adv(*args):
    name_dict = dict()
    for names in args:
        f_name = names.split()[0][0]
        surname = names.split()[1][0]
        if surname not in name_dict:
            name_dict[surname] = {f_name: [names]}
        elif f_name in name_dict[surname]:
            name_dict[surname][f_name].append(names)
        else:
            name_dict[surname][f_name] = [names]
    return name_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
