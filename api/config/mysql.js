import mysql from 'mysql'
//import { db_host,db_username,db_password,db_name } from './variables';

const dbConfig = {
  host: 'REPLACE_WITH_YOUR_DB_SERVER',
  user: 'REPLACE_WITH_YOUR_DB_USER',
  password: 'REPLACE_WITH_YOUR_DB_PASSWORD',
  database: 'REPLACE_WITH_YOUR_DB'
};

const db = mysql.createConnection(dbConfig);

db.connect(err => {
  if (err) {
    console.error('Fehler beim Verbinden mit der Datenbank:', err);
    return;
  }
  console.log('Erfolgreich mit der Datenbank verbunden');
});

export default db;
