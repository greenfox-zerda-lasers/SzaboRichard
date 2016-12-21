var mysql = require("mysql");

var con = mysql.createConnection({
  host: "localhost",
  user: "'root'",
  password: "admin",
  database: "bookstore"
});

con.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

// all books with its name, authors name, category name, publishers name and price

con.query("SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast INNER JOIN author ON author.aut_id = book_mast.aut_id INNER JOIN category ON category.cate_id = book_mast.cate_id INNER JOIN newpublisher ON newpublisher.pub_id = book_mast.pub_id ;", function(err, rows){
  if (err) {
    console.log(err.toString());
    return
  }
  console.log("Data recieved from Db:\n");
  console.log(rows);
});

con.end();
