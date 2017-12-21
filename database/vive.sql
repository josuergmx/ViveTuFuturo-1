--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.6
-- Dumped by pg_dump version 9.6.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: agenda_catestatuscita; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE agenda_catestatuscita (
    "idEstatus" bigint NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion character varying(100)
);


ALTER TABLE agenda_catestatuscita OWNER TO vive;

--
-- Name: agenda_cattipocita; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE agenda_cattipocita (
    "idTipoCita" bigint NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion character varying(100)
);


ALTER TABLE agenda_cattipocita OWNER TO vive;

--
-- Name: agenda_cita; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE agenda_cita (
    "idCita" integer NOT NULL,
    fecha timestamp with time zone NOT NULL,
    "direccionCita" character varying(200),
    descripcion character varying(500),
    "idAsesorCliente_id" integer NOT NULL,
    "idEstatus_id" bigint NOT NULL,
    "idTipoCita_id" bigint NOT NULL
);


ALTER TABLE agenda_cita OWNER TO vive;

--
-- Name: agenda_cita_idCita_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "agenda_cita_idCita_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "agenda_cita_idCita_seq" OWNER TO vive;

--
-- Name: agenda_cita_idCita_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "agenda_cita_idCita_seq" OWNED BY agenda_cita."idCita";


--
-- Name: asesor_reporteactividad; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE asesor_reporteactividad (
    "idReporte" integer NOT NULL,
    "fechaReporte" date NOT NULL,
    "recomendadosObtenidos" integer NOT NULL,
    "recomendadosContactados" integer NOT NULL,
    "llamadasRealizadas" integer NOT NULL,
    "citasObtenidas" integer NOT NULL,
    "citasTotales" integer NOT NULL,
    "citasNuevas" integer NOT NULL,
    "entrevistasInicialesPlaneadas" integer NOT NULL,
    "entrevistasInicialesRealizadas" integer NOT NULL,
    "entrevistasCierrePlaneadas" integer NOT NULL,
    "entrevistasCierreRealizadas" integer NOT NULL,
    "solicitudesSucritas" integer NOT NULL,
    "idAsesor_id" integer NOT NULL
);


ALTER TABLE asesor_reporteactividad OWNER TO vive;

--
-- Name: asesor_reporteactividad_idReporte_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "asesor_reporteactividad_idReporte_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "asesor_reporteactividad_idReporte_seq" OWNER TO vive;

--
-- Name: asesor_reporteactividad_idReporte_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "asesor_reporteactividad_idReporte_seq" OWNED BY asesor_reporteactividad."idReporte";


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO vive;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO vive;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO vive;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO vive;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO vive;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO vive;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO vive;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO vive;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO vive;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO vive;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO vive;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO vive;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: cliente_asesorcliente; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE cliente_asesorcliente (
    "idAsesorCliente" integer NOT NULL,
    "clienteProspecto" boolean NOT NULL,
    "fechaActualizacion" date NOT NULL,
    ocupacion character varying(150),
    dependientes character varying(150),
    ingresos double precision,
    link character varying(300),
    password character varying(10),
    nombre character varying(20),
    activo boolean,
    "Estatus_id" integer,
    "Origen_id" integer,
    "idAsesor_id" integer NOT NULL,
    "idCliente_id" integer NOT NULL,
    fecha timestamp with time zone
);


ALTER TABLE cliente_asesorcliente OWNER TO vive;

--
-- Name: cliente_asesorcliente_idAsesorCliente_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "cliente_asesorcliente_idAsesorCliente_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "cliente_asesorcliente_idAsesorCliente_seq" OWNER TO vive;

--
-- Name: cliente_asesorcliente_idAsesorCliente_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "cliente_asesorcliente_idAsesorCliente_seq" OWNED BY cliente_asesorcliente."idAsesorCliente";


--
-- Name: cliente_estatus; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE cliente_estatus (
    "idEstatus" integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion character varying(200)
);


ALTER TABLE cliente_estatus OWNER TO vive;

--
-- Name: cliente_estatus_idEstatus_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "cliente_estatus_idEstatus_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "cliente_estatus_idEstatus_seq" OWNER TO vive;

--
-- Name: cliente_estatus_idEstatus_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "cliente_estatus_idEstatus_seq" OWNED BY cliente_estatus."idEstatus";


--
-- Name: cliente_origenrecomendacion; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE cliente_origenrecomendacion (
    "idOrigen" integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion character varying(200)
);


ALTER TABLE cliente_origenrecomendacion OWNER TO vive;

--
-- Name: cliente_origenrecomendacion_idOrigen_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "cliente_origenrecomendacion_idOrigen_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "cliente_origenrecomendacion_idOrigen_seq" OWNER TO vive;

--
-- Name: cliente_origenrecomendacion_idOrigen_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "cliente_origenrecomendacion_idOrigen_seq" OWNED BY cliente_origenrecomendacion."idOrigen";


--
-- Name: cliente_recomendadocliente; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE cliente_recomendadocliente (
    id integer NOT NULL,
    nombre character varying(80) NOT NULL,
    celular integer,
    hijos boolean NOT NULL,
    activo boolean,
    asesor_id integer,
    "estadoCivil_id" integer
);


ALTER TABLE cliente_recomendadocliente OWNER TO vive;

--
-- Name: cliente_recomendadocliente_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE cliente_recomendadocliente_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE cliente_recomendadocliente_id_seq OWNER TO vive;

--
-- Name: cliente_recomendadocliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE cliente_recomendadocliente_id_seq OWNED BY cliente_recomendadocliente.id;


--
-- Name: creditos_creditos; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE creditos_creditos (
    "idCredito" integer NOT NULL,
    "estatusCredito_id" integer,
    "idAsesor_id" integer NOT NULL,
    "idCliente_id" integer
);


ALTER TABLE creditos_creditos OWNER TO vive;

--
-- Name: creditos_creditos_idCredito_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "creditos_creditos_idCredito_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "creditos_creditos_idCredito_seq" OWNER TO vive;

--
-- Name: creditos_creditos_idCredito_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "creditos_creditos_idCredito_seq" OWNED BY creditos_creditos."idCredito";


--
-- Name: creditos_estatuscredito; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE creditos_estatuscredito (
    idestatuscredito integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion character varying(200)
);


ALTER TABLE creditos_estatuscredito OWNER TO vive;

--
-- Name: creditos_estatuscredito_idestatuscredito_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE creditos_estatuscredito_idestatuscredito_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE creditos_estatuscredito_idestatuscredito_seq OWNER TO vive;

--
-- Name: creditos_estatuscredito_idestatuscredito_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE creditos_estatuscredito_idestatuscredito_seq OWNED BY creditos_estatuscredito.idestatuscredito;


--
-- Name: creditos_sale; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE creditos_sale (
    id integer NOT NULL
);


ALTER TABLE creditos_sale OWNER TO vive;

--
-- Name: creditos_sale_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE creditos_sale_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE creditos_sale_id_seq OWNER TO vive;

--
-- Name: creditos_sale_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE creditos_sale_id_seq OWNED BY creditos_sale.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO vive;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO vive;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO vive;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO vive;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO vive;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO vive;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO vive;

--
-- Name: login_cattipodireccion; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE login_cattipodireccion (
    "idtipoDireccion" integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion character varying(100),
    CONSTRAINT "login_cattipodireccion_idtipoDireccion_check" CHECK (("idtipoDireccion" >= 0))
);


ALTER TABLE login_cattipodireccion OWNER TO vive;

--
-- Name: login_contacto; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE login_contacto (
    id integer NOT NULL,
    celular character varying(15) NOT NULL,
    telcasa character varying(15),
    oficina character varying(15),
    facebookid character varying(50),
    idpersona_id integer NOT NULL
);


ALTER TABLE login_contacto OWNER TO vive;

--
-- Name: login_contacto_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE login_contacto_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE login_contacto_id_seq OWNER TO vive;

--
-- Name: login_contacto_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE login_contacto_id_seq OWNED BY login_contacto.id;


--
-- Name: login_direccion; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE login_direccion (
    iddireccion integer NOT NULL,
    calle character varying(150),
    colonia character varying(100),
    delegacion character varying(100),
    cp character varying(5),
    numinterior character varying(7),
    numexterior character varying(7),
    idpersona_id integer NOT NULL,
    idtipodireccion_id integer
);


ALTER TABLE login_direccion OWNER TO vive;

--
-- Name: login_direccion_iddireccion_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE login_direccion_iddireccion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE login_direccion_iddireccion_seq OWNER TO vive;

--
-- Name: login_direccion_iddireccion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE login_direccion_iddireccion_seq OWNED BY login_direccion.iddireccion;


--
-- Name: login_estadocivil; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE login_estadocivil (
    "idEstadoCivil" integer NOT NULL,
    nombre character varying(20) NOT NULL,
    CONSTRAINT "login_estadocivil_idEstadoCivil_check" CHECK (("idEstadoCivil" >= 0))
);


