query = '''
SELECT
    b.id,
    b.name,
    COALESCE(o.total_offer, 0) as total_offer,
    COALESCE(p.total_payment, 0) as total_payment,
    COALESCE(o.total_offer, 0) - COALESCE(p.total_payment, 0) as difference 
FROM
    buyer b
LEFT JOIN (
    SELECT buyer_id, SUM(value) as total_offer FROM offer
    GROUP BY buyer_id
) o ON o.buyer_id = b.id
LEFT JOIN (
    SELECT buyer_id, SUM(value) as total_payment FROM payment
    GROUP BY buyer_id
) p ON p.buyer_id = b.id
WHERE COALESCE(total_offer, 0) > 0;
'''