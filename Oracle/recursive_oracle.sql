-- Query that will join the table with itself, and display all the possible paths
-- starting from every row.

-- The table has following structure:
-- entryguid | name | parententryguid

-- The goal of this query is to get a all the rows, together with the longest 
-- path that can be formed following the parent -> entryguid link to itself.

-- The tricky parts here are the prior construct: it evaluates to the prior step in the
-- tree. As the parent of the row should be equal to the entry guid of the previous node 
-- in the tree, the connect_by condition is ch.parententryguid = prior ch.entryguid

-- Because the query will return all the paths, I have the need for the extra filter using CTE.

-- LABELS: oracle, sql, recursive, query, tree, path
-- DATE: 2016-02-10

with cte as (SELECT ch.entryguid, ch.name, SYS_CONNECT_BY_PATH(ch.name, '/') "Path", LEVEL as lvl, connect_by_isleaf is_leaf
FROM mdm_materialentity ch
where lifecyclestatus='active'
connect by  ch.parententryguid = prior ch.entryguid
order by SYS_CONNECT_BY_PATH(ch.name, '/') 
), got_level as 
(select max(lvl) max_level, entryguid
from cte
group by entryguid)
select cte.entryguid, name, "Path", is_leaf
from cte 
join got_level on cte.entryguid = got_level.entryguid
where cte.lvl = got_level.max_level
;
