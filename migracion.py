import conexion as cx
import provincia as pv
import mysql.connector
dest = cx.lojurid.cursor()

# orig = mysql.connector.connect()

provincias = {
    1:pv.provincia(21,"Pinar del Rio",21,"lojurid_01pinar"),
    2:pv.provincia(23,"Habana",23,"lojurid_02habana"),
    3:pv.provincia(22,"Artemisa",22,"lojurid_03artemisa"),
    4:pv.provincia(25,"Matanzas",25,"lojurid_05matanzas"),
    5:pv.provincia(26,"Villa Clara",26,"lojurid_06villaclara"),
    6:pv.provincia(27,"Cienfuegos",27,"lojurid_08cienfuegos"),
    7:pv.provincia(28,"Sancti Spíritus",28,"lojurid_07santispiritus"),
    8:pv.provincia(8,"Ciego de Avila",29,"lojurid_09ciego"),
    9:pv.provincia(9,"Camagüey",30,"lojurid_10camaguey"),
    10:pv.provincia(10,"Las Tunas",31,"lojurid_11lastunas"),
    11:pv.provincia(11,"Granma",33,"lojurid_13granma"),
    12:pv.provincia(12,"Holguín",32,"lojurid_12holguin"),
    13:pv.provincia(13,"Santiago de Cuba",34,"lojurid_14santiago"),
    14:pv.provincia(14,"Guantánamo",35,"lojurid_15gtm"),
    15:pv.provincia(15,"Isla de la Juventud",40,"lojurid_16gerona"),
    # 17:pv.provincia(17,"Mayabeque",)
    }
#Pedimos al usuario una cantidad
# sol_cantidad = int(input("Introduzca una cantidad: "))
 
#Consulta SQL que ejecutaremos, en este caso un select
#Con el parámetro sol_cantidad para filtrar aquellos
#registros cuya cantidad sea superior a la introducida
# sqlSelect = f"""SELECT * from medios_trans           
                # limit {sol_cantidad}"""           
#A partir del cursor, ejecutamos la consulta SQL
# dest.execute(sqlSelect)
#Guardamos el resultado de la consulta en una variable
# resultadoSQL = dest.fetchall()
 
#Cerramos el cursor y la conexión con MySQL
# dest.close()
# cx.lojurid.close()
 
#Mostramos el resultado por pantalla
# print (resultadoSQL)

baseorig = pv.bdprov("localhost","root","","lojurid_db")


for prov in provincias:
    baseorig.db = provincias[prov].bdname
    tmp= mysql.connector.connect(
        host = baseorig.host,
        user = baseorig.user,
        password = baseorig.password,
        db=baseorig.db,
        )
    
    sqlModificarRegistro = 'DELETE FROM `lotjurídicas` WHERE `NuLicencia` is NULL or `IdEntidad` is NULL or (`NuLicencia` not like("J%") and `NuLicencia` not like("j%") ) or (`IDEstado` in (2,4,8,10));'
    sqlUpdate = 'UPDATE `lotjurídicas` SET `NuLicencia`=REPLACE(`NuLicencia`,"j","J")'
    sqlLimpiaPJ = 'DELETE FROM `personasjurídicas` WHERE `NomEntidad` is NULL or (`IdEntidad` not in (SELECT `IdEntidad` from `lotjurídicas`))'
    sqlEstadLot = f"""SELECT sum(if(`NuLicencia` like("%-{provincias[prov].codigo}"),1,0)) as `locales`, sum(if(`NuLicencia` like("%-{provincias[prov].codigo}"),0,1)) as `foraneas`, count(*) as `total` FROM `lotjurídicas`"""
    sqllimpiaLot = f"""delete FROM `lotjurídicas` where `NuLicencia` not like("%-{provincias[prov].codigo}") """
    #Establecemos un cursor para la conexión con el servidor MySQL
    cursor = tmp.cursor()
    #A partir del cursor, ejecutamos la consulta SQL de modificación
    # cursor.execute(sqlModificarRegistro)
    cursor.execute(sqlLimpiaPJ)
    # cursor.execute(sqllimpiaLot)
    
    tmp.commit()
    # cursor.execute(sqlEstadLot)
    # sqlSelect = f"""SELECT count(*)  FROM `lotjurídicas` where `NuLicencia` like("%-{provincias[prov].codigo}") and `IDEstado` = 5 """           
    # sqlSelect = f"""SELECT count(*)  FROM `personasjurídicas` """           
    #A partir del cursor, ejecutamos la consulta SQL
    # cursor.execute(sqlSelect)
    #Guardamos el resultado de la consulta en una variable
    # resultadoSQL = cursor.fetchall()
    # print("Provincia","locales","Foraneas","Totales")
    # print(provincias[prov].nombre,resultadoSQL[0][0],resultadoSQL[0][1],resultadoSQL[0][2])
    tmp.close()

# print(provincias)