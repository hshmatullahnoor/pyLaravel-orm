from database.core import Database
from database.crud.Table import Table

# اتصال
Database.host = "localhost"
Database.port = 3306
Database.name = "python_test"
Database.user = "root"
Database.password = "secret"

# INSERT
Table("users").insert({"name": "Ali", "email": "ali@example.com"}).run()

# UPDATE
Table("users").update({"name": "Mehdi"}).where("id = 1").run()

# DELETE
Table("users").delete().where("id = 5").run()

# SELECT
rows = Table("users").select("*").where("id > 1").orderBy("id", "DESC").limit(5).run()
print(rows)

# JOIN + GROUP
rows = (
    Table("orders")
    .select("orders.id, users.name, SUM(orders.amount) as total")
    .join("users", "orders.user_id = users.id")
    .groupBy("users.id")
    .run()
)
print(rows)


# ساخت جدول

from database.schema.CreateTable import CreateTable

# ساخت جدول users
table = CreateTable("users") \
    .id() \
    .string("name", 100) \
    .string("email", 150) \
    .boolean("is_active") \
    .enum("role", "admin", "user") \
    .timestamps()

print(table.build())   # فقط SQL رو ببینی
print(table.run())     # واقعا جدول ساخته میشه

