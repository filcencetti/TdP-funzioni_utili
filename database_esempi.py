# selezionare tutte le gare di una stagione
"""
select *
from races r
where `year` = %s
"""

#numero di piloti che hanno corso in entrambe le gare adiacenti all’arco,
# e che sono giunti al traguardo (cioè results.statusId=1).
"""
#select r1.raceId as gara1Id, r2.raceId as gara2Id, count(*) as peso
from races r1, races r2, results re1, results re2
where r2.`year` = r1.`year` 
and re1.raceId = r1.raceId and re2.raceId = r2.raceId 
and re2.driverId = re1.driverId
and re2.raceId < re1.raceId
and r1.`year` = %s
and re2.statusId = 1
and re1.statusId = 1
group by r1.raceId, r2.raceId 
order by peso desc
"""

#selezionare i piloti che hanno partecipato alle gare
#considerate ed hanno tagliato il traguardo
"""
#select distinct d.*
from results r , races r2 , drivers d 
where r.raceId = r2.raceId 
and d.driverId = r.driverId 
and r.`position` is not null 
and r2.`year` = %s
"""

#Un arco orientato rappresenta la vittoria di un pilota su un altro,
# con peso pari al numero di gare in cui tale vittoria si è verificata
"""
#select r.driverId as driver1Id, r2.driverId as driver2Id, count(*) as peso
from results r , results r2 , races ra
where ra.`year` = %s
and r2.raceId = ra.raceId 
and r.raceId = r2.raceId 
and r2.`position` is not null 
and r.`position` is not null 
and r.`position` < r2.`position` 
group by r.driverId, r2.driverId
"""

###ARCHI RAPPRESENTANO GLI HEAD-TO-HEAD TRA PILOTI DELLO STESSO COSTRUTTORE IN GARA
"""
#select d.driverRef , d2.driverRef , count(*) as n
from  races r , results r2 , drivers d , results r3 , drivers d2 
where r.year = 2015  
and r.raceId = r2.raceId
and r3.raceId = r.raceId
and r2.constructorId = r3.constructorId 
and r2.driverId != r3.driverId 
and r2.driverId = d.driverId
and r3.driverId = d2.driverId
and r2.position < r3.position
group by d.driverRef , d2.driverRef 
"""

###ARCHI RAPPRESENTANO GLI HEAD-TO-HEAD TRA PILOTI DELLO STESSO COSTRUTTORE IN QUALIFICA
"""
#select d.driverRef , d2.driverRef , count(*) as n
from  races r , qualifying q , drivers d , qualifying q2  , drivers d2 
where r.year = 2012  
and r.raceId = q.raceId
and q2.raceId = r.raceId
and q.constructorId = q2.constructorId 
and q.driverId != q2.driverId 
and q.driverId = d.driverId
and q2.driverId = d2.driverId
and q.position < q2.position
group by d.driverRef , d2.driverRef
"""

#selezionare i punti fatti da ogni costruttore dopo ogni gara in una determinata stagione
"""
#select c.constructorId , c.points , c.raceId
from constructorstandings c , constructors c2 , constructorresults c3 , races r 
where  c2.constructorId = c.constructorId 
and  c3.constructorId = c.constructorId and c3.raceId = c.raceId 
and c.raceId =r.raceId and r.year =2012
group by c.constructorId , c.points , c.raceId
"""

#selezionare la classifica finale costruttori in un certo anno con punti, nomecostruttore e vittorie
"""
#select c.points, c2.constructorRef, c.wins
from (	select max(r.raceId) as ultima
		from races r 
		where r.year = 2015) as m, constructorstandings c , constructors c2 
where c.constructorId = c2.constructorId and m.ultima = c.raceId
order by c.points desc
"""

#selezionare classifica piloti in un certo anno
"""
#select d2.driverRef, d.points, d.wins, c.constructorRef 
from (	select max(r.raceId) as ultima
		from races r 
		where r.year = 2015) as m, driverstandings d  , drivers d2 , constructors c , results r 
where m.ultima = d.raceId and d.driverId = d2.driverId  and d.raceId = r.raceId and r.constructorId = c.constructorId and r.driverId = d.driverId
order by d.points DESC
"""

#selezionare i piloti che anno fatto pole in un certo anno e quante sono state convertite in vittorie
"""
#select  q.driverId,d.driverRef , count(*) as pole,  COALESCE(p.convertite, 0) AS convertite
from qualifying q , races r , drivers d , (select  q.driverId,d.driverRef , count(*) as convertite
											from qualifying q , races r , drivers d , results r2 
											where q.raceId = r.raceId and r.year = 2012 and q.position  = 1 and d.driverId = q.driverId and r.raceId = r2.raceId and q.driverId = r2.driverId
											and r2.position = 1
											group by q.driverId , d.driverRef) as p			
where q.raceId = r.raceId and r.year = 2012 and q.position  = 1 and d.driverId = q.driverId and q.driverId = p.driverId
group by q.driverId , d.driverRef, p.convertite
"""


#selezionare i piloti che in un certo anno sono arrivati primi in qualifica e in gara
"""
#select  q.driverId,d.driverRef , count(*) as n
from qualifying q , races r , drivers d , results r2 
where q.raceId = r.raceId and r.year = 2012 and q.position  = 1 and d.driverId = q.driverId and r.raceId = r2.raceId and q.driverId = r2.driverId
and r2.position = 1
group by q.driverId , d.driverRef
"""

#selezionare i piloti che in un certo anno hanno fatto pole e poi quante ne hanno convertite
"""
#select q.driverId, d.driverRef,COUNT(*) AS pole, COALESCE(p.convertite, 0) AS convertite
from qualifying AS q 
JOIN races AS r ON q.raceId = r.raceId
AND r.year   = 2012
JOIN drivers    AS d
ON q.driverId = d.driverId
LEFT JOIN (
    SELECT
      q.driverId,
      COUNT(*) AS convertite
    FROM
      qualifying AS q
      JOIN races   AS r
        ON q.raceId = r.raceId
        AND r.year   = 2012
      JOIN results AS re
        ON re.raceId  = q.raceId
       AND re.driverId = q.driverId
       AND re.position = 1    -- vittoria
    WHERE
      q.position = 1          -- pole position
    GROUP BY
      q.driverId
  ) AS p
    ON q.driverId = p.driverId
WHERE
  q.position = 1   -- pole position nella gara
GROUP BY
  q.driverId,
  d.driverRef
ORDER BY
  pole DESC
"""