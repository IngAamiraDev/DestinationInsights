
primary_country_cod = ['DE','AR','AU','AT','BE','CA','CZ','CN','CY','CO','KR','HR','DK','EG','AE','ES','US','FI','FR','GR','IN','IE','IL','IT','JP','MA','MX','NO','NL','PL','PT','GB','RU','SE','CH','TN','TR']
primary_country_id = ['select_option_637','select_option_565','select_option_568','select_option_569','select_option_575','select_option_593','select_option_612','select_option_600','select_option_611','select_option_603','select_option_761','select_option_608','select_option_614','select_option_619','select_option_790','select_option_763','select_option_792','select_option_630','select_option_631','select_option_640','select_option_656','select_option_660','select_option_662','select_option_663','select_option_665','select_option_701','select_option_695','select_option_718','select_option_707','select_option_729','select_option_730','select_option_791','select_option_736','select_option_768','select_option_769','select_option_782','select_option_783']

country_cod = ['CO','KR','HR','DK']


dic_country = {
    'Country_Cod': primary_country_cod,
    'Country_Id': primary_country_id
}


def lookup_country(dic_country, country_cod):
    try:
        return dic_country[country_cod]
    except KeyError:
        return {k:v for k,v in dic_country.items()}


print(lookup_country(dic_country, country_cod))