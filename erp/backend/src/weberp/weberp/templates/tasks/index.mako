<?xml version="1.0" encoding="UTF-8"?>
<response status="ok">
	<tasks>
		% for task in c.tasks:
		<task>
			<id>${task.id_tsk}</id>
			
			<projectid>${task.idprj_tsk}</projectid>
			<projectname>${task.project.name_prj}</projectname>
			<name>${task.title_tsk}</name>
			<description>${task.description_tsk}</description>			
			<addedby>${task.added_by_tsk}</addedby>
			% if task.owner is not None:
			<addedby_name>${task.owner.name_usr}</addedby_name>
			% else:
			<addedby_name></addedby_name>
			% endif
			<assignedto>${task.assignedto_tsk}</assignedto>
			% if task.assignee is not None:
			<assignedto_name>${task.assignee.name_usr}</assignedto_name>
			%else:
			<assignedto_name></assignedto_name>
			% endif
			% if task.timeleft_tsk is None:
				<timeleft>0h</timeleft>
			% else:
				<timeleft>0h</timeleft>
			% endif
			<status>${task.status_tsk}</status>
			<startedon>${task.starton_tsk}</startedon>
			<endon>${task.endon_tsk}</endon>		
		</task>
		% endfor
	</tasks>
</response>