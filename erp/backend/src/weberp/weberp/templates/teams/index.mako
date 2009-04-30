<?xml version="1.0" encoding="UTF-8"?>
<teams>
	% for team in c.teams:
	<team>
		<id>${team.id_tms}</id>
		<name>${team.name_tms}</name>
		<manager>${team.managerid_tms}</manager>
		<users>
		% for user in team.users:
			<user>
			  <id>${user.id_usr}</id>
			  <name>${user.name_usr}</name>
			</user>
		%endfor
		</users>
	</team>
	% endfor
</teams>