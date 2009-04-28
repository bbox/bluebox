<?xml version="1.0" encoding="UTF-8"?>
% for user in c.user:
<id>${user.id_usr}</id>
<email>${user.email_usr}</email>
<password>${user.password_usr}</password>
<name>${user.name_usr}</name>
<status>
% if user.status_usr == 0:
	superuser
% else:
	user
% endif
</status>
<team>${user.teamid_usr}</team>
% endfor