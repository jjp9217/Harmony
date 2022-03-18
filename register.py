# insert into p320_19."user" (username, acc_creation_date, password, first_name, last_name, email)
# values ('test', '2022-03-17', 'pass', 'catherine', 'katherine', 'null@gmail.com');
import sqlconnect

SQL = "insert into p320_19.\"user\" (username, acc_creation_date, password, first_name, last_name, email)" \
      "values (%s, %s, %s, %s, %s, %s);"


