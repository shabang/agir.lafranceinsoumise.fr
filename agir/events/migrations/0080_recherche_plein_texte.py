# Generated by Django 2.2.4 on 2019-09-02 10:43

from django.db import migrations

SEARCH_COLUMN = """
setweight(to_tsvector('french_unaccented', COALESCE("name", '')), 'A')
|| setweight(to_tsvector('french_unaccented', COALESCE("location_name", '')), 'B')
|| setweight(to_tsvector('french_unaccented', COALESCE("location_city", '')), 'B')
|| setweight(to_tsvector('french_unaccented', COALESCE("location_zip", '')), 'B')
|| setweight(to_tsvector('french_unaccented', COALESCE("description", '')), 'C')
|| setweight(to_tsvector('french_unaccented', COALESCE("report_content", '')), 'C')
"""

ADD_GROUP_TEXT_SEARCH_INDEX = f"""
-- noinspection SqlResolve
CREATE INDEX events_event_search ON events_event USING GIN (({SEARCH_COLUMN}));
"""

DROP_GROUP_TEXT_SEARCH_INDEX = """
-- noinspection SqlResolve
DROP INDEX events_event_search;
"""

##############################################################################
# Copié collé depuis 0075_recherche_evenement_plein_texte                    #
##############################################################################

add_event_search_trigger = """
CREATE TEXT SEARCH CONFIGURATION fr ( COPY = french );
ALTER TEXT SEARCH CONFIGURATION fr
  ALTER MAPPING FOR hword, hword_part, word
  WITH unaccent, french_stem;


CREATE FUNCTION get_event_tsvector(
    _id events_event.id%TYPE,
    name events_event.name%TYPE,
    description events_event.description %TYPE,
    report events_event.report_content%TYPE,
    location_name events_event.location_name%TYPE
    ) RETURNS tsvector AS $$
DECLARE
    group_name RECORD;
    search tsvector;
BEGIN

    search := '';
    FOR group_name IN
    SELECT grp.name
    FROM groups_supportgroup grp JOIN events_organizerconfig config ON grp.id = config.as_group_id
    WHERE config.event_id = _id LOOP
        search := search || setweight(to_tsvector('fr', coalesce(group_name.name, '')), 'B');
    END LOOP;
  RETURN
    search ||
    setweight(to_tsvector('fr', coalesce(name, '')), 'A') ||
    setweight(to_tsvector('fr', coalesce(description, '')), 'C') ||
    setweight(to_tsvector('fr', coalesce(report, '')), 'C') ||
    setweight(to_tsvector('fr', coalesce(location_name, '')), 'B')
    ;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION update_event_search_field_from_id(event_id events_event.id%TYPE) RETURNS VOID AS $$
BEGIN
    UPDATE events_event SET search = get_event_tsvector(id, name, description, report_content, location_name) WHERE id = event_id;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION process_update_event() RETURNS TRIGGER AS $$
DECLARE
    do_update bool default FALSE;
BEGIN

    IF TG_OP = 'INSERT' THEN
        NEW.search := get_event_tsvector(NEW.id, NEW.name, NEW.description, NEW.report_content, NEW.location_name);
        RETURN NEW;
    END IF;

    IF (NEW.name <> OLD.name) THEN do_update = TRUE;
    ELSIF (NEW.description <> OLD.description) THEN do_update = TRUE;
    ELSIF (NEW.report_content <> OLD.report_content) THEN do_update = TRUE;
    ELSIF (NEW.location_name <> OLD.location_name) THEN do_update = TRUE;
    END IF;

    IF do_update THEN
        NEW.search := get_event_tsvector(NEW.id, NEW.name, NEW.description, NEW.report_content, NEW.location_name);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION process_update_supportgroup() RETURNS TRIGGER AS $$
DECLARE
    og RECORD;
BEGIN
    -- 
    -- Se charge de mettre a jour le champ search des événement lorsaue le nom d'un groupe est modifier
    -- ou lorsque le groupe est supprimer
    -- 
    IF (tg_op = 'UPDATE') AND OLD.name <> NEW.name THEN
        FOR og IN SELECT event_id FROM events_organizerconfig WHERE as_group_id = NEW.id LOOP
            PERFORM update_event_search_field_from_id(og.event_id);
        END LOOP;
    ELSIF (tg_op = 'DELETE') THEN
        FOR og IN SELECT event_id FROM events_organizerconfig WHERE as_group_id = OLD.id LOOP
            PERFORM update_event_search_field_from_id(og.event_id);
        END LOOP;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;


CREATE FUNCTION process_update_organizerconfig() RETURNS TRIGGER AS $$
BEGIN
    IF (tg_op = 'INSERT') OR (tg_op = 'UPDATE') THEN
        PERFORM update_event_search_field_from_id(NEW.event_id);
    ELSIF (tg_op = 'DELETE') THEN
        PERFORM update_event_search_field_from_id(OLD.event_id);
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_event_search_field_when_modified
BEFORE UPDATE OR INSERT ON events_event
    FOR EACH ROW EXECUTE PROCEDURE process_update_event();

CREATE TRIGGER update_event_search_field_when_supportgroup_modified
AFTER UPDATE OR DELETE ON groups_supportgroup
    FOR EACH ROW EXECUTE PROCEDURE process_update_supportgroup();

CREATE TRIGGER update_event_search_field_when_organizerconfig_modified
AFTER INSERT OR UPDATE OR DELETE ON events_organizerconfig
    FOR EACH ROW EXECUTE PROCEDURE process_update_organizerconfig();

UPDATE events_event SET search = get_event_tsvector(id, name, description, report_content, location_name);
"""

remove_event_search_trigger = """
DROP TRIGGER update_event_search_field_when_modified ON events_event;
DROP FUNCTION process_update_event();
DROP FUNCTION get_event_tsvector(_id events_event.id%TYPE,
    name events_event.name%TYPE, description events_event.description %TYPE,
    report events_event.report_content%TYPE, location_name events_event.location_name%TYPE);
DROP FUNCTION update_event_search_field_from_id(event_id events_event.id%TYPE);

DROP TRIGGER update_event_search_field_when_supportgroup_modified ON groups_supportgroup;
DROP FUNCTION process_update_supportgroup();
DROP TRIGGER update_event_search_field_when_organizerconfig_modified ON events_organizerconfig;
DROP FUNCTION process_update_organizerconfig();
DROP TEXT SEARCH CONFIGURATION fr;
"""


##############################################################################
# Fin du copier/coller                                                       #
##############################################################################


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0079_event_facebook"),
        ("groups", "0036_recherche_plein_texte"),
    ]

    operations = [
        migrations.RunSQL(
            sql=ADD_GROUP_TEXT_SEARCH_INDEX, reverse_sql=DROP_GROUP_TEXT_SEARCH_INDEX
        ),
        migrations.RunSQL(
            sql=remove_event_search_trigger, reverse_sql=add_event_search_trigger
        ),
        migrations.RemoveIndex(model_name="event", name="search_event_index"),
        migrations.RemoveField(model_name="event", name="search"),
    ]
