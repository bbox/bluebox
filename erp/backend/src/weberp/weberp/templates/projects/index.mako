<?xml version="1.0" encoding="UTF-8"?>
<response status="ok">
	<projects>
	% for project in c.projects:
		<project>
			<id>${project.id_prj}</id>
			<name>${project.name_prj}</name>
			<added_by>${project.added_by_prj}</added_by>
			<owned_by>${project.owned_by_prj}</owned_by>
			<startdate>${project.startdate_prj}</startdate>
			<enddate>${project.enddate_prj}</enddate>
			<documents>
				% for doc in project.documents:
					<document>
						<name>${doc.name_doc}</document>
					</document>
				% endfor
			</documents>
		</project>
	% endfor
	</projects>
</response>