--This query will calculate number of wells on lease from oglease column and insert them into nwells column
-- Run daily
UPDATE tx_header_latest_build --change this to the table you want to update
SET nwells = subquery.nwells 
FROM
	( SELECT oglease, COUNT ( oglease ) AS nwells FROM tx_header_latest_build GROUP BY oglease ) AS subquery --change FROM table to the table you want to update
WHERE
	tx_header_latest_build.oglease = subquery.oglease --change this to the table you want to update
	AND tx_header_latest_build.oglease IS NOT NULL; --change this to the table you want to update