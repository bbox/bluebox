<?xml version="1.0" encoding="UTF-8"?>
<response status="ok">
	<messages>
		% for message in c.messages:
			<message>
				<id>${message.id_msg}</id>
				<from>${message.from_msg}</from>
				<to>${message.to_msg}</to>
				<title>${message.title_msg}</title>
				<body>${message.body_msg}</body>
				<expeditor>${message.expeditor.name_usr}</expeditor>
				<destinatar>${message.destinatar.name_usr}</destinatar>
			</message>
		%endfor
	</messages>
</response>