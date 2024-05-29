BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "Client" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "lastname" TEXT NOT NULL,
    "nin" INTEGER NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "Product" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "mfg" DATE NOT NULL,
    "exp" DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS "ClientProduct" (
    "client_id" INTEGER,
    "product_id" INTEGER,
    PRIMARY KEY("client_id", "product_id"),
    FOREIGN KEY("client_id") REFERENCES "Client"("id"),
    FOREIGN KEY("product_id") REFERENCES "Product"("id")
);

INSERT INTO "Client" VALUES (1,'Yngwie','Malmsteen',11111111);
INSERT INTO "Client" VALUES (2,'Jason','Becker',22222222);
INSERT INTO "Client" VALUES (3,'Joe','Satriani',33333333);
INSERT INTO "Client" VALUES (4,'Steve','Vai',44444444);
INSERT INTO "Client" VALUES (5,'Paul','Gilber',55555555);
INSERT INTO "Client" VALUES (6,'Guthrie','Govan',66666666);
INSERT INTO "ClientProduct" VALUES (1,1);
INSERT INTO "ClientProduct" VALUES (1,3);
INSERT INTO "ClientProduct" VALUES (2,4);
INSERT INTO "ClientProduct" VALUES (1,4);
INSERT INTO "ClientProduct" VALUES (1,2);
INSERT INTO "Product" VALUES (1,'leche','2024-02-04','2024-03-04');
INSERT INTO "Product" VALUES (2,'yogurt','2024-05-27','2024-06-15');
INSERT INTO "Product" VALUES (3,'lata de atun','2022-03-01','2024-03-01');
INSERT INTO "Product" VALUES (4,'pan de molde','2024-05-15','2024-05-30');
INSERT INTO "Product" VALUES (5,'torta','2024-05-20','2024-06-20');

COMMIT;
