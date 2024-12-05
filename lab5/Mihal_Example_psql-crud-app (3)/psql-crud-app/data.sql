

CREATE DATABASE "CKCS145"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_CA.UTF-8'
    LC_CTYPE = 'en_CA.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    
-- Table: public.Students

-- DROP TABLE IF EXISTS public."Students";

CREATE TABLE IF NOT EXISTS public."Students"
(
    "firstName" text COLLATE pg_catalog."default",
    "lastName" text COLLATE pg_catalog."default",
    "studentNo" integer NOT NULL,
    email text COLLATE pg_catalog."default",
    CONSTRAINT "Students_pkey" PRIMARY KEY ("studentNo")
)

    
    
INSERT INTO public."Students"("firstName", "lastName", "studentNo", "email")
	VALUES ('John', 'Doe', 202401001, 'john.doe@torontomu.ca');

INSERT INTO public."Students"("firstName", "lastName", "studentNo", email)
	VALUES ('Jonathan', 'Doe', 202401002, 'jonathan.doe@torontomu.ca');

SELECT * FROM public."Students"








