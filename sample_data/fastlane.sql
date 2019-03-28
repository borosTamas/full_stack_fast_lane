
ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS pk_user_id CASCADE;


DROP TABLE IF EXISTS public.user;
CREATE TABLE "users"(
  id serial NOT NULL,
  username text,
  scores integer
);

ALTER TABLE ONLY "users"
  ADD CONSTRAINT pk_user_id PRIMARY KEY (id);

INSERT INTO "users" VALUES (1, 'levente', 250);