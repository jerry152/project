
.mode "csv"
.separator ","
.import csv/Referee.csv Referee
.import csv/Fighters.csv Fighters
.import csv/Coaches.csv Coaches
.import csv/Stadium.csv Stadium
.import csv/Region.csv Regions
.import csv/Sponsor.csv Sponsors
.import csv/SponsoredFighter.csv SponsoredFighter


--Insert into Fighters(Max,Teddy Atlas,22/5/1,5, 1,140000,1,11);

--1 choose which boxer is better than the other
SELECT f2.f_name
FROM Fighters f1, Fighters f2
where f1.f_wins < f2.f_wins
and f1.f_name = 'Canelo'
and f2.f_name = 'Manny Pacquiao';
--2 choose which stadium is the biggest
-- SELECT st2.st_name, st2.st_size
-- FROM Stadium st1, Stadium st2
-- where st1.st_size < st2.st_size
-- and st1.st_name = 'MGM Grand Hotel'
-- and st2.st_name = 'Madison Square Garden';
--3 Coach with the most champions
-- SELECT f_coachName, num
-- FROM(
--     SELECT f_coachName, max(c_champions) as num
--     FROM Coaches
--     JOIN Fighters on f_coachName = c_name
-- );
--4 sponsor pays more than current sponsor
-- INSERT INTO Fighters
-- SELECT f_name,f_coachName,f_wins,f_losses,f_salary+s2.s_pay,f_Championships,f_fighterKey,f_cityKey,f_ties
-- FROM Fighters, Sponsors s2
-- JOIN SponsoredFighter ON f_fighterKey = sp_fighterKey
-- JOIN Sponsors s1 on sp_sponsorKey = s1.s_sponsorKey
-- WHERE s2.s_pay > s1.s_pay
-- AND f_name = 'Tyson Fury';

--5 fighter got hired to fight at new stadium (moved to a new city)
-- UPDATE Fighters
-- SET f_cityKey = (
--     SELECT st2.st_cityKey
--     FROM Fighters, Stadium st2
--     JOIN Stadium st1 on f_cityKey = st1.st_cityKey
--     WHERE st2.st_size > st1.st_size
--     )
-- WHERE f_name = 'Tyson Fury'
-- AND f_salary > 361800;
--6 Biggest stadium in a region
-- SELECT st_name, MAX(st_size) as size
-- FROM Stadium
-- JOIN Regions on st_cityKey = r_cityKey
-- WHERE r_country = 'USA';
--7 Which fighters does a coach have
-- SELECT f_coachName, f_name
-- FROM Fighters
-- GROUP BY f_name
-- ORDER BY f_coachName ASC;
--8 sponsor with the most pay
-- SELECT s_name, max(s_pay)
-- FROM Sponsors;
--9 How many matches have refs done in the USA
-- SELECT sum(rf_matches)
-- FROM Referee
-- JOIN Regions on rf_citykey = r_cityKey
-- WHERE r_country = 'USA';
--10 Best fighter outside USA
SELECT f_name,max(f_wins)
FROM Fighters
JOIN Regions on f_cityKey = r_cityKey
WHERE r_country != 'USA';
--11 Which ref has been at the biggest stadium
-- SELECT st_refName
-- FROM(
--     SELECT st_refName, max(st_size)
--     FROM Stadium
--     );
--12 Changing Canelo to full name
-- UPDATE Fighters
-- SET f_name = 'Saul Canelo Alvarez'
-- WHERE f_name = 'Canelo';
--13 Which sponsor televises an American fighter and what city are they from
-- SELECT s_name, r_name
-- FROM Sponsors
-- JOIN SponsoredFighter on s_sponsorKey = sp_sponsorKey
-- JOIN Fighters on sp_fighterKey = f_fighterKey
-- JOIN Regions on f_cityKey = r_cityKey
-- WHERE r_country = 'USA'
-- AND s_televised = 'yes';
--14 adding sponsors that dont require clothing
-- INSERT INTO SponsoredFighter
-- SELECT f_fighterKey, s_sponsorKey
-- FROM Fighters, Sponsors
-- WHERE s_clothingRequired = 'no'
-- AND f_name = 'Saul Canelo Alvarez';
-- --15 Which coach has the most fighters and which of their fighters have the best wins
-- SELECT c_name, max(f_wins)
-- FROM Fighters, Coaches
-- WHERE f_coachName IN (
--     SELECT c_name
--     FROM(
--         SELECT c_name, max(c_numFighters)
--         FROM Coaches
--     )
-- );
--16 Which fighter has the best win to loss ratio
-- SELECT f_name
-- FROM(
--     SELECT f_name, max(f_wins/f_losses)
--     FROM Fighters
-- );
-- --17 nike wants to sponsor all fighters who have at least 4 championships
-- INSERT INTO SponsoredFighter
-- SELECT f_fighterKey, s_sponsorKey
-- FROM Fighters, Sponsors
-- WHERE s_name = 'nike'
-- AND f_Championships >= 4;
-- --18 Boxer wants to get sponsored by anyone who doesnt get televised
-- INSERT INTO SponsoredFighter
-- SELECT f_fighterKey, s_sponsorKey
-- FROM Fighters, Sponsors
-- WHERE f_name = 'Boxer'
-- AND s_televised = 'no';
-- --19 budlight wants to sponsor all of Floyd Mayweather Sr's fighters
-- INSERT INTO SponsoredFighter
-- SELECT f_fighterKey, s_sponsorKey
-- FROM Fighters, Sponsors
-- WHERE f_coachName = 'Floyd Mayweather Sr'
-- AND s_name = 'budlight';
-- --20 corona wants to sponsor all fighters that belong to a stadium that can seat more than 50000 people
-- INSERT INTO SponsoredFighter
-- SELECT f_fighterKey, s_sponsorKey
-- FROM Fighters, Sponsors
-- JOIN Stadium on f_cityKey = st_cityKey
-- WHERE st_size > 50000
-- AND s_name = 'corona';

