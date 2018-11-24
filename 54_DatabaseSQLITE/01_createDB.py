#!/usr/bin/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

def createDB():
   db = QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('sports.db')

   if not db.open():
      QMessageBox.critical(None, qApp.tr("Cannot open database"),
         qApp.tr("Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read "
            "the Qt SQL driver documentation for information "
            "how to build it.\n\n" "Click Cancel to exit."),
         QMessageBox.Cancel)

      return False

   query = QSqlQuery()

   query.exec_("create table sportsmen(id int primary key, "
      "firstname varchar(20), lastname varchar(20))")

   query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
   query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
   query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
   query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
   query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
   return True

if __name__ == '__main__':
   import sys

   app = QApplication(sys.argv)
   createDB()
