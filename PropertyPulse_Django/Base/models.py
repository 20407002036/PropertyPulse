from django.db import models

# Create your models here.
"""_summary_
    The database model for this project
    planning to have an app for the database
    
    Schema: have two tables;
            - Users
            - Property
        Users
            => Id varchar(60) not null primary key
            => Created_at - datetime
            => Updated_at - datetime
            => firstname - varchar(60)
            => lastname - varchar(60)
            => email - varchar(128) not null
            => password - varchar(128) not null
            => phone Number - varchar(128)
            => UserType < Tenant/Owner > - varchar(128)
            
        Property
            => Created_at - datetime
            => Updated_at - datetime
            => name -varchar(128)
            => User_Id < Owner> - varchar
            => Description
    """