-- --21 deleting dupicates
-- -- DELETE from Fighters
-- -- where f_salary < (select Max(f_salary)
-- -- from Fighters
-- -- where f_name = 'Tyson Fury');

-- -- 22 averge winrate for fighters in the uk 
-- select avg(f_wins)
-- from Fighters, Regions
-- where f_cityKey = r_cityKey
-- and r_cityKey = 3;

-- --23fighers where the coach as the least amount of champions
-- select f_name, c_name, min(c_champions)
-- from Fighters, Coaches
-- where c_name = f_coachName;

-- -- 24 total amount of money made for all sponsers for canelo
-- select sum(s_pay)
-- FROM Fighters, Sponsors, SponsoredFighter
-- where f_name = 'Saul Canelo Alvarez'
-- and s_sponsorKey = sp_sponsorKey
-- and f_fighterKey = sp_fighterKey
-- ;

-- --25 insert new fighter from russia aslo addd new region
-- INSERT INTO Fighters 
-- VALUES('Max','Teddy Atlas', 21, 4.00,74000.00,0.00,11,11,4.00);
-- INSERT INTO Regions
-- VALUES(10,'Moscow','Moscow','Russia');

-- --testing ideas simple queries
-- SELECT total(st_size)
-- from Stadium;

-- SELECT max(st_size)
-- from Stadium;



-- --staiums bigger than mgm grand hotel
-- SELECT st_name, st_size
-- from Stadium 
-- where st_size > (select st_size
-- from Stadium
-- where st_name = 'MGM Grand Hotel') 
-- ;

SELECT c_name , f_name, Max(f_wins)
FROM Fighters, Coaches
WHERE c_name = 'Freddie Roach'
and f_coachName = c_name;

SELECT r_name, r_state, r_country
FROM  Coaches, Regions
WHERE c_name = 'Chepo Reynoso'
and c_citykey = r_cityKey;

SELECT COUNT(DISTINCT f_name)
FROM Fighters;

-- SELECT c_name, max(f_wins), f_name
-- FROM Fighters, Coaches
-- WHERE f_coachName IN (
--     SELECT c_name
--     FROM(
--         SELECT c_name, max(c_numFighters)
--         FROM Coaches,Fighters
        
--     )
--     where f_name = 'Mike Tyson'
-- );

