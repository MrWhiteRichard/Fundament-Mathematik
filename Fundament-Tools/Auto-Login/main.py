from outsource import *

site = get_site()
discord_name = get_discord_name(site)
matriculation_number, private_path, password = get_login_data(site, discord_name)
drive(site, discord_name, matriculation_number, private_path, password)