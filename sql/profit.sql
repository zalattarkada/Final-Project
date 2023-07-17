USE movies;

SELECT 
    title,
    revenue, 
    budget,
    (revenue - budget) AS profit,
    CASE
        WHEN budget > 0 THEN (revenue - budget) / budget
        ELSE NULL
    END AS profit_ratio,
    CASE
        WHEN revenue > 0 THEN ((revenue - budget) / revenue) * 100
        ELSE NULL
    END AS profit_margin
FROM 
    tmdb_movies;
