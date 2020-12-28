""" 28/12/2020 Database Operations
"""

"""
Veritabanı nedir ?
Bir sosyal medyaya yada uygulamaya üye oluyorsunuz diyelim.
Girişte sizden alınan ad,soyad,telefon gibi bilgilerin tutulduğu sisteme vertabanı sistemleri denir.
Örneğin kullanıcı bilgileri Users tablosunda kullanıcıya ait fotoğraflar Photos tablosunda tutulsun.
Her kullanıcının bir fotoğrafı olabileceği için Users ve Photos tabloları birbiriyle ilişkilidir.
Bu yapıdaki veritabanı sistemlerine ilişkisel veritabanı sistemleri denir.
İlişkisel veri tabanı sistemleri yaygın olarak kulllanılır.
Özetle veritabanı verilerin saklandığı yapılardır,ilişkisel veritabanı sistemleri de mevcuttur.
"""

"""

Mssql server ,Microsoft tarafından geliştirlen ilişkisel verştabanı sistemidir.

Oracle ,ilişkisel verştabanı sistemidir.
Mysql,Oracle tarafından satın alınmıştır.İlişkisel veritabanı sistemidir.
SQLite

SQLite dosya üzerinden çalışabilme imkanı sunduğu ve mobil projelerde de
kolaylıkla kullanılabilmesi açısından tercih ediliyor.

MongoDB ilişkisel vertabanı değildir.Nosql
Büyük verilerde tercih edilen veritabanıdır.
Json formatında data tutulur.
Veritabanına yeni veriler eklenmek isteniyor .
Daha performanslı çalışabilmek için mongodb kullanılır.

PostgreSql ,İlişkisel Veritabanına örnektir.





"""

"""
Biz projemizde SQLite database kullanacağız.
SQLite kolay olması,dosya üzerinden çalışabilme olanağı sağlaması ,mobilde ve diğer platformalardada
rahatlıkla kullanılabilmesi sebebiyle tercih edilir.
https://sqlitebrowser.org/ üzerinden sisteminize uygun version u kurabilirsiniz.

https://www.sqlitetutorial.net/ adrsinden sample database altından chinook database ini indirip sqllite da open database diyerek açalım.
"""
