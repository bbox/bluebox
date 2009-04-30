<?xml version="1.0" encoding="UTF-8"?>
<user>
<id>${c.user.id_usr}</id>
<email>${c.user.email_usr}</email>
<password>${c.user.password_usr}</password>
<name>${c.user.name_usr}</name>
<status>
% if c.user.status_usr == 0:
	superuser
% elif c.user.status_usr ==1:
	admin
% else:
	user
% endif
</status>
<address_usr>${c.user.address_usr}</address_usr>
<phone_usr>${c.user.phone_usr}</phone_usr>
<salary_usr>${c.user.salary_usr}</salary_usr>
<team>${c.user.teamid_usr}</team>
<manager>${c.user.managerid_usr}</manager>
</user>