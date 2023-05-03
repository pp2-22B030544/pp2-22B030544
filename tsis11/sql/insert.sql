CREATE OR REPLACE PROCEDURE add_one(contact_name VARCHAR(20), contact_number VARCHAR(20))
	AS $$
	DECLARE
		is_exist BOOLEAN;
	BEGIN
		SELECT EXISTS(SELECT Zhanel.number FROM Zhanel WHERE contact_name = Zhanel.name) INTO is_exist;
		
		IF is_exist THEN 
			UPDATE Zhanel SET number = contact_number WHERE Zhanel.name = contact_name;
		ELSE
			INSERT INTO tsis11 (name, number) VALUES (contact_name, contact_number);
		END IF;
		
	END; $$
	LANGUAGE 'plpgsql'