ALTER TABLE login_estadocivil OWNER TO vive;

--
-- Name: login_persona; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE login_persona (
    id integer NOT NULL,
    curp character varying(18),
    rfc character varying(13),
    "fechaDeNacimiento" character varying(10),
    "estadoCivil_id" integer,
    "idRol_id" integer,
    user_id integer NOT NULL
);


ALTER TABLE login_persona OWNER TO vive;

--
-- Name: login_persona_id_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE login_persona_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE login_persona_id_seq OWNER TO vive;

--
-- Name: login_persona_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE login_persona_id_seq OWNED BY login_persona.id;


--
-- Name: login_roles; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE login_roles (
    "idRole" integer NOT NULL,
    nombre character varying(50),
    descripcion character varying(200)
);


ALTER TABLE login_roles OWNER TO vive;

--
-- Name: login_roles_idRole_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "login_roles_idRole_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "login_roles_idRole_seq" OWNER TO vive;

--
-- Name: login_roles_idRole_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "login_roles_idRole_seq" OWNED BY login_roles."idRole";


--
-- Name: productos_catestados; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE productos_catestados (
    "idEstado" integer NOT NULL,
    nombre character varying(100) NOT NULL,
    "idPais_id" integer NOT NULL
);


ALTER TABLE productos_catestados OWNER TO vive;

--
-- Name: productos_catestados_idEstado_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "productos_catestados_idEstado_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "productos_catestados_idEstado_seq" OWNER TO vive;

--
-- Name: productos_catestados_idEstado_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "productos_catestados_idEstado_seq" OWNED BY productos_catestados."idEstado";


--
-- Name: productos_catpais; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE productos_catpais (
    "idPais" integer NOT NULL,
    nombre character varying(100) NOT NULL
);


ALTER TABLE productos_catpais OWNER TO vive;

--
-- Name: productos_catpais_idPais_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "productos_catpais_idPais_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "productos_catpais_idPais_seq" OWNER TO vive;

--
-- Name: productos_catpais_idPais_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "productos_catpais_idPais_seq" OWNED BY productos_catpais."idPais";


--
-- Name: productos_departamento; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE productos_departamento (
    "idDepartamento" integer NOT NULL,
    nombre character varying(100),
    ubicacion character varying(50),
    telefono character varying(15),
    extension character varying(5),
    "idInstitucion_id" integer NOT NULL
);


ALTER TABLE productos_departamento OWNER TO vive;

--
-- Name: productos_departamento_idDepartamento_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "productos_departamento_idDepartamento_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "productos_departamento_idDepartamento_seq" OWNER TO vive;

--
-- Name: productos_departamento_idDepartamento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "productos_departamento_idDepartamento_seq" OWNED BY productos_departamento."idDepartamento";


--
-- Name: productos_institucionfinanciera; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE productos_institucionfinanciera (
    "idInstitucion" integer NOT NULL,
    nombre character varying(200),
    calle character varying(100),
    colonia character varying(100),
    cp character varying(5),
    num_int character varying(7),
    num_ext character varying(7),
    "idLocalidad_id" integer NOT NULL,
    "idPersona_id" integer
);


ALTER TABLE productos_institucionfinanciera OWNER TO vive;

--
-- Name: productos_institucionfinanciera_idInstitucion_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "productos_institucionfinanciera_idInstitucion_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "productos_institucionfinanciera_idInstitucion_seq" OWNER TO vive;

--
-- Name: productos_institucionfinanciera_idInstitucion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "productos_institucionfinanciera_idInstitucion_seq" OWNED BY productos_institucionfinanciera."idInstitucion";


--
-- Name: productos_localidad; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE productos_localidad (
    "idLocalidad" integer NOT NULL,
    nombre character varying(200) NOT NULL,
    "CatEstados_id" integer NOT NULL,
    "CatPais_id" integer NOT NULL
);


ALTER TABLE productos_localidad OWNER TO vive;

--
-- Name: productos_localidad_idLocalidad_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "productos_localidad_idLocalidad_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "productos_localidad_idLocalidad_seq" OWNER TO vive;

--
-- Name: productos_localidad_idLocalidad_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "productos_localidad_idLocalidad_seq" OWNED BY productos_localidad."idLocalidad";


--
-- Name: productos_servicio; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE productos_servicio (
    "idServicio" integer NOT NULL,
    descripcion character varying(300) NOT NULL,
    nombre character varying(300) NOT NULL,
    "idDepartamento_id" integer NOT NULL
);


ALTER TABLE productos_servicio OWNER TO vive;

--
-- Name: productos_servicio_idServicio_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "productos_servicio_idServicio_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "productos_servicio_idServicio_seq" OWNER TO vive;

--
-- Name: productos_servicio_idServicio_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "productos_servicio_idServicio_seq" OWNED BY productos_servicio."idServicio";


--
-- Name: promotor_promotorasesor; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE promotor_promotorasesor (
    "idAsesorPromotor" integer NOT NULL,
    activo boolean,
    "idAsesor_id" integer NOT NULL,
    "idPromotor_id" integer NOT NULL,
    institucion_id integer NOT NULL
);


ALTER TABLE promotor_promotorasesor OWNER TO vive;

--
-- Name: promotor_promotorasesor_idAsesorPromotor_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "promotor_promotorasesor_idAsesorPromotor_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "promotor_promotorasesor_idAsesorPromotor_seq" OWNER TO vive;

--
-- Name: promotor_promotorasesor_idAsesorPromotor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "promotor_promotorasesor_idAsesorPromotor_seq" OWNED BY promotor_promotorasesor."idAsesorPromotor";


--
-- Name: sesion1_blindajefinanciero; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE sesion1_blindajefinanciero (
    idbl integer NOT NULL,
    "column" integer
);


ALTER TABLE sesion1_blindajefinanciero OWNER TO vive;

--
-- Name: sesion1_blindajefinanciero_idbl_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE sesion1_blindajefinanciero_idbl_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE sesion1_blindajefinanciero_idbl_seq OWNER TO vive;

--
-- Name: sesion1_blindajefinanciero_idbl_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE sesion1_blindajefinanciero_idbl_seq OWNED BY sesion1_blindajefinanciero.idbl;


--
-- Name: sesion1_capitalizacion; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE sesion1_capitalizacion (
    idcapitalizacion integer NOT NULL,
    "column" integer
);


ALTER TABLE sesion1_capitalizacion OWNER TO vive;

--
-- Name: sesion1_capitalizacion_idcapitalizacion_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE sesion1_capitalizacion_idcapitalizacion_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE sesion1_capitalizacion_idcapitalizacion_seq OWNER TO vive;

--
-- Name: sesion1_capitalizacion_idcapitalizacion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE sesion1_capitalizacion_idcapitalizacion_seq OWNED BY sesion1_capitalizacion.idcapitalizacion;


--
-- Name: sesion1_libertadfinanciera; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE sesion1_libertadfinanciera (
    idlf integer NOT NULL,
    edad integer,
    "montoObjetivo" integer,
    anos integer,
    ahorro double precision
);


ALTER TABLE sesion1_libertadfinanciera OWNER TO vive;

--
-- Name: sesion1_libertadfinanciera_idlf_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE sesion1_libertadfinanciera_idlf_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE sesion1_libertadfinanciera_idlf_seq OWNER TO vive;

--
-- Name: sesion1_libertadfinanciera_idlf_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE sesion1_libertadfinanciera_idlf_seq OWNED BY sesion1_libertadfinanciera.idlf;


--
-- Name: sesion1_sesion1; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE sesion1_sesion1 (
    "idSesion" integer NOT NULL,
    "videoPresentacion" character varying(100),
    "cartaConfidencialidad" character varying(100),
    "blindajeFinancieroidbl_id" integer NOT NULL,
    "idAsesorCliente_id" integer NOT NULL,
    "idCapitalizacion_id" integer NOT NULL,
    "libertadFinancieraiDlf_id" integer NOT NULL
);


ALTER TABLE sesion1_sesion1 OWNER TO vive;

--
-- Name: sesion1_sesion1_idSesion_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "sesion1_sesion1_idSesion_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "sesion1_sesion1_idSesion_seq" OWNER TO vive;

--
-- Name: sesion1_sesion1_idSesion_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "sesion1_sesion1_idSesion_seq" OWNED BY sesion1_sesion1."idSesion";


--
-- Name: ventas_planesconcretados; Type: TABLE; Schema: public; Owner: vive
--

CREATE TABLE ventas_planesconcretados (
    "idPlan" integer NOT NULL,
    "fechaContratacion" time without time zone NOT NULL,
    "numeroPoliza" character varying(10) NOT NULL,
    "primaNetaAnual" double precision NOT NULL,
    "plazoAnos" integer NOT NULL,
    "valorPlan" double precision NOT NULL,
    observaciones character varying(300),
    "idAsesor_id" integer NOT NULL,
    "idCliente_id" integer NOT NULL,
    "idServicio_id" integer NOT NULL
);


