-- lists all bands with Glam rock as their main style, ranked by their longevity
    -- table dump: metal_bands.sql.zip
    -- column names must be: band_name and lifespan (in years)
    -- use attributes formed and split for computing the lifespan
SELECT band_name, IFNULL(split,2020) - IFNULL(formed,0) AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan DESC;
