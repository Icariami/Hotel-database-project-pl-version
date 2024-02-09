create schema Hotel;

-- Tabela przedstawiająca hotel
-- W poniższej bazie operuję na jednym hotelu (o id=1)
CREATE TABLE IF NOT EXISTS Hotel.Hotel
(
    hotel_ID serial PRIMARY KEY,
    name character varying(30) NOT NULL,
    address character varying(100) NOT NULL,
    phone_number character varying(12) NOT NULL,
    e_mail character varying(50) NOT NULL,
    description text,
    star_rating int not null
);

-- Rodzaj pokoju - nazwa, opis, cena za noc, czy można nocować ze zwierzakiem, i ilu-osobowy jest pokój
CREATE TABLE IF NOT EXISTS Hotel.Room_type
(
    room_type_ID serial PRIMARY KEY,
    name character varying(50) NOT NULL,
    description text,
    price_per_night numeric(6, 2) NOT NULL,
    pet_friendly boolean NOT NULL DEFAULT false,
    capacity integer NOT NULL
);

-- Pokój - jakiego jest rodzaju, numer na drzwiach oraz w jakim hotelu się znajduje
CREATE TABLE IF NOT EXISTS Hotel.Room
(
    room_ID serial PRIMARY KEY,
    room_type integer NOT NULL references Hotel.Room_type,
    door_number integer NOT NULL,
    hotel_ID integer NOT NULL references Hotel.Hotel
);

-- Gość - Imię, nazwisko, numer telefonu i adres e-mail
CREATE TABLE IF NOT EXISTS Hotel.Guest
(
    guest_ID serial NOT NULL PRIMARY KEY,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    phone_number character varying(12) NOT NULL,
    e_mail character varying(50) NOT NULL
);

-- Rezerwacja na pobyt w hotelu z datami zameldowania i wymeldowania
CREATE TABLE IF NOT EXISTS Hotel.Booking
(
    booking_ID serial PRIMARY KEY,
    room_ID integer NOT NULL references Hotel.Room,
    guest_ID integer NOT NULL references Hotel.Guest,
    check_in_date date NOT NULL,
    check_out_date date NOT NULL
);

-- Usługi realizowane w ramach pobytu w hotelu ale dodatkowo płatne
CREATE TABLE IF NOT EXISTS Hotel.Service
(
    service_ID serial PRIMARY KEY,
    name character varying(30) NOT NULL,
    description text,
    price numeric(5, 2) NOT NULL
);

-- Tabela wykorzystanych usług w czasie danego pobytu w hotelu
CREATE TABLE IF NOT EXISTS Hotel.Booked_service
(
    Booked_service_ID serial PRIMARY KEY,
    booking_ID integer NOT NULL references Hotel.Booking,
    service_ID integer NOT NULL references Hotel.Service
);

-- Opinia o usługach realizowanych w hotelu
CREATE TABLE IF NOT EXISTS Hotel.Review
(
    review_ID serial PRIMARY KEY,
    booking_ID integer references Hotel.Booking,
    booked_service_ID integer references Hotel.Booked_service(booked_service_ID),
    rating integer NOT NULL,
    review_text text
);

