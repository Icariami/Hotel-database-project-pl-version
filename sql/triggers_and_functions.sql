
CREATE OR REPLACE FUNCTION check_review_rating()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.rating BETWEEN 1 AND 10 THEN
        RETURN NEW;
    ELSE
        RAISE EXCEPTION 'Ocena powinna być w zakresie 1-10. Popraw wprowadzone dane.';
        RETURN NULL;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- end

CREATE TRIGGER check_review_rating_trigger
BEFORE INSERT ON Hotel.Review
FOR EACH ROW EXECUTE FUNCTION check_review_rating();

-- end

CREATE OR REPLACE FUNCTION check_booking()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM Hotel.Booking b
        WHERE NEW.room_ID = b.room_ID
          AND (
            (NEW.check_in_date BETWEEN b.check_in_date AND b.check_out_date)
            OR (NEW.check_out_date BETWEEN b.check_in_date AND b.check_out_date)
          )
    ) THEN
        RAISE EXCEPTION 'Pokój jest już zajęty w podanym terminie.';
        RETURN NULL;
    ELSE
        RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- end

CREATE TRIGGER check_booking_trigger
BEFORE INSERT ON Hotel.Booking
FOR EACH ROW EXECUTE FUNCTION check_booking();

-- end