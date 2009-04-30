<?xml version="1.0" encoding="UTF-8"?>
<users>
% for user in c.users:
<user>
<id>${user.id_usr}</id>
<email>${user.email_usr}</email>
<password>${user.password_usr}</password>
<name>${user.name_usr}</name>
<status>
% if user.status_usr == 0:
	superuser
% elif user.status_usr ==1:
	admin	
% else:
	user
% endif
</status>
<address_usr>${user.address_usr}</address_usr>
<phone_usr>${user.phone_usr}</phone_usr>
<salary_usr>${user.salary_usr}</salary_usr>
<team>${user.teamid_usr}</team>
<manager>${user.managerid_usr}</manager>
</user>
% endfor
</users>