ALTER TABLE ventas_planesconcretados OWNER TO vive;

--
-- Name: ventas_planesconcretados_idPlan_seq; Type: SEQUENCE; Schema: public; Owner: vive
--

CREATE SEQUENCE "ventas_planesconcretados_idPlan_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "ventas_planesconcretados_idPlan_seq" OWNER TO vive;

--
-- Name: ventas_planesconcretados_idPlan_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vive
--

ALTER SEQUENCE "ventas_planesconcretados_idPlan_seq" OWNED BY ventas_planesconcretados."idPlan";


--
-- Name: agenda_cita idCita; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY agenda_cita ALTER COLUMN "idCita" SET DEFAULT nextval('"agenda_cita_idCita_seq"'::regclass);


--
-- Name: asesor_reporteactividad idReporte; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY asesor_reporteactividad ALTER COLUMN "idReporte" SET DEFAULT nextval('"asesor_reporteactividad_idReporte_seq"'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: cliente_asesorcliente idAsesorCliente; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_asesorcliente ALTER COLUMN "idAsesorCliente" SET DEFAULT nextval('"cliente_asesorcliente_idAsesorCliente_seq"'::regclass);


--
-- Name: cliente_estatus idEstatus; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_estatus ALTER COLUMN "idEstatus" SET DEFAULT nextval('"cliente_estatus_idEstatus_seq"'::regclass);


--
-- Name: cliente_origenrecomendacion idOrigen; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_origenrecomendacion ALTER COLUMN "idOrigen" SET DEFAULT nextval('"cliente_origenrecomendacion_idOrigen_seq"'::regclass);


--
-- Name: cliente_recomendadocliente id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_recomendadocliente ALTER COLUMN id SET DEFAULT nextval('cliente_recomendadocliente_id_seq'::regclass);


--
-- Name: creditos_creditos idCredito; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_creditos ALTER COLUMN "idCredito" SET DEFAULT nextval('"creditos_creditos_idCredito_seq"'::regclass);


--
-- Name: creditos_estatuscredito idestatuscredito; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_estatuscredito ALTER COLUMN idestatuscredito SET DEFAULT nextval('creditos_estatuscredito_idestatuscredito_seq'::regclass);


--
-- Name: creditos_sale id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_sale ALTER COLUMN id SET DEFAULT nextval('creditos_sale_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: login_contacto id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_contacto ALTER COLUMN id SET DEFAULT nextval('login_contacto_id_seq'::regclass);


--
-- Name: login_direccion iddireccion; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_direccion ALTER COLUMN iddireccion SET DEFAULT nextval('login_direccion_iddireccion_seq'::regclass);


--
-- Name: login_persona id; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_persona ALTER COLUMN id SET DEFAULT nextval('login_persona_id_seq'::regclass);


--
-- Name: login_roles idRole; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_roles ALTER COLUMN "idRole" SET DEFAULT nextval('"login_roles_idRole_seq"'::regclass);


--
-- Name: productos_catestados idEstado; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_catestados ALTER COLUMN "idEstado" SET DEFAULT nextval('"productos_catestados_idEstado_seq"'::regclass);


--
-- Name: productos_catpais idPais; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_catpais ALTER COLUMN "idPais" SET DEFAULT nextval('"productos_catpais_idPais_seq"'::regclass);


--
-- Name: productos_departamento idDepartamento; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_departamento ALTER COLUMN "idDepartamento" SET DEFAULT nextval('"productos_departamento_idDepartamento_seq"'::regclass);


--
-- Name: productos_institucionfinanciera idInstitucion; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_institucionfinanciera ALTER COLUMN "idInstitucion" SET DEFAULT nextval('"productos_institucionfinanciera_idInstitucion_seq"'::regclass);


--
-- Name: productos_localidad idLocalidad; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_localidad ALTER COLUMN "idLocalidad" SET DEFAULT nextval('"productos_localidad_idLocalidad_seq"'::regclass);


--
-- Name: productos_servicio idServicio; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_servicio ALTER COLUMN "idServicio" SET DEFAULT nextval('"productos_servicio_idServicio_seq"'::regclass);


--
-- Name: promotor_promotorasesor idAsesorPromotor; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY promotor_promotorasesor ALTER COLUMN "idAsesorPromotor" SET DEFAULT nextval('"promotor_promotorasesor_idAsesorPromotor_seq"'::regclass);


--
-- Name: sesion1_blindajefinanciero idbl; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_blindajefinanciero ALTER COLUMN idbl SET DEFAULT nextval('sesion1_blindajefinanciero_idbl_seq'::regclass);


--
-- Name: sesion1_capitalizacion idcapitalizacion; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_capitalizacion ALTER COLUMN idcapitalizacion SET DEFAULT nextval('sesion1_capitalizacion_idcapitalizacion_seq'::regclass);


--
-- Name: sesion1_libertadfinanciera idlf; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_libertadfinanciera ALTER COLUMN idlf SET DEFAULT nextval('sesion1_libertadfinanciera_idlf_seq'::regclass);


--
-- Name: sesion1_sesion1 idSesion; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_sesion1 ALTER COLUMN "idSesion" SET DEFAULT nextval('"sesion1_sesion1_idSesion_seq"'::regclass);


--
-- Name: ventas_planesconcretados idPlan; Type: DEFAULT; Schema: public; Owner: vive
--

ALTER TABLE ONLY ventas_planesconcretados ALTER COLUMN "idPlan" SET DEFAULT nextval('"ventas_planesconcretados_idPlan_seq"'::regclass);


--
-- Data for Name: agenda_catestatuscita; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY agenda_catestatuscita ("idEstatus", nombre, descripcion) FROM stdin;
1	Sin asignar	\N
2	En espera	\N
\.


--
-- Data for Name: agenda_cattipocita; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY agenda_cattipocita ("idTipoCita", nombre, descripcion) FROM stdin;
1	Sin asignar	\N
2	Sesion 1	\N
\.


--
-- Data for Name: agenda_cita; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY agenda_cita ("idCita", fecha, "direccionCita", descripcion, "idAsesorCliente_id", "idEstatus_id", "idTipoCita_id") FROM stdin;
3	2017-11-28 22:06:00-06	ESCOM	ES CHIDA	5	2	1
4	2017-11-24 10:40:00-06	Vasconcelos	Es una cita profesional	6	2	2
5	2017-11-26 12:30:00-06	ESCOM	Es no se.	7	2	2
6	2017-11-27 10:45:00-06	Escom	ES CHIDA	7	2	2
7	2017-11-30 23:08:00-06	Vasconcelos	ES CHIDA	6	1	2
\.


--
-- Name: agenda_cita_idCita_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"agenda_cita_idCita_seq"', 7, true);


--
-- Data for Name: asesor_reporteactividad; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY asesor_reporteactividad ("idReporte", "fechaReporte", "recomendadosObtenidos", "recomendadosContactados", "llamadasRealizadas", "citasObtenidas", "citasTotales", "citasNuevas", "entrevistasInicialesPlaneadas", "entrevistasInicialesRealizadas", "entrevistasCierrePlaneadas", "entrevistasCierreRealizadas", "solicitudesSucritas", "idAsesor_id") FROM stdin;
\.


--
-- Name: asesor_reporteactividad_idReporte_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"asesor_reporteactividad_idReporte_seq"', 1, false);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add cat tipocita	7	add_cattipocita
20	Can change cat tipocita	7	change_cattipocita
21	Can delete cat tipocita	7	delete_cattipocita
22	Can add cita	8	add_cita
23	Can change cita	8	change_cita
24	Can delete cita	8	delete_cita
25	Can add cat estatuscita	9	add_catestatuscita
26	Can change cat estatuscita	9	change_catestatuscita
27	Can delete cat estatuscita	9	delete_catestatuscita
28	Can add reporte actividad	10	add_reporteactividad
29	Can change reporte actividad	10	change_reporteactividad
30	Can delete reporte actividad	10	delete_reporteactividad
31	Can add origen recomendacion	11	add_origenrecomendacion
32	Can change origen recomendacion	11	change_origenrecomendacion
33	Can delete origen recomendacion	11	delete_origenrecomendacion
34	Can add recomendado cliente	12	add_recomendadocliente
35	Can change recomendado cliente	12	change_recomendadocliente
36	Can delete recomendado cliente	12	delete_recomendadocliente
37	Can add estatus	13	add_estatus
38	Can change estatus	13	change_estatus
39	Can delete estatus	13	delete_estatus
40	Can add asesor cliente	14	add_asesorcliente
41	Can change asesor cliente	14	change_asesorcliente
42	Can delete asesor cliente	14	delete_asesorcliente
43	Can add sale	15	add_sale
44	Can change sale	15	change_sale
45	Can delete sale	15	delete_sale
46	Can add estatuscredito	16	add_estatuscredito
47	Can change estatuscredito	16	change_estatuscredito
48	Can delete estatuscredito	16	delete_estatuscredito
49	Can add creditos	17	add_creditos
50	Can change creditos	17	change_creditos
51	Can delete creditos	17	delete_creditos
52	Can add roles	18	add_roles
53	Can change roles	18	change_roles
54	Can delete roles	18	delete_roles
55	Can add persona	19	add_persona
56	Can change persona	19	change_persona
57	Can delete persona	19	delete_persona
58	Can add cat tipodireccion	20	add_cattipodireccion
59	Can change cat tipodireccion	20	change_cattipodireccion
60	Can delete cat tipodireccion	20	delete_cattipodireccion
61	Can add direccion	21	add_direccion
62	Can change direccion	21	change_direccion
63	Can delete direccion	21	delete_direccion
64	Can add estado civil	22	add_estadocivil
65	Can change estado civil	22	change_estadocivil
66	Can delete estado civil	22	delete_estadocivil
67	Can add contacto	23	add_contacto
68	Can change contacto	23	change_contacto
69	Can delete contacto	23	delete_contacto
70	Can add servicio	24	add_servicio
71	Can change servicio	24	change_servicio
72	Can delete servicio	24	delete_servicio
73	Can add departamento	25	add_departamento
74	Can change departamento	25	change_departamento
75	Can delete departamento	25	delete_departamento
76	Can add cat pais	26	add_catpais
77	Can change cat pais	26	change_catpais
78	Can delete cat pais	26	delete_catpais
79	Can add institucion financiera	27	add_institucionfinanciera
80	Can change institucion financiera	27	change_institucionfinanciera
81	Can delete institucion financiera	27	delete_institucionfinanciera
82	Can add localidad	28	add_localidad
83	Can change localidad	28	change_localidad
84	Can delete localidad	28	delete_localidad
85	Can add cat estados	29	add_catestados
86	Can change cat estados	29	change_catestados
87	Can delete cat estados	29	delete_catestados
88	Can add promotor asesor	30	add_promotorasesor
89	Can change promotor asesor	30	change_promotorasesor
90	Can delete promotor asesor	30	delete_promotorasesor
91	Can add sesion1	31	add_sesion1
92	Can change sesion1	31	change_sesion1
93	Can delete sesion1	31	delete_sesion1
94	Can add capitalizacion	32	add_capitalizacion
95	Can change capitalizacion	32	change_capitalizacion
96	Can delete capitalizacion	32	delete_capitalizacion
97	Can add libertadfinanciera	33	add_libertadfinanciera
98	Can change libertadfinanciera	33	change_libertadfinanciera
99	Can delete libertadfinanciera	33	delete_libertadfinanciera
100	Can add blindajefinanciero	34	add_blindajefinanciero
101	Can change blindajefinanciero	34	change_blindajefinanciero
102	Can delete blindajefinanciero	34	delete_blindajefinanciero
103	Can add planes concretados	35	add_planesconcretados
104	Can change planes concretados	35	change_planesconcretados
105	Can delete planes concretados	35	delete_planesconcretados
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('auth_permission_id_seq', 105, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
8	pbkdf2_sha256$36000$iyPiY49qgvWq$5wpS0DbPHle4UuXMNnGpJtBDSTmQpADzKFdg6uSICkw=	\N	f	Smariab	Santa	Barrera Ramirez	smariab11@gmail.com	f	t	2017-11-26 07:41:18.662463-06
9	pbkdf2_sha256$36000$k4NxnaAJbcI9$e+uVIyDaPfuIqroOFj0r5tRRj/uVMNlzEw4BO8DYOho=	2017-11-26 11:05:07.657459-06	f	rosita	Rosa	Chavez Barrera	rosita@gmail.com	f	t	2017-11-26 08:01:27.677102-06
10	pbkdf2_sha256$36000$9xzF0cGARX2F$uq+LXPLCarkYMVXYBgpZjwks5KZgajDJZFveHOPDyqw=	2017-11-26 11:09:22.172154-06	f	andy	Andres	Lopez Sanchez	andres@gmail.com	f	t	2017-11-26 08:31:59.22658-06
1	pbkdf2_sha256$36000$NbIOE2SUGQxH$LkCu9E7YJiSOGc75BeBxZMPzcr+Y1EFL5yNkaayy0vs=	2017-12-17 10:50:09.243934-06	t	huitzoo	Oscar	Chavez Barrera	eckobik@gmail.com	t	t	2017-11-25 16:49:29-06
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('auth_user_id_seq', 10, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: cliente_asesorcliente; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY cliente_asesorcliente ("idAsesorCliente", "clienteProspecto", "fechaActualizacion", ocupacion, dependientes, ingresos, link, password, nombre, activo, "Estatus_id", "Origen_id", "idAsesor_id", "idCliente_id", fecha) FROM stdin;
5	f	2017-11-26	\N	\N	\N	\N	\N	\N	t	1	1	1	8	2017-11-28 22:06:00-06
7	f	2017-11-26	\N	\N	\N	\N	\N	\N	t	1	1	1	10	2017-11-27 10:45:00-06
6	f	2017-11-26	\N	\N	\N	\N	\N	\N	t	1	1	1	9	2017-11-30 23:08:00-06
\.


--
-- Name: cliente_asesorcliente_idAsesorCliente_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"cliente_asesorcliente_idAsesorCliente_seq"', 7, true);


--
-- Data for Name: cliente_estatus; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY cliente_estatus ("idEstatus", nombre, descripcion) FROM stdin;
1	Sin asignar	\N
\.


--
-- Name: cliente_estatus_idEstatus_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"cliente_estatus_idEstatus_seq"', 1, true);


--
-- Data for Name: cliente_origenrecomendacion; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY cliente_origenrecomendacion ("idOrigen", nombre, descripcion) FROM stdin;
1	Sin asignar	\N
\.


--
-- Name: cliente_origenrecomendacion_idOrigen_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"cliente_origenrecomendacion_idOrigen_seq"', 1, true);


--
-- Data for Name: cliente_recomendadocliente; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY cliente_recomendadocliente (id, nombre, celular, hijos, activo, asesor_id, "estadoCivil_id") FROM stdin;
\.


--
-- Name: cliente_recomendadocliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('cliente_recomendadocliente_id_seq', 1, false);


--
-- Data for Name: creditos_creditos; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY creditos_creditos ("idCredito", "estatusCredito_id", "idAsesor_id", "idCliente_id") FROM stdin;
\.


--
-- Name: creditos_creditos_idCredito_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"creditos_creditos_idCredito_seq"', 1, false);


--
-- Data for Name: creditos_estatuscredito; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY creditos_estatuscredito (idestatuscredito, nombre, descripcion) FROM stdin;
\.


--
-- Name: creditos_estatuscredito_idestatuscredito_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('creditos_estatuscredito_idestatuscredito_seq', 1, false);


--
-- Data for Name: creditos_sale; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY creditos_sale (id) FROM stdin;
\.


--
-- Name: creditos_sale_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('creditos_sale_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2017-11-25 16:50:34.901224-06	1	Sin asignar	1	[{"added": {}}]	22	1
2	2017-11-25 16:50:38.053438-06	2	SOlte	1	[{"added": {}}]	22	1
3	2017-11-25 16:50:46.0251-06	2	Soltero	2	[{"changed": {"fields": ["nombre"]}}]	22	1
4	2017-11-25 16:51:33.370026-06	1	Cliente	1	[{"added": {}}]	18	1
5	2017-11-25 16:52:46.799744-06	2	Asesor	1	[{"added": {}}]	18	1
6	2017-11-25 16:52:59.679212-06	3	Asesor-Promotor	1	[{"added": {}}]	18	1
7	2017-11-25 16:53:44.993372-06	1	Sin asignar	1	[{"added": {}}]	20	1
8	2017-11-25 16:54:07.06991-06	1	Sin asignar	1	[{"added": {}}]	11	1
9	2017-11-25 16:54:38.629282-06	1	Sin asignar	1	[{"added": {}}]	13	1
10	2017-11-25 16:54:51.501643-06	1	Sin asignar	1	[{"added": {}}]	9	1
11	2017-11-25 16:54:56.394508-06	2	En espera	1	[{"added": {}}]	9	1
12	2017-11-25 16:55:08.329786-06	1	Sin asignar	1	[{"added": {}}]	7	1
13	2017-11-25 16:55:14.469014-06	2	Sesion 1	1	[{"added": {}}]	7	1
14	2017-11-25 16:55:57.802171-06	1		2	[{"changed": {"fields": ["idRol", "estadoCivil"]}}]	19	1
15	2017-11-25 16:57:18.336559-06	1	huitzoo	2	[{"changed": {"fields": ["first_name", "last_name"]}}]	4	1
16	2017-11-25 17:07:34.720802-06	2	oscarin	3		4	1
17	2017-11-25 17:57:13.064862-06	1	Cita object	3		8	1
18	2017-11-25 17:57:46.643425-06	3	AsesorCliente object	3		14	1
19	2017-11-26 07:03:53.484472-06	5	juanito	3		4	1
20	2017-11-26 07:06:57.514897-06	6	juan	3		4	1
21	2017-11-26 07:38:54.716578-06	4	AsesorCliente object	3		14	1
22	2017-11-26 07:39:27.386413-06	7	JuanCr	3		4	1
23	2017-11-26 07:39:27.390318-06	4	oscarin	3		4	1
24	2017-11-26 07:39:27.393931-06	3	Oscarin	3		4	1
25	2017-11-26 09:24:39.425596-06	5	Direccion object	2	[]	21	1
26	2017-11-26 09:24:48.698182-06	6	Direccion object	1	[{"added": {}}]	21	1
27	2017-11-26 10:48:20.017338-06	7	Direccion object	1	[{"added": {}}]	21	1
28	2017-11-26 10:48:43.514824-06	6	Contacto object	1	[{"added": {}}]	23	1
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 28, true);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	agenda	cattipocita
8	agenda	cita
9	agenda	catestatuscita
10	asesor	reporteactividad
11	cliente	origenrecomendacion
12	cliente	recomendadocliente
13	cliente	estatus
14	cliente	asesorcliente
15	creditos	sale
16	creditos	estatuscredito
17	creditos	creditos
18	login	roles
19	login	persona
20	login	cattipodireccion
21	login	direccion
22	login	estadocivil
23	login	contacto
24	productos	servicio
25	productos	departamento
26	productos	catpais
27	productos	institucionfinanciera
28	productos	localidad
29	productos	catestados
30	promotor	promotorasesor
31	sesion1	sesion1
32	sesion1	capitalizacion
33	sesion1	libertadfinanciera
34	sesion1	blindajefinanciero
35	ventas	planesconcretados
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('django_content_type_id_seq', 35, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2017-11-25 14:57:01.073556-06
2	auth	0001_initial	2017-11-25 14:57:01.264874-06
3	admin	0001_initial	2017-11-25 14:57:01.324382-06
4	admin	0002_logentry_remove_auto_add	2017-11-25 14:57:01.350265-06
5	login	0001_initial	2017-11-25 14:57:01.57275-06
6	cliente	0001_initial	2017-11-25 14:57:01.785197-06
7	agenda	0001_initial	2017-11-25 14:57:01.888236-06
8	asesor	0001_initial	2017-11-25 14:57:01.951712-06
9	contenttypes	0002_remove_content_type_name	2017-11-25 14:57:02.022449-06
10	auth	0002_alter_permission_name_max_length	2017-11-25 14:57:02.039617-06
11	auth	0003_alter_user_email_max_length	2017-11-25 14:57:02.069487-06
12	auth	0004_alter_user_username_opts	2017-11-25 14:57:02.097838-06
13	auth	0005_alter_user_last_login_null	2017-11-25 14:57:02.134557-06
14	auth	0006_require_contenttypes_0002	2017-11-25 14:57:02.139936-06
15	auth	0007_alter_validators_add_error_messages	2017-11-25 14:57:02.16845-06
16	auth	0008_alter_user_username_max_length	2017-11-25 14:57:02.211322-06
17	productos	0001_initial	2017-11-25 14:57:02.481482-06
18	promotor	0001_initial	2017-11-25 14:57:02.564751-06
19	sesion1	0001_initial	2017-11-25 14:57:02.695305-06
20	sessions	0001_initial	2017-11-25 14:57:02.737598-06
21	ventas	0001_initial	2017-11-25 14:57:02.828687-06
22	creditos	0001_initial	2017-11-25 17:00:56.330042-06
23	cliente	0002_auto_20171125_2308	2017-11-25 17:08:33.245844-06
24	cliente	0003_auto_20171126_1258	2017-11-26 06:58:59.171425-06
25	cliente	0004_auto_20171126_1340	2017-11-26 07:40:29.12201-06
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('django_migrations_id_seq', 25, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
8ds8cyhsexthfkpi8f999m6io8ld794v	OTkyNTkzZTliNzIwMDM3MTMwMjc5NDczMTk4ZDg4ODBiYmRkMTBhNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTFlMDhkYjU5MTM1NDM1NGRhM2E0OTVkMWM3Nzk0MGQzOWIwMGExNSIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2017-12-10 11:15:58.383779-06
jovzceb9k5gnt94578qbojixg2225okw	OTkyNTkzZTliNzIwMDM3MTMwMjc5NDczMTk4ZDg4ODBiYmRkMTBhNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTFlMDhkYjU5MTM1NDM1NGRhM2E0OTVkMWM3Nzk0MGQzOWIwMGExNSIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2017-12-13 12:48:25.510243-06
j8zkyxfh9uiydz0quxjqkudna0dycg9c	YTllOTBmYzYxOWJlZTE2MzRjOTNkMzljZThkODg1YThlZDVmZDUzMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTFlMDhkYjU5MTM1NDM1NGRhM2E0OTVkMWM3Nzk0MGQzOWIwMGExNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2017-12-31 10:50:09.259322-06
\.


--
-- Data for Name: login_cattipodireccion; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY login_cattipodireccion ("idtipoDireccion", nombre, descripcion) FROM stdin;
1	Sin asignar	\N
\.


--
-- Data for Name: login_contacto; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY login_contacto (id, celular, telcasa, oficina, facebookid, idpersona_id) FROM stdin;
3	556643643				8
4	535364343				9
5	5570707070				10
6	5549140474	26108029	\N	\N	1
\.


--
-- Name: login_contacto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('login_contacto_id_seq', 6, true);


--
-- Data for Name: login_direccion; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY login_direccion (iddireccion, calle, colonia, delegacion, cp, numinterior, numexterior, idpersona_id, idtipodireccion_id) FROM stdin;
3							8	1
4							9	1
5	\N	\N	\N	\N	\N	\N	10	1
6	\N	\N	\N	\N	\N	\N	10	1
7	gitana 331	Col. Del mar	Tlahuac	13270	\N	\N	1	1
\.


--
-- Name: login_direccion_iddireccion_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('login_direccion_iddireccion_seq', 7, true);


--
-- Data for Name: login_estadocivil; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY login_estadocivil ("idEstadoCivil", nombre) FROM stdin;
1	Sin asignar
2	Soltero
\.


--
-- Data for Name: login_persona; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY login_persona (id, curp, rfc, "fechaDeNacimiento", "estadoCivil_id", "idRol_id", user_id) FROM stdin;
1	\N	\N	\N	2	3	1
8				1	1	8
9				1	1	9
10				1	1	10
\.


--
-- Name: login_persona_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('login_persona_id_seq', 10, true);


--
-- Data for Name: login_roles; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY login_roles ("idRole", nombre, descripcion) FROM stdin;
1	Cliente	Es un cliente
2	Asesor	Es un Asesor
3	Asesor-Promotor	Es un asesor promotor
\.


--
-- Name: login_roles_idRole_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"login_roles_idRole_seq"', 3, true);


--
-- Data for Name: productos_catestados; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY productos_catestados ("idEstado", nombre, "idPais_id") FROM stdin;
\.


--
-- Name: productos_catestados_idEstado_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"productos_catestados_idEstado_seq"', 1, false);


--
-- Data for Name: productos_catpais; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY productos_catpais ("idPais", nombre) FROM stdin;
\.


--
-- Name: productos_catpais_idPais_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"productos_catpais_idPais_seq"', 1, false);


--
-- Data for Name: productos_departamento; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY productos_departamento ("idDepartamento", nombre, ubicacion, telefono, extension, "idInstitucion_id") FROM stdin;
\.


--
-- Name: productos_departamento_idDepartamento_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"productos_departamento_idDepartamento_seq"', 1, false);


--
-- Data for Name: productos_institucionfinanciera; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY productos_institucionfinanciera ("idInstitucion", nombre, calle, colonia, cp, num_int, num_ext, "idLocalidad_id", "idPersona_id") FROM stdin;
\.


--
-- Name: productos_institucionfinanciera_idInstitucion_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"productos_institucionfinanciera_idInstitucion_seq"', 1, false);


--
-- Data for Name: productos_localidad; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY productos_localidad ("idLocalidad", nombre, "CatEstados_id", "CatPais_id") FROM stdin;
\.


--
-- Name: productos_localidad_idLocalidad_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"productos_localidad_idLocalidad_seq"', 1, false);


--
-- Data for Name: productos_servicio; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY productos_servicio ("idServicio", descripcion, nombre, "idDepartamento_id") FROM stdin;
\.


--
-- Name: productos_servicio_idServicio_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"productos_servicio_idServicio_seq"', 1, false);


--
-- Data for Name: promotor_promotorasesor; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY promotor_promotorasesor ("idAsesorPromotor", activo, "idAsesor_id", "idPromotor_id", institucion_id) FROM stdin;
\.


--
-- Name: promotor_promotorasesor_idAsesorPromotor_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"promotor_promotorasesor_idAsesorPromotor_seq"', 1, false);


--
-- Data for Name: sesion1_blindajefinanciero; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY sesion1_blindajefinanciero (idbl, "column") FROM stdin;
\.


--
-- Name: sesion1_blindajefinanciero_idbl_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('sesion1_blindajefinanciero_idbl_seq', 1, false);


--
-- Data for Name: sesion1_capitalizacion; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY sesion1_capitalizacion (idcapitalizacion, "column") FROM stdin;
\.


--
-- Name: sesion1_capitalizacion_idcapitalizacion_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('sesion1_capitalizacion_idcapitalizacion_seq', 1, false);


--
-- Data for Name: sesion1_libertadfinanciera; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY sesion1_libertadfinanciera (idlf, edad, "montoObjetivo", anos, ahorro) FROM stdin;
\.


--
-- Name: sesion1_libertadfinanciera_idlf_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('sesion1_libertadfinanciera_idlf_seq', 1, false);


--
-- Data for Name: sesion1_sesion1; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY sesion1_sesion1 ("idSesion", "videoPresentacion", "cartaConfidencialidad", "blindajeFinancieroidbl_id", "idAsesorCliente_id", "idCapitalizacion_id", "libertadFinancieraiDlf_id") FROM stdin;
\.


--
-- Name: sesion1_sesion1_idSesion_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"sesion1_sesion1_idSesion_seq"', 1, false);


--
-- Data for Name: ventas_planesconcretados; Type: TABLE DATA; Schema: public; Owner: vive
--

COPY ventas_planesconcretados ("idPlan", "fechaContratacion", "numeroPoliza", "primaNetaAnual", "plazoAnos", "valorPlan", observaciones, "idAsesor_id", "idCliente_id", "idServicio_id") FROM stdin;
\.


--
-- Name: ventas_planesconcretados_idPlan_seq; Type: SEQUENCE SET; Schema: public; Owner: vive
--

SELECT pg_catalog.setval('"ventas_planesconcretados_idPlan_seq"', 1, false);


--
-- Name: agenda_catestatuscita agenda_catestatuscita_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY agenda_catestatuscita
    ADD CONSTRAINT agenda_catestatuscita_pkey PRIMARY KEY ("idEstatus");


--
-- Name: agenda_cattipocita agenda_cattipocita_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY agenda_cattipocita
    ADD CONSTRAINT agenda_cattipocita_pkey PRIMARY KEY ("idTipoCita");


--
-- Name: agenda_cita agenda_cita_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY agenda_cita
    ADD CONSTRAINT agenda_cita_pkey PRIMARY KEY ("idCita");


--
-- Name: asesor_reporteactividad asesor_reporteactividad_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY asesor_reporteactividad
    ADD CONSTRAINT asesor_reporteactividad_pkey PRIMARY KEY ("idReporte");


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: cliente_asesorcliente cliente_asesorcliente_idCliente_id_key; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_asesorcliente
    ADD CONSTRAINT "cliente_asesorcliente_idCliente_id_key" UNIQUE ("idCliente_id");


--
-- Name: cliente_asesorcliente cliente_asesorcliente_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_asesorcliente
    ADD CONSTRAINT cliente_asesorcliente_pkey PRIMARY KEY ("idAsesorCliente");


--
-- Name: cliente_estatus cliente_estatus_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_estatus
    ADD CONSTRAINT cliente_estatus_pkey PRIMARY KEY ("idEstatus");


--
-- Name: cliente_origenrecomendacion cliente_origenrecomendacion_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_origenrecomendacion
    ADD CONSTRAINT cliente_origenrecomendacion_pkey PRIMARY KEY ("idOrigen");


--
-- Name: cliente_recomendadocliente cliente_recomendadocliente_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_recomendadocliente
    ADD CONSTRAINT cliente_recomendadocliente_pkey PRIMARY KEY (id);


--
-- Name: creditos_creditos creditos_creditos_idCliente_id_key; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_creditos
    ADD CONSTRAINT "creditos_creditos_idCliente_id_key" UNIQUE ("idCliente_id");


--
-- Name: creditos_creditos creditos_creditos_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_creditos
    ADD CONSTRAINT creditos_creditos_pkey PRIMARY KEY ("idCredito");


--
-- Name: creditos_estatuscredito creditos_estatuscredito_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_estatuscredito
    ADD CONSTRAINT creditos_estatuscredito_pkey PRIMARY KEY (idestatuscredito);


--
-- Name: creditos_sale creditos_sale_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_sale
    ADD CONSTRAINT creditos_sale_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: login_cattipodireccion login_cattipodireccion_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_cattipodireccion
    ADD CONSTRAINT login_cattipodireccion_pkey PRIMARY KEY ("idtipoDireccion");


--
-- Name: login_contacto login_contacto_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_contacto
    ADD CONSTRAINT login_contacto_pkey PRIMARY KEY (id);


--
-- Name: login_direccion login_direccion_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_direccion
    ADD CONSTRAINT login_direccion_pkey PRIMARY KEY (iddireccion);


--
-- Name: login_estadocivil login_estadocivil_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_estadocivil
    ADD CONSTRAINT login_estadocivil_pkey PRIMARY KEY ("idEstadoCivil");


--
-- Name: login_persona login_persona_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_persona
    ADD CONSTRAINT login_persona_pkey PRIMARY KEY (id);


--
-- Name: login_persona login_persona_user_id_key; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_persona
    ADD CONSTRAINT login_persona_user_id_key UNIQUE (user_id);


--
-- Name: login_roles login_roles_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_roles
    ADD CONSTRAINT login_roles_pkey PRIMARY KEY ("idRole");


--
-- Name: productos_catestados productos_catestados_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_catestados
    ADD CONSTRAINT productos_catestados_pkey PRIMARY KEY ("idEstado");


--
-- Name: productos_catpais productos_catpais_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_catpais
    ADD CONSTRAINT productos_catpais_pkey PRIMARY KEY ("idPais");


--
-- Name: productos_departamento productos_departamento_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_departamento
    ADD CONSTRAINT productos_departamento_pkey PRIMARY KEY ("idDepartamento");


--
-- Name: productos_institucionfinanciera productos_institucionfinanciera_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_institucionfinanciera
    ADD CONSTRAINT productos_institucionfinanciera_pkey PRIMARY KEY ("idInstitucion");


--
-- Name: productos_localidad productos_localidad_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_localidad
    ADD CONSTRAINT productos_localidad_pkey PRIMARY KEY ("idLocalidad");


--
-- Name: productos_servicio productos_servicio_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_servicio
    ADD CONSTRAINT productos_servicio_pkey PRIMARY KEY ("idServicio");


--
-- Name: promotor_promotorasesor promotor_promotorasesor_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY promotor_promotorasesor
    ADD CONSTRAINT promotor_promotorasesor_pkey PRIMARY KEY ("idAsesorPromotor");


--
-- Name: sesion1_blindajefinanciero sesion1_blindajefinanciero_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_blindajefinanciero
    ADD CONSTRAINT sesion1_blindajefinanciero_pkey PRIMARY KEY (idbl);


--
-- Name: sesion1_capitalizacion sesion1_capitalizacion_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_capitalizacion
    ADD CONSTRAINT sesion1_capitalizacion_pkey PRIMARY KEY (idcapitalizacion);


--
-- Name: sesion1_libertadfinanciera sesion1_libertadfinanciera_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_libertadfinanciera
    ADD CONSTRAINT sesion1_libertadfinanciera_pkey PRIMARY KEY (idlf);


--
-- Name: sesion1_sesion1 sesion1_sesion1_idAsesorCliente_id_key; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_sesion1
    ADD CONSTRAINT "sesion1_sesion1_idAsesorCliente_id_key" UNIQUE ("idAsesorCliente_id");


--
-- Name: sesion1_sesion1 sesion1_sesion1_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_sesion1
    ADD CONSTRAINT sesion1_sesion1_pkey PRIMARY KEY ("idSesion");


--
-- Name: ventas_planesconcretados ventas_planesconcretados_pkey; Type: CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY ventas_planesconcretados
    ADD CONSTRAINT ventas_planesconcretados_pkey PRIMARY KEY ("idPlan");


--
-- Name: agenda_cita_idAsesorCliente_id_67e8e83c; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "agenda_cita_idAsesorCliente_id_67e8e83c" ON agenda_cita USING btree ("idAsesorCliente_id");


--
-- Name: agenda_cita_idEstatus_id_65b62f62; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "agenda_cita_idEstatus_id_65b62f62" ON agenda_cita USING btree ("idEstatus_id");


--
-- Name: agenda_cita_idTipoCita_id_7c5fc631; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "agenda_cita_idTipoCita_id_7c5fc631" ON agenda_cita USING btree ("idTipoCita_id");


--
-- Name: asesor_reporteactividad_idAsesor_id_6fc5af39; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "asesor_reporteactividad_idAsesor_id_6fc5af39" ON asesor_reporteactividad USING btree ("idAsesor_id");


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: cliente_asesorcliente_Estatus_id_f8a34a38; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "cliente_asesorcliente_Estatus_id_f8a34a38" ON cliente_asesorcliente USING btree ("Estatus_id");


--
-- Name: cliente_asesorcliente_Origen_id_374b7108; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "cliente_asesorcliente_Origen_id_374b7108" ON cliente_asesorcliente USING btree ("Origen_id");


--
-- Name: cliente_asesorcliente_idAsesor_id_1fee84e7; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "cliente_asesorcliente_idAsesor_id_1fee84e7" ON cliente_asesorcliente USING btree ("idAsesor_id");


--
-- Name: cliente_recomendadocliente_asesor_id_9bd915b7; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX cliente_recomendadocliente_asesor_id_9bd915b7 ON cliente_recomendadocliente USING btree (asesor_id);


--
-- Name: cliente_recomendadocliente_estadoCivil_id_3522af5f; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "cliente_recomendadocliente_estadoCivil_id_3522af5f" ON cliente_recomendadocliente USING btree ("estadoCivil_id");


--
-- Name: creditos_creditos_estatusCredito_id_c4964821; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "creditos_creditos_estatusCredito_id_c4964821" ON creditos_creditos USING btree ("estatusCredito_id");


--
-- Name: creditos_creditos_idAsesor_id_e7f39a47; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "creditos_creditos_idAsesor_id_e7f39a47" ON creditos_creditos USING btree ("idAsesor_id");


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: login_contacto_idpersona_id_9cab37c7; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX login_contacto_idpersona_id_9cab37c7 ON login_contacto USING btree (idpersona_id);


--
-- Name: login_direccion_idpersona_id_d4c95c1e; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX login_direccion_idpersona_id_d4c95c1e ON login_direccion USING btree (idpersona_id);


--
-- Name: login_direccion_idtipodireccion_id_60332f4e; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX login_direccion_idtipodireccion_id_60332f4e ON login_direccion USING btree (idtipodireccion_id);


--
-- Name: login_persona_estadoCivil_id_e3958123; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "login_persona_estadoCivil_id_e3958123" ON login_persona USING btree ("estadoCivil_id");


--
-- Name: login_persona_idRol_id_6eedffe4; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "login_persona_idRol_id_6eedffe4" ON login_persona USING btree ("idRol_id");


--
-- Name: productos_catestados_idPais_id_69b16272; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "productos_catestados_idPais_id_69b16272" ON productos_catestados USING btree ("idPais_id");


--
-- Name: productos_departamento_idInstitucion_id_b379bb1a; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "productos_departamento_idInstitucion_id_b379bb1a" ON productos_departamento USING btree ("idInstitucion_id");


--
-- Name: productos_institucionfinanciera_idLocalidad_id_cca614bb; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "productos_institucionfinanciera_idLocalidad_id_cca614bb" ON productos_institucionfinanciera USING btree ("idLocalidad_id");


--
-- Name: productos_institucionfinanciera_idPersona_id_6a7ab597; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "productos_institucionfinanciera_idPersona_id_6a7ab597" ON productos_institucionfinanciera USING btree ("idPersona_id");


--
-- Name: productos_localidad_CatEstados_id_0b638aa4; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "productos_localidad_CatEstados_id_0b638aa4" ON productos_localidad USING btree ("CatEstados_id");


--
-- Name: productos_localidad_CatPais_id_6bb91643; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "productos_localidad_CatPais_id_6bb91643" ON productos_localidad USING btree ("CatPais_id");


--
-- Name: productos_servicio_idDepartamento_id_15cd5e4a; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "productos_servicio_idDepartamento_id_15cd5e4a" ON productos_servicio USING btree ("idDepartamento_id");


--
-- Name: promotor_promotorasesor_idAsesor_id_c44afffd; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "promotor_promotorasesor_idAsesor_id_c44afffd" ON promotor_promotorasesor USING btree ("idAsesor_id");


--
-- Name: promotor_promotorasesor_idPromotor_id_8f7c5fca; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "promotor_promotorasesor_idPromotor_id_8f7c5fca" ON promotor_promotorasesor USING btree ("idPromotor_id");


--
-- Name: promotor_promotorasesor_institucion_id_8a0eb282; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX promotor_promotorasesor_institucion_id_8a0eb282 ON promotor_promotorasesor USING btree (institucion_id);


--
-- Name: sesion1_sesion1_blindajeFinancieroidbl_id_7e9b7948; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "sesion1_sesion1_blindajeFinancieroidbl_id_7e9b7948" ON sesion1_sesion1 USING btree ("blindajeFinancieroidbl_id");


--
-- Name: sesion1_sesion1_idCapitalizacion_id_46f7d8da; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "sesion1_sesion1_idCapitalizacion_id_46f7d8da" ON sesion1_sesion1 USING btree ("idCapitalizacion_id");


--
-- Name: sesion1_sesion1_libertadFinancieraiDlf_id_bd113c84; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "sesion1_sesion1_libertadFinancieraiDlf_id_bd113c84" ON sesion1_sesion1 USING btree ("libertadFinancieraiDlf_id");


--
-- Name: ventas_planesconcretados_idAsesor_id_f68c075b; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "ventas_planesconcretados_idAsesor_id_f68c075b" ON ventas_planesconcretados USING btree ("idAsesor_id");


--
-- Name: ventas_planesconcretados_idCliente_id_05277f4d; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "ventas_planesconcretados_idCliente_id_05277f4d" ON ventas_planesconcretados USING btree ("idCliente_id");


--
-- Name: ventas_planesconcretados_idServicio_id_79d29715; Type: INDEX; Schema: public; Owner: vive
--

CREATE INDEX "ventas_planesconcretados_idServicio_id_79d29715" ON ventas_planesconcretados USING btree ("idServicio_id");


--
-- Name: agenda_cita agenda_cita_idAsesorCliente_id_67e8e83c_fk_cliente_a; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY agenda_cita
    ADD CONSTRAINT "agenda_cita_idAsesorCliente_id_67e8e83c_fk_cliente_a" FOREIGN KEY ("idAsesorCliente_id") REFERENCES cliente_asesorcliente("idAsesorCliente") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: agenda_cita agenda_cita_idEstatus_id_65b62f62_fk_agenda_ca; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY agenda_cita
    ADD CONSTRAINT "agenda_cita_idEstatus_id_65b62f62_fk_agenda_ca" FOREIGN KEY ("idEstatus_id") REFERENCES agenda_catestatuscita("idEstatus") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: agenda_cita agenda_cita_idTipoCita_id_7c5fc631_fk_agenda_ca; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY agenda_cita
    ADD CONSTRAINT "agenda_cita_idTipoCita_id_7c5fc631_fk_agenda_ca" FOREIGN KEY ("idTipoCita_id") REFERENCES agenda_cattipocita("idTipoCita") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: asesor_reporteactividad asesor_reporteactividad_idAsesor_id_6fc5af39_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY asesor_reporteactividad
    ADD CONSTRAINT "asesor_reporteactividad_idAsesor_id_6fc5af39_fk_auth_user_id" FOREIGN KEY ("idAsesor_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cliente_asesorcliente cliente_asesorclient_Estatus_id_f8a34a38_fk_cliente_e; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_asesorcliente
    ADD CONSTRAINT "cliente_asesorclient_Estatus_id_f8a34a38_fk_cliente_e" FOREIGN KEY ("Estatus_id") REFERENCES cliente_estatus("idEstatus") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cliente_asesorcliente cliente_asesorclient_Origen_id_374b7108_fk_cliente_o; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_asesorcliente
    ADD CONSTRAINT "cliente_asesorclient_Origen_id_374b7108_fk_cliente_o" FOREIGN KEY ("Origen_id") REFERENCES cliente_origenrecomendacion("idOrigen") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cliente_asesorcliente cliente_asesorcliente_idAsesor_id_1fee84e7_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_asesorcliente
    ADD CONSTRAINT "cliente_asesorcliente_idAsesor_id_1fee84e7_fk_auth_user_id" FOREIGN KEY ("idAsesor_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cliente_asesorcliente cliente_asesorcliente_idCliente_id_3deb9c64_fk_login_persona_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_asesorcliente
    ADD CONSTRAINT "cliente_asesorcliente_idCliente_id_3deb9c64_fk_login_persona_id" FOREIGN KEY ("idCliente_id") REFERENCES login_persona(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cliente_recomendadocliente cliente_recomendadoc_asesor_id_9bd915b7_fk_login_per; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_recomendadocliente
    ADD CONSTRAINT cliente_recomendadoc_asesor_id_9bd915b7_fk_login_per FOREIGN KEY (asesor_id) REFERENCES login_persona(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cliente_recomendadocliente cliente_recomendadoc_estadoCivil_id_3522af5f_fk_login_est; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY cliente_recomendadocliente
    ADD CONSTRAINT "cliente_recomendadoc_estadoCivil_id_3522af5f_fk_login_est" FOREIGN KEY ("estadoCivil_id") REFERENCES login_estadocivil("idEstadoCivil") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: creditos_creditos creditos_creditos_estatusCredito_id_c4964821_fk_creditos_; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_creditos
    ADD CONSTRAINT "creditos_creditos_estatusCredito_id_c4964821_fk_creditos_" FOREIGN KEY ("estatusCredito_id") REFERENCES creditos_estatuscredito(idestatuscredito) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: creditos_creditos creditos_creditos_idAsesor_id_e7f39a47_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_creditos
    ADD CONSTRAINT "creditos_creditos_idAsesor_id_e7f39a47_fk_auth_user_id" FOREIGN KEY ("idAsesor_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: creditos_creditos creditos_creditos_idCliente_id_c9a0d491_fk_cliente_a; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY creditos_creditos
    ADD CONSTRAINT "creditos_creditos_idCliente_id_c9a0d491_fk_cliente_a" FOREIGN KEY ("idCliente_id") REFERENCES cliente_asesorcliente("idAsesorCliente") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: login_contacto login_contacto_idpersona_id_9cab37c7_fk_login_persona_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_contacto
    ADD CONSTRAINT login_contacto_idpersona_id_9cab37c7_fk_login_persona_id FOREIGN KEY (idpersona_id) REFERENCES login_persona(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: login_direccion login_direccion_idpersona_id_d4c95c1e_fk_login_persona_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_direccion
    ADD CONSTRAINT login_direccion_idpersona_id_d4c95c1e_fk_login_persona_id FOREIGN KEY (idpersona_id) REFERENCES login_persona(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: login_direccion login_direccion_idtipodireccion_id_60332f4e_fk_login_cat; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_direccion
    ADD CONSTRAINT login_direccion_idtipodireccion_id_60332f4e_fk_login_cat FOREIGN KEY (idtipodireccion_id) REFERENCES login_cattipodireccion("idtipoDireccion") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: login_persona login_persona_estadoCivil_id_e3958123_fk_login_est; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_persona
    ADD CONSTRAINT "login_persona_estadoCivil_id_e3958123_fk_login_est" FOREIGN KEY ("estadoCivil_id") REFERENCES login_estadocivil("idEstadoCivil") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: login_persona login_persona_idRol_id_6eedffe4_fk_login_roles_idRole; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_persona
    ADD CONSTRAINT "login_persona_idRol_id_6eedffe4_fk_login_roles_idRole" FOREIGN KEY ("idRol_id") REFERENCES login_roles("idRole") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: login_persona login_persona_user_id_826db02f_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY login_persona
    ADD CONSTRAINT login_persona_user_id_826db02f_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_catestados productos_catestados_idPais_id_69b16272_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_catestados
    ADD CONSTRAINT "productos_catestados_idPais_id_69b16272_fk_productos" FOREIGN KEY ("idPais_id") REFERENCES productos_catpais("idPais") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_departamento productos_departamen_idInstitucion_id_b379bb1a_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_departamento
    ADD CONSTRAINT "productos_departamen_idInstitucion_id_b379bb1a_fk_productos" FOREIGN KEY ("idInstitucion_id") REFERENCES productos_institucionfinanciera("idInstitucion") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_institucionfinanciera productos_institucio_idLocalidad_id_cca614bb_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_institucionfinanciera
    ADD CONSTRAINT "productos_institucio_idLocalidad_id_cca614bb_fk_productos" FOREIGN KEY ("idLocalidad_id") REFERENCES productos_localidad("idLocalidad") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_institucionfinanciera productos_institucio_idPersona_id_6a7ab597_fk_login_per; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_institucionfinanciera
    ADD CONSTRAINT "productos_institucio_idPersona_id_6a7ab597_fk_login_per" FOREIGN KEY ("idPersona_id") REFERENCES login_persona(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_localidad productos_localidad_CatEstados_id_0b638aa4_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_localidad
    ADD CONSTRAINT "productos_localidad_CatEstados_id_0b638aa4_fk_productos" FOREIGN KEY ("CatEstados_id") REFERENCES productos_catestados("idEstado") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_localidad productos_localidad_CatPais_id_6bb91643_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_localidad
    ADD CONSTRAINT "productos_localidad_CatPais_id_6bb91643_fk_productos" FOREIGN KEY ("CatPais_id") REFERENCES productos_catpais("idPais") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: productos_servicio productos_servicio_idDepartamento_id_15cd5e4a_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY productos_servicio
    ADD CONSTRAINT "productos_servicio_idDepartamento_id_15cd5e4a_fk_productos" FOREIGN KEY ("idDepartamento_id") REFERENCES productos_departamento("idDepartamento") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: promotor_promotorasesor promotor_promotorase_idAsesor_id_c44afffd_fk_login_per; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY promotor_promotorasesor
    ADD CONSTRAINT "promotor_promotorase_idAsesor_id_c44afffd_fk_login_per" FOREIGN KEY ("idAsesor_id") REFERENCES login_persona(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: promotor_promotorasesor promotor_promotorase_institucion_id_8a0eb282_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY promotor_promotorasesor
    ADD CONSTRAINT promotor_promotorase_institucion_id_8a0eb282_fk_productos FOREIGN KEY (institucion_id) REFERENCES productos_institucionfinanciera("idInstitucion") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: promotor_promotorasesor promotor_promotorasesor_idPromotor_id_8f7c5fca_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY promotor_promotorasesor
    ADD CONSTRAINT "promotor_promotorasesor_idPromotor_id_8f7c5fca_fk_auth_user_id" FOREIGN KEY ("idPromotor_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sesion1_sesion1 sesion1_sesion1_blindajeFinancieroid_7e9b7948_fk_sesion1_b; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_sesion1
    ADD CONSTRAINT "sesion1_sesion1_blindajeFinancieroid_7e9b7948_fk_sesion1_b" FOREIGN KEY ("blindajeFinancieroidbl_id") REFERENCES sesion1_blindajefinanciero(idbl) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sesion1_sesion1 sesion1_sesion1_idAsesorCliente_id_ff3c5bbf_fk_cliente_a; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_sesion1
    ADD CONSTRAINT "sesion1_sesion1_idAsesorCliente_id_ff3c5bbf_fk_cliente_a" FOREIGN KEY ("idAsesorCliente_id") REFERENCES cliente_asesorcliente("idAsesorCliente") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sesion1_sesion1 sesion1_sesion1_idCapitalizacion_id_46f7d8da_fk_sesion1_c; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_sesion1
    ADD CONSTRAINT "sesion1_sesion1_idCapitalizacion_id_46f7d8da_fk_sesion1_c" FOREIGN KEY ("idCapitalizacion_id") REFERENCES sesion1_capitalizacion(idcapitalizacion) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: sesion1_sesion1 sesion1_sesion1_libertadFinancieraiD_bd113c84_fk_sesion1_l; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY sesion1_sesion1
    ADD CONSTRAINT "sesion1_sesion1_libertadFinancieraiD_bd113c84_fk_sesion1_l" FOREIGN KEY ("libertadFinancieraiDlf_id") REFERENCES sesion1_libertadfinanciera(idlf) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ventas_planesconcretados ventas_planesconcret_idCliente_id_05277f4d_fk_login_per; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY ventas_planesconcretados
    ADD CONSTRAINT "ventas_planesconcret_idCliente_id_05277f4d_fk_login_per" FOREIGN KEY ("idCliente_id") REFERENCES login_persona(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ventas_planesconcretados ventas_planesconcret_idServicio_id_79d29715_fk_productos; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY ventas_planesconcretados
    ADD CONSTRAINT "ventas_planesconcret_idServicio_id_79d29715_fk_productos" FOREIGN KEY ("idServicio_id") REFERENCES productos_servicio("idServicio") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ventas_planesconcretados ventas_planesconcretados_idAsesor_id_f68c075b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: vive
--

ALTER TABLE ONLY ventas_planesconcretados
    ADD CONSTRAINT "ventas_planesconcretados_idAsesor_id_f68c075b_fk_auth_user_id" FOREIGN KEY ("idAsesor_id") REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

