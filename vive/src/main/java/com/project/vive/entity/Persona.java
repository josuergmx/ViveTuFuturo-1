package com.project.vive.entity;

import java.util.Date;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "Persona")
public class Persona {
	@Id
	@GeneratedValue
	@Column(name = "idpersona")
	private Integer id;
	
	@Column(name = "nombre")
	private String nombre;
	
	@Column(name = "apellidopaterno")
	private String apellidoPaterno;
	
	@Column(name = "apellidomaterno")
	private String apellidoMaterno;
	
	@Column(name = "curp")
	private String curp;
	
	@Column(name = "rfc")
	private String rfc;
	
	@Column(name = "fechanacimiento")
	private Date fechaNacimiento;
	
	@OneToMany(mappedBy = "propietario")
	private List<Contacto> contactos;
	  
	@OneToMany(mappedBy = "propietario")
	private List<Direccion> direcciones;
	
	public Persona(){
		super();
	}
	
	public Persona(Integer id, String nombre, String apellidoPaterno, String apellidoMaterno, String curp, String rfc,
			Date fechaNacimiento) {
		super();
		this.id = id;
		this.nombre = nombre;
		this.apellidoPaterno = apellidoPaterno;
		this.apellidoMaterno = apellidoMaterno;
		this.curp = curp;
		this.rfc = rfc;
		this.fechaNacimiento = fechaNacimiento;
	}

	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getApellidoPaterno() {
		return apellidoPaterno;
	}
	public void setApellidoPaterno(String apellidoPaterno) {
		this.apellidoPaterno = apellidoPaterno;
	}
	public String getApellidoMaterno() {
		return apellidoMaterno;
	}
	public void setApellidoMaterno(String apellidoMaterno) {
		this.apellidoMaterno = apellidoMaterno;
	}
	public String getCurp() {
		return curp;
	}
	public void setCurp(String curp) {
		this.curp = curp;
	}
	public String getRfc() {
		return rfc;
	}
	public void setRfc(String rfc) {
		this.rfc = rfc;
	}
	public Date getFechaNacimiento() {
		return fechaNacimiento;
	}
	public void setFechaNacimiento(Date fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}

	public List<Contacto> getContactos() {
		return contactos;
	}

	public void setContactos(List<Contacto> contactos) {
		this.contactos = contactos;
	}

	public List<Direccion> getDirecciones() {
		return direcciones;
	}

	public void setDirecciones(List<Direccion> direcciones) {
		this.direcciones = direcciones;
	}
	
	
}