INSERT INTO Hotel.Hotel (name, address, phone_number, e_mail, description, star_rating) 
VALUES 
('Chata', 'ul. Zimowa 18, 
30-101, Zimów, Polska', '101202303', 'chata@kontakt.com', 'Chata to urokliwy hotel położony w malowniczym otoczeniu gór.\n 
Nasz hotel oferuje niezapomniane doświadczenia w zimowej scenerii, w otoczeniu białego puchu i zapierających dech w piersiach widoków.\n
Znajdujemy się z dala od zgiełku miasta, w sercu górskiej natury, zapewniając naszym gościom spokój i odprężenie.\n
Wnętrza Chaty emanują ciepłem kominka i rustykalnym urokiem, tworząc idealną atmosferę do relaksu po dniu spędzonym na stokach lub na górskich wędrówkach.\n
Zapraszamy do Chaty - gdzie natura i komfort spotykają się, by stworzyć niezapomniane wspomnienia górskiego pobytu.', 4);

INSERT INTO Hotel.Room_type (name, description, price_per_night, pet_friendly, capacity) VALUES 
('Pokój standard', 'Przytulny pokój z widokiem na góry dla dwóch osób, z pojedynczymi łóżkami i łazienką', 150.00, true, 2),
('Apartament premium', 'Przestrzenny apartament z salonem i sypialnią z podwójnym łóżkiem, oraz dużym balkonem', 300.00, false, 2),
('Apartament rodzinny 2+2', 'Pokój z dwuosobowym łóżkiem dla rodziców, połączony z pokojem z dwoma osobnymi łóżkami dla dzieci, ze wspólną łazienką', 270.00, true, 4),
('Pokój standard 3 - osobowy', 'Pokój z trzema pojedynczymi łóżkami i łazienką', 225.00, false, 3),
('Pokój standard 4 - osobowy', 'Pokój z czterema pojedynczymi łóżkami, balkonem z widokiem na góry i łazienką', 290.00, false, 4);

INSERT INTO Hotel.Room (room_type, door_number, hotel_ID) VALUES 
(1, 101, 1),
(1, 102, 1),
(1, 103, 1),
(2, 201, 1),
(2, 202, 1),
(2, 203, 1),
(3, 301, 1),
(3, 302, 1),
(3, 303, 1),
(4, 401, 1),
(4, 402, 1),
(4, 403, 1),
(5, 501, 1),
(5, 502, 1),
(5, 503, 1);

INSERT INTO Hotel.Guest (first_name, last_name, phone_number, e_mail) VALUES 
('Jan', 'Kowalski', '123456789', 'jan.kowalski@gmail.com'),
('Anna', 'Nowak', '987654321', 'anna.nowak@gmail.com'),
('Piotr', 'Wiśniewski', '555444333', 'piotr.wisniewski@gmail.com'),
('Maria', 'Dąbrowska', '111222333', 'maria.dabrowska@gmail.com'),
('Aleksandra', 'Kowalczyk', '999888777', 'aleksandra.kowalczyk@gmail.com'),
('Tomasz', 'Lewandowski', '333222111', 'tomasz.lewandowski@gmail.com'),
('Magdalena', 'Zając', '444555666', 'magdalena.zajac@gmail.com'),
('Wojciech', 'Szymański', '777888999', 'wojciech.szymanski@gmail.com'),
('Alicja', 'Woźniak', '666777888', 'alicja.wozniak@gmail.com'),
('Kamil', 'Jankowski', '111333555', 'kamil.jankowski@gmail.com'),
('Martyna', 'Kaczmarek', '999111222', 'martyna.kaczmarek@gmail.com'),
('Paweł', 'Mazur', '444666888', 'pawel.mazur@gmail.com');

INSERT INTO Hotel.Booking (room_ID, guest_ID, check_in_date, check_out_date) VALUES 
(1, 1, '2023-01-10', '2023-01-17'), --1
(3, 5, '2023-03-02', '2023-03-10'), --2
(2, 8, '2023-04-20', '2023-04-25'), --3
(5, 11, '2023-05-15', '2023-05-20'), --4
(4, 6, '2023-06-10', '2023-06-15'), --5
(6, 9, '2023-07-05', '2023-07-10'), --6
(10, 12, '2023-08-30', '2023-09-04'), --7
(3, 7, '2023-09-25', '2023-09-30'), --8
(1, 1, '2023-02-22', '2023-02-25'), --9
(2, 2, '2023-03-15', '2023-03-27'), --10
(3, 3, '2023-04-30', '2023-05-02'), --11
(4, 4, '2023-05-24', '2023-05-30'), --12
(5, 5, '2023-06-23', '2023-06-25'), --13
(6, 6, '2023-07-18', '2023-07-20'), --14
(7, 7, '2023-08-30', '2023-09-04'), --15
(8, 8, '2023-09-16', '2023-09-30'), --16
(9, 9, '2023-10-20', '2023-10-27'), --17
(10, 10, '2023-11-15', '2023-11-20'), --18
(11, 11, '2023-12-30', '2024-01-04'), --19
(12, 12, '2024-01-25', '2024-01-30'), --20
(13, 1, '2024-02-16', '2024-02-25'), --21
(14, 2, '2024-03-15', '2024-03-23'), --22
(15, 3, '2024-04-25', '2024-05-05'); --23


INSERT INTO Hotel.Service (name, description, price) VALUES 
('Góralskie śniadanie', 'Szwedzki stół z tradycyjnymi daniami z lokalnych produktów', 20.00),
('Masaż relaksacyjny', 'Profesjonalny masaż dla odprężenia - 1 godzina', 50.00),
('Basen', 'Dostęp do basenu z dwoma 25-metrowymi torami, basenu rekreacyjnego oraz jacuzzi', 60.00),
('Sauna', 'Dostęp do dwóch saun - suchej i mokrej', 60.00),
('Sauna + basen', 'Pakiet saun oraz basenów', 100.00);

INSERT INTO Hotel.Booked_service (booking_ID, service_ID) VALUES 
(1, 1),
(1, 2),
(2, 3),
(3, 5),
(4, 1),
(4, 2),
(5, 3),
(6, 5),
(7, 1),
(7, 2),
(7, 4),
(8, 1),
(9, 4),
(10, 3);


INSERT INTO Hotel.Review (booking_ID, booked_service_ID, rating, review_text)
VALUES 
(1, 1, 5, 'Świetne śniadanie! Bardzo smaczne i urozmaicone posiłki.'),
(2, 3, 4, 'Basen utrzymany w dobrym stanie, przestronny i przyjemna.'),
(3, 4, 4, 'Bardzo relaksujący basen i sauna, świetne miejsce na odpoczynek.'),
(4, 6, 5, 'Masaż był rewelacyjny, kompletnie się zrelaksowałem.'),
(5, 7, 4, 'Świetny basen, odpowiedni dla małych jak i większych dzieci.'),
(6, 8, 3, 'Basen był OK, ale sauna mogłaby być lepiej utrzymana.'),
(7, 10, 5, 'Masaż był doskonały, polecam każdemu!'),
(8, 12, 4, 'Smaczne śniadanie, świetny wybór dań.'),
(9, 13, 5, 'Super sauny i balie z lodowatą wodą.'),
(10, 14, 3, 'Basen był OK, jednak oczekiwałem czegoś więcej.');



-- WIDOKI 

-- Zestawienie gości, którzy skorzystali z którejś usługi oraz wystawili o niej opinię
CREATE VIEW Guest_Service_Reservations_With_Reviews AS
SELECT
	g.first_name AS Imię_gościa,
    g.last_name AS Nazwisko_gościa,
    s.name AS nazwa_wykorzystanej_usługi,
    rv.rating AS ocena,
    rv.review_text as opinia
FROM
    Hotel.Guest g
JOIN
    Hotel.Booking b ON g.guest_ID = b.guest_ID
LEFT JOIN
    Hotel.Booked_service bs ON b.booking_ID = bs.booking_ID
LEFT JOIN
    Hotel.Service s ON bs.service_ID = s.service_ID
LEFT JOIN
    Hotel.Review rv ON b.booking_ID = rv.booking_ID AND bs.booked_service_ID = rv.booked_service_ID
where bs.service_ID is not null and rv.review_ID is not null;



-- Zestawienie przychodów dla hotelu Chata w roku 2023. Płatności za pobyt są dokonywane przed rozpoczęciem pobytu w hotelu.
CREATE VIEW Monthly_revenue AS
SELECT
    EXTRACT(MONTH FROM b.check_in_date) AS miesiąc,
    SUM(rt.price_per_night * (b.check_out_date - b.check_in_date)) AS Przychód_za_pokoje,
    COALESCE(SUM(s.price),0) AS Przychód_za_usługi,
	SUM(rt.price_per_night * (b.check_out_date - b.check_in_date) + COALESCE(s.price, 0)) as Całkowity_przychód
FROM
    Hotel.Booking b
JOIN
    Hotel.Room r ON b.room_ID = r.room_ID
JOIN
    Hotel.Room_type rt ON r.room_type = rt.room_type_ID
JOIN
    Hotel.Hotel h ON r.hotel_ID = h.hotel_ID
LEFT JOIN
    Hotel.Booked_service bs ON b.booking_ID = bs.booking_ID
LEFT JOIN
    Hotel.Service s ON bs.service_ID = s.service_ID
WHERE
    h.hotel_ID = 1 and EXTRACT(YEAR FROM b.check_in_date) = 2023
GROUP BY
    EXTRACT(MONTH FROM b.check_in_date)
ORDER BY
    EXTRACT(MONTH FROM b.check_in_date);


-- Zestawienie
CREATE VIEW Average_duration_of_stay AS
SELECT
    g.first_name as imię_gościa,
    g.last_name as nazwisko_gościa,
	COUNT(DISTINCT b.booking_ID) as liczba_pobytów_w_hotelu,
    round(cast(AVG(b.check_out_date - b.check_in_date) as numeric), 2) AS średnia_liczba_dni_pobytu
FROM
    Hotel.Guest g
JOIN
    Hotel.Booking b ON g.guest_ID = b.guest_ID
GROUP BY
    g.first_name, g.last_name
HAVING
     COUNT(DISTINCT b.booking_ID) >= 2
ORDER BY
    g.last_name;
