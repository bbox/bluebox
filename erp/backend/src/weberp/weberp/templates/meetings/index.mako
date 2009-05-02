<?xml version="1.0" encoding="UTF-8"?>
<response status="ok">
% for meeting in c.meetings:
	<meeting>
		<id>${meeting.id_met}</id>
		<subject>${meeting.subject_met}</subject>
		<participants>${meeting.participants_met}</participants>
		<location>${meeting.location_met}</location>
		<owner>${meeting.owner_met}</owner>
		<start>${meeting.start_met}</start>
		<end>${meeting.end_met}</end>
		<notes>${meeting.notes_met}</notes>
	</meeting>
% endfor
</response>