<?xml version="1.0" encoding="UTF-8"?>
<response status="ok">
	<tasks>
		% for task in c.tasks:
		<task>
			<id>${task.id_tsk}</id>
			
			<projectid>${task.idprj_tsk}</projectid>
			<name>${task.title_tsk}</name>
			<description>${task.description_tsk}</description>			
			<addedby>${task.added_by_tsk}</addedby>
			<addedby_name>
			% if task.owner is not None:
			${task.owner.name_usr}
			% endif
			</addedby_name>
			<assignedto>${task.assignedto_tsk}</assignedto>
			<assignedto_name>
			% if task.assignee is not None:
			${task.assignee.name_usr}
			% endif
			</assignedto_name>
			<timeleft>
			% if task.timeleft_tsk is None:
			0h
			% else:
			${task.timeleft_tsk}h
			% endif
			</timeleft>
			<status>${task.status_tsk}</status>
			<startedon>${task.starton_tsk}</startedon>
			<endon>${task.endon_tsk}</endon>		
		</task>
		% endfor
	</tasks>
</response>