<?xml version="1.0" encoding="UTF-8"?>
<response status="ok">
	<documents>
		% for document in c.documents:
			<document>
				<id>${document.id_doc}</id>
				<project>
					<id>${document.project.id_prj}</id>
					<name>${document.project.name_prj}</name>
				</project>
				<name>${document.name_doc}</name>
				<file>${document.file_doc}</file>
			</document>
		% endfor
	</documents>
</response>