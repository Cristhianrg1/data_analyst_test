/**Ejercicio 1**/
select
    full_name
from clients
where date(registration_date) < '2020-09-25'

#### Ejercicio 2 ####
select
    avg(score) as promedio_score
from orders
where status = 'ENTREGADO'



#### Ejercicio 3 ####
select
    c.full_name
    ,count(o.id) as pedidos
from   orders o
left join clients c on o.client_id = c.id
group by c.full_name
order by pedidos desc



#### Ejercicio 4 ####
select
    dd.full_name
    ,count(*) ordenes_entregadas
from   orders o
left join delivery_drivers dd on o.delivery_driver_id = dd.id
where status = 'ENTREGADO'
group by dd.full_name
order by ordenes_entregadas desc



#### Ejercicio 5 ####
select
    p.name
    ,max(p.price) as price
    ,sum(quantity) as quantity
from order_products op
left join products p on op.product_id = p.id
inner join orders o
on  op.order_id = o.id
and o.status = 'ENTREGADO'
group by p.name
order by sum(quantity) desc, max(price) asc
limit 1



#### Ejercicio 6 ####
select
    clients.full_name as client_name
from (
    select
        p.name
        ,p.id
        ,max(p.price) as price
        ,sum(quantity) as quantity
    from order_products op
    left join products p on op.product_id = p.id
    inner join orders o
    on  op.order_id = o.id
    and o.status = 'ENTREGADO'
    group by p.name
    order by sum(quantity) desc, max(price) desc
    limit 1
) pd
left join order_products
on pd.id = order_products.product_id
left join orders on order_products.order_id = orders.id
left join  clients on orders.client_id = clients.id
group by clients.full_name
