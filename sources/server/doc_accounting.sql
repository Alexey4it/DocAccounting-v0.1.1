/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     07.02.2022 15:26:39                          */
/*==============================================================*/


alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_CATEGORY;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_VIEW_DOC;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_EMPLOYEE;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_STATUS_D;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_DEVELOPE;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_SOURCES;

alter table Employees 
   drop foreign key FK_EMPLOYEE_RELATIONS_POSITION;

alter table Employees 
   drop foreign key FK_EMPLOYEE_RELATIONS_DEPARTME;

drop table if exists Category_Docs;

drop table if exists Departments;

drop table if exists Developers;


alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_CATEGORY;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_VIEW_DOC;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_EMPLOYEE;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_STATUS_D;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_DEVELOPE;

alter table Docs 
   drop foreign key FK_DOCS_RELATIONS_SOURCES;

drop table if exists Docs;


alter table Employees 
   drop foreign key FK_EMPLOYEE_RELATIONS_POSITION;

alter table Employees 
   drop foreign key FK_EMPLOYEE_RELATIONS_DEPARTME;

drop table if exists Employees;

drop table if exists Positions;

drop table if exists Regulations;

drop table if exists Sources;

drop table if exists Status_Docs;

drop table if exists View_Docs;

/*==============================================================*/
/* Table: Category_Docs                                         */
/*==============================================================*/
create table Category_Docs
(
   code                 int not null  comment '',
   title                text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: Departments                                           */
/*==============================================================*/
create table Departments
(
   code                 int not null  comment '',
   title                text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: Developers                                            */
/*==============================================================*/
create table Developers
(
   code                 int not null  comment '',
   title                text  comment '',
   comments             text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: Docs                                                  */
/*==============================================================*/
create table Docs
(
   code                 int not null  comment '',
   category_code        int  comment '',
   view_code            int  comment '',
   employee_code        int  comment '',
   status_code          int  comment '',
   developer_code       int  comment '',
   source_code          int  comment '',
   title                text  comment '',
   date_loading         datetime  comment '',
   date_change          datetime  comment '',
   barcode              text  comment '',
   keywords             text  comment '',
   section_number       int  comment '',
   pages                int  comment '',
   copy_n               int  comment '',
   cupboard             text  comment '',
   rack                 text  comment '',
   description          text  comment '',
   docs                 longblob  comment '',
   docs_ext             text  comment '',
   sizeMB               text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: Employees                                             */
/*==============================================================*/
create table Employees
(
   code                 int not null  comment '',
   positions_code       int  comment '',
   departments_code     int  comment '',
   allnames             text  comment '',
   email                text  comment '',
   login                text  comment '',
   password             text  comment '',
   editable             text  comment '',
   reading              text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: Positions                                             */
/*==============================================================*/
create table Positions
(
   code                 int not null  comment '',
   title                text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: Regulations                                           */
/*==============================================================*/
create table Regulations
(
   code                 int not null  comment '',
   category             text  comment '',
   title                text  comment '',
   docs                 longblob  comment '',
   docs_ext             text  comment '',
   url                  text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: Sources                                               */
/*==============================================================*/
create table Sources
(
   code                 int not null  comment '',
   title                text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: Status_Docs                                           */
/*==============================================================*/
create table Status_Docs
(
   code                 int not null  comment '',
   title                text  comment '',
   description          text  comment '',
   primary key (code)
);

/*==============================================================*/
/* Table: View_Docs                                             */
/*==============================================================*/
create table View_Docs
(
   code                 int not null  comment '',
   title                text  comment '',
   description          text  comment '',
   primary key (code)
);

alter table Docs add constraint FK_DOCS_RELATIONS_CATEGORY foreign key (category_code)
      references Category_Docs (code) on delete restrict on update restrict;

alter table Docs add constraint FK_DOCS_RELATIONS_VIEW_DOC foreign key (view_code)
      references View_Docs (code) on delete restrict on update restrict;

alter table Docs add constraint FK_DOCS_RELATIONS_EMPLOYEE foreign key (employee_code)
      references Employees (code) on delete restrict on update restrict;

alter table Docs add constraint FK_DOCS_RELATIONS_STATUS_D foreign key (status_code)
      references Status_Docs (code) on delete restrict on update restrict;

alter table Docs add constraint FK_DOCS_RELATIONS_DEVELOPE foreign key (developer_code)
      references Developers (code) on delete restrict on update restrict;

alter table Docs add constraint FK_DOCS_RELATIONS_SOURCES foreign key (source_code)
      references Sources (code) on delete restrict on update restrict;

alter table Employees add constraint FK_EMPLOYEE_RELATIONS_POSITION foreign key (positions_code)
      references Positions (code) on delete restrict on update restrict;

alter table Employees add constraint FK_EMPLOYEE_RELATIONS_DEPARTME foreign key (departments_code)
      references Departments (code) on delete restrict on update restrict;

