DROP TABLE tx_header CASCADE;
ALTER TABLE tx_header_latest_build RENAME TO tx_header;
DROP TABLE tx_bottom_hole CASCADE;
ALTER TABLE tx_bottom_hole_latest_build RENAME TO tx_bottom_hole;