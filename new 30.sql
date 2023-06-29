Sa se afiseze acele cursuri pentru care mai exista in acelasi an de predare macar inca un curs cu acelasi numar de credite.

select id_curs from cursuri c1 
where exists (
select 1 from cursuri c2 where c1.an=c2.an and c1.credite=c2.credite and c1.id_curs!=c2.id_curs)

select id_curs from cursuri c1 where exists (select 1 from cursuri c2 
 where c1.credite=c2.credite and c1.an=c2.an and  c1.id_curs!=c2.id_curs);
 
 
 
 Sa se determine care este grupa (sau care sunt grupele) in care se gasesc cei mai multi bursieri. O grupa este identificata de combinatia grupa-an.
 
 select grupa,an from studenti s1 group by grupa,an having count(bursa) in (select max(count(bursa)) from studenti group by grupa,an);
 
 
 
 Sa se afiseze pentru fiecare an de studiu care e disciplina cea mai usoara din acel an, adica disciplina la care media notelor e cea mai mare din an. Se considera anul in care se preda disciplina (campul an din tabelul cursuri si nu din tabelul studenti).
 
 select id_curs,an from note n1 natural join cursuri c1 group by an,id_curs having avg(valoare) in (select max(avg(valoare)) from note n2 natural join cursuri c2 group by an,id_curs having c1.an=c2.an);
 
Sa se afiseze numele si prenumele acelor studenti care obtin cea mai mare nota din anul lor pentru fiecare disciplina. Rezolvati utilizand subinterogari corelate.
 
  select nume,prenume from studenti s1 natural join note n1
    group by valoare,nume,prenume,nr_matricol
    having valoare in
    (select max(valoare) from note n2 group by id_curs);
	
Sa se afiseze titlul disciplinei cu cea mai mare medie a notelor puse.
select titlu_curs from note natural join cursuri
group by id_curs,titlu_curs
having avg(valoare) in
(select max(avg(valoare)) from note group by id_curs);

Sa se afiseze titlul disciplinei cu cea mai mare medie a notelor puse.
select titlu_curs from note natural join cursuri group by id_curs,titlu_curs having avg(valoare) in 
(select max(avg(valoare)) from note group by id_curs);